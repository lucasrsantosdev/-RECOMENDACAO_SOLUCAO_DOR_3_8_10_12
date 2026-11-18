# DOR 03 - Investigacao Tecnica v0.2

## Objetivo
Conciliar eventos academicos com faturamento,
titulos, bolsas, pagamentos, estornos e saldos.

## Pontos documentados no mapa V3
- Tombamento das tabelas de valores.
- Tombamento de cobrancas e vencimentos.
- Avanco de alunos e repescagem.
- Remocao e ajuste inteligente de disciplinas.
- Conferencia de recalculo de mensalidades.
- Evolucao financeira.
- Conferencia e aplicacao de bolsas.
- Liberacao da visualizacao do financeiro.
- Validacao de aproveitamento de estudos.

## Problemas investigados
H3.1: cobrancas apos cancelamento.
H3.2: faturamento e notas de pre-candidatos.
H3.3: identificacao do responsavel pelo pagamento.
H3.4: erros e duplicidades de aproveitamento.

## Motor proposto
Entrada:
- Eventos academicos.
- Matriculas e contratos.
- Disciplinas e aproveitamentos.
- Parametros de preco e bolsas.
- Titulos e movimentos financeiros.

Processamento:
- Padronizar chaves.
- Relacionar eventos a titulos.
- Preservar data efetiva e data do registro.
- Aplicar regras parametrizadas por IES.
- Identificar divergencias candidatas.
- Registrar justificativas e proveniencia.

Saida:
- Registros conciliados.
- Divergencias para revisao.
- Casos pendentes de regra homologada.
- Indicadores por competencia e causa.

## Regras ainda nao homologadas
- Cancelamento e trancamento.
- Momento correto da baixa financeira.
- Bolsas integrais e abatimentos.
- Cobrancas apos alteracao de disciplina.
- Nota fiscal zerada de candidato.
- Pagamento de polo versus aluno.
- Classificacao contabil de estornos.

## Restricao
Nao assumir que todo titulo posterior a um evento
academico representa cobranca indevida.

Nao executar baixa nem ajuste no ERP.

## Resultado esperado
POC independente e auditavel com dados sinteticos,
pronta para incorporar regras reais apos homologacao.

Status: investigacao v0.2, motor pendente.
