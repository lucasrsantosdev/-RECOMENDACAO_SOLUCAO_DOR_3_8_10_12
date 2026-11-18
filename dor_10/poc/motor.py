
from decimal import Decimal
from poc_shared import resposta


def valor(x):
    return Decimal(str(x or 0))


def avaliar(r):
    if (
        "repasse_sisfies" in r
        and "repasse_financeiro" in r
        and valor(r["repasse_sisfies"])
        != valor(r["repasse_financeiro"])
    ):
        return resposta(
            "DIVERGENCIA_CANDIDATA", "H10.1",
            "Repasse FIES divergente do financeiro"
        )

    if (
        "resumo_sisfies" in r
        and "detalhado_sisfies" in r
        and valor(r["resumo_sisfies"])
        != valor(r["detalhado_sisfies"])
    ):
        return resposta(
            "DIVERGENCIA_CANDIDATA", "H10.2",
            "Extracao agregada e individual divergentes"
        )

    if (
        r.get("aditamento_retroativo")
        and valor(r.get("pagamento_aluno")) > 0
    ):
        return resposta(
            "PENDENTE_APROVACAO", "H10.3",
            "Possivel ressarcimento; nao executar ajuste"
        )

    if (
        r.get("cobertura") in ("VENCIDA", "NAO_RENOVADA")
        and r.get("matricula_ativa")
    ):
        return resposta(
            "PENDENTE_REGRA", "H10.5",
            "Cobertura irregular em matricula ativa"
        )

    if (
        r.get("fies_cancelado")
        and valor(r.get("saldo_pendente")) > 0
    ):
        return resposta(
            "PENDENTE_REGRA", "H10.4",
            "Saldo apos cancelamento requer analise"
        )

    if r.get("rpa_status") == "FALHA":
        return resposta(
            "PENDENTE_EVIDENCIA", "H10.6",
            "Falha de processamento do RPA existente"
        )

    return resposta(
        "CONCILIADO", "SEM_ALERTA",
        "Nenhuma divergencia sintetica detectada"
    )
