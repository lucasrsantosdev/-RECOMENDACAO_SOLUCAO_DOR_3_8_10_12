
import re
from poc_shared import resposta


def avaliar(r):
    cep = str(r.get("cep", "")).strip().replace("-", "")

    if not re.fullmatch(r"\d{8}", cep):
        return resposta(
            "DIVERGENCIA_CANDIDATA", "H12.1",
            "CEP ausente ou estruturalmente invalido"
        )

    if r.get("cadastro_legado") and (
        r.get("endereco_completo") is False
    ):
        return resposta(
            "DIVERGENCIA_CANDIDATA", "H12.1",
            "Cadastro legado incompleto"
        )

    if (
        r.get("uf_referencia")
        and r.get("uf") != r.get("uf_referencia")
    ):
        return resposta(
            "DIVERGENCIA_CANDIDATA", "H12.1",
            "UF divergente da referencia sintetica"
        )

    if r.get("endereco_igual_polo"):
        return resposta(
            "REQUER_REVISAO_HUMANA", "H12.3",
            "Coincidencia com polo nao prova irregularidade"
        )

    if r.get("edicao_apos_cep") and (
        r.get("campo_editado")
        not in ("numero", "complemento")
    ):
        return resposta(
            "PENDENTE_REGRA", "H12.2",
            "Alteracao de endereco requer regra homologada"
        )

    return resposta(
        "CONCILIADO", "SEM_ALERTA",
        "Validacoes estruturais sinteticas satisfeitas"
    )
