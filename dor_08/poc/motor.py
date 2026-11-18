
from datetime import datetime
from decimal import Decimal
from poc_shared import resposta


def valor(x):
    return Decimal(str(x or 0))


def avaliar(r):
    if r.get("qtd_ndd", 0) != r.get("qtd_faturamento", 0):
        return resposta(
            "DIVERGENCIA_CANDIDATA", "H8.1",
            "Quantidade de documentos divergente"
        )

    if valor(r.get("valor_ndd")) != valor(
        r.get("valor_faturamento")
    ):
        return resposta(
            "DIVERGENCIA_CANDIDATA", "H8.1",
            "Diferenca monetaria; inclusive abaixo de 1%"
        )

    extracao = r.get("data_extracao")
    fechamento = r.get("data_fechamento")

    if extracao and fechamento:
        if datetime.fromisoformat(extracao) < (
            datetime.fromisoformat(fechamento)
        ):
            return resposta(
                "DIVERGENCIA_CANDIDATA", "H8.3",
                "Extracao anterior ao fechamento"
            )

    if not r.get("aprovador"):
        return resposta(
            "PENDENTE_EVIDENCIA", "H8.2",
            "Aprovacao gerencial nao comprovada"
        )

    if r.get("excecao_aberta") and not r.get(
        "justificativa"
    ):
        return resposta(
            "PENDENTE_EVIDENCIA", "H8.4",
            "Excecao sem investigacao documentada"
        )

    return resposta(
        "CONCILIADO", "SEM_ALERTA",
        "Controles sinteticos satisfeitos"
    )
