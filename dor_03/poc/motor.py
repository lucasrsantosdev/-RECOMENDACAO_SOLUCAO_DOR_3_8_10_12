
from datetime import date
from decimal import Decimal
from poc_shared import resposta


def valor(x):
    return Decimal(str(x or 0))


def avaliar(r):
    if r.get("aproveitamento_duplicado"):
        return resposta(
            "DIVERGENCIA_CANDIDATA", "H3.4",
            "Possivel duplicidade de aproveitamento"
        )

    if r.get("disciplina_removida") and (
        r.get("recalculo_executado") is False
    ):
        return resposta(
            "DIVERGENCIA_CANDIDATA", "H3.1",
            "Disciplina removida sem recalculo registrado"
        )

    if r.get("evento") in ("CANCELAMENTO", "TRANCAMENTO"):
        efetiva = r.get("data_efetiva")
        vencimento = r.get("vencimento_titulo")

        if efetiva and vencimento:
            if (
                date.fromisoformat(vencimento)
                > date.fromisoformat(efetiva)
                and valor(r.get("valor_titulo")) > 0
                and not r.get("estornado")
            ):
                return resposta(
                    "DIVERGENCIA_CANDIDATA", "H3.1",
                    "Titulo positivo apos evento academico; "
                    "exige validacao da regra"
                )

    if (
        r.get("bolsa_percentual") == 100
        and valor(r.get("saldo")) > 0
    ):
        return resposta(
            "DIVERGENCIA_CANDIDATA", "H3.1",
            "Bolsa integral com saldo financeiro positivo"
        )

    if (
        r.get("situacao") == "PRE_CANDIDATO"
        and valor(r.get("valor_nota")) == 0
    ):
        return resposta(
            "PENDENTE_REGRA", "H3.2",
            "Nota zerada de pre-candidato requer validacao fiscal"
        )

    if (
        r.get("pagador") == "POLO"
        and r.get("engajamento_aluno")
    ):
        return resposta(
            "PENDENTE_EVIDENCIA", "H3.3",
            "Confirmar correcao da identificacao do pagador"
        )

    if (
        r.get("tipo_ajuste") == "ESTORNO"
        and r.get("classificacao") == "CANCELAMENTO_PERIODO"
    ):
        return resposta(
            "PENDENTE_REGRA", "H3.1",
            "Classificacao contabil do estorno requer revisao"
        )

    return resposta(
        "CONCILIADO", "SEM_ALERTA",
        "Nenhuma regra candidata acionada"
    )
