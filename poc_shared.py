
import hashlib
import json
from collections import Counter
from pathlib import Path


def resposta(status, regra, justificativa):
    return {
        "status": status,
        "regra": regra,
        "justificativa": justificativa,
        "ajuste_automatico": False,
        "revisao_humana": status != "CONCILIADO",
    }


def canonico(dados):
    return json.dumps(
        dados, ensure_ascii=False, sort_keys=True, indent=2
    ) + "\n"


def gravar_imutavel(caminho, dados):
    conteudo = canonico(dados)
    caminho.parent.mkdir(parents=True, exist_ok=True)

    if caminho.exists():
        if caminho.read_text(encoding="utf-8") != conteudo:
            raise RuntimeError(
                f"Integridade comprometida: {caminho}"
            )
        return "REUTILIZADO"

    caminho.write_text(conteudo, encoding="utf-8")
    return "CRIADO"


def executar(base, avaliador, salvar=True):
    base = Path(base)
    entrada = base / "fixtures" / "cenarios.json"
    motor = base / "motor.py"

    casos = json.loads(entrada.read_text(encoding="utf-8"))

    if not isinstance(casos, list) or not casos:
        raise ValueError("Cenarios ausentes ou invalidos")

    ids = [x.get("caso") for x in casos]

    if any(not x for x in ids) or len(set(ids)) != len(ids):
        raise ValueError("Identificadores invalidos ou duplicados")

    origem_hash = hashlib.sha256(
        entrada.read_bytes()
    ).hexdigest()

    motor_hash = hashlib.sha256(
        motor.read_bytes()
    ).hexdigest()

    lote = hashlib.sha256(
        (origem_hash + motor_hash).encode("utf-8")
    ).hexdigest()[:16]

    bronze = []
    silver = []

    for caso in casos:
        if caso.get("origem") != "SINTETICA":
            raise ValueError("Somente dados sinteticos nesta POC")

        resultado = avaliador(caso)

        if resultado["status"] != caso["esperado"]:
            raise AssertionError(
                f"{caso['caso']}: esperado "
                f"{caso['esperado']}, obtido "
                f"{resultado['status']}"
            )

        bronze.append({
            **caso,
            "id_lote": lote,
            "camada": "BRONZE",
        })

        silver.append({
            "caso": caso["caso"],
            "hipotese": caso["hipotese"],
            "id_lote": lote,
            **resultado,
        })

    por_status = dict(
        sorted(Counter(x["status"] for x in silver).items())
    )

    gold = {
        "lote": lote,
        "total": len(silver),
        "por_status": por_status,
        "casos_para_revisao": sum(
            x["revisao_humana"] for x in silver
        ),
        "casos_conciliados": por_status.get("CONCILIADO", 0),
    }

    manifesto = {
        "lote": lote,
        "origem": "DADOS_SINTETICOS",
        "sha256_entrada": origem_hash,
        "sha256_motor": motor_hash,
        "registros_entrada": len(casos),
        "registros_saida": len(silver),
        "escrita_sistema_origem": False,
        "regras_homologadas": False,
    }

    if salvar:
        saida = base / "output"

        arquivos = {
            "raw": casos,
            "bronze": bronze,
            "silver": silver,
            "gold": gold,
            "manifesto": manifesto,
        }

        for camada, dados in arquivos.items():
            caminho = saida / f"{camada}_{lote}.json"
            gravar_imutavel(caminho, dados)

    return {
        "lote": lote,
        "gold": gold,
        "manifesto": manifesto,
        "silver": silver,
    }
