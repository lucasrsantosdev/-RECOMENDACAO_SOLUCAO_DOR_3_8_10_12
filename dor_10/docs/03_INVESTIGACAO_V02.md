# DOR 10 - Investigacao Tecnica v0.2

## Objetivo
Conciliar cobertura FIES, faturamento,
coparticipacao, repasses e saldos por periodo.

## Fontes previstas
- SisFIES, mediante extracao autorizada.
- Sistema academico.
- Contas a receber.
- Historico de aditamentos.
- Execucoes do RPA existente.

As estruturas e integracoes reais estao pendentes.

## Paliativa
Consolidador de extratos e relatorio de excecoes.

## Definitiva
Motor historico de cobertura FIES integrado
a gestao financeira e rematricula.

## Entidades logicas propostas
- Aluno e contrato.
- Periodo academico.
- Cobertura FIES.
- Aditamento.
- Componente financeiro.
- Titulo.
- Pagamento.
- Evento financeiro.
- Execucao do processo.

## Regras candidatas
- Separar repasse e coparticipacao.
- Identificar alteracao de cobertura.
- Detectar aditamento retroativo.
- Identificar saldo atribuido a cobertura irregular.
- Sinalizar situacao FIES na rematricula.
- Identificar pagamentos para analise de ressarcimento.
- Auditar e monitorar a execucao do RPA.

## Regras pendentes
- Fonte oficial autorizada.
- Vigencia contratual de cada cobertura.
- Formula de calculo dos componentes.
- Tratamento de cancelamento e nao renovacao.
- Procedimento de ressarcimento.
- Requisitos regulatorios e aprovacoes.

## Restricao
Nenhuma integracao automatizada com SisFIES
sera implementada sem autorizacao.

Nao efetuar ressarcimentos ou recalculos na origem.

Status: investigacao v0.2, motor pendente.
