# POC 03 - Solucao Definitiva v0.1

## Nome
Plataforma de Integracao e Conciliacao
Academico-Financeira.

## Objetivo
Manter situacao academica, cobrancas, bolsas,
faturamento e saldos reconciliados de forma continua.

## Arquitetura proposta
Sistemas academicos e financeiros
-> Captura de eventos e alteracoes
-> RAW / Bronze
-> Validacoes e regras Silver
-> Motor de conciliacao
-> Gold financeira
-> Monitoramento e auditoria.

## Capacidades

### Integracao academico-financeira
- Receber eventos academicos confirmados.
- Identificar inclusoes, alteracoes e cancelamentos.
- Aplicar regras homologadas por instituicao.
- Impedir cobrancas futuras indevidas conforme regra.
- Controlar respostas e falhas das integracoes.

### Bolsa e responsavel financeiro
- Identificar modalidade e vigencia da bolsa.
- Diferenciar abatimento, baixa e pagamento.
- Identificar o responsavel pelo pagamento.
- Tratar bolsas integrais segundo regra homologada.

### Estornos e ajustes
- Diferenciar cancelamento efetivo de correcao.
- Preservar competencia original e competencia do ajuste.
- Registrar motivo, aprovador e referencia do titulo.
- Nao reclassificar valores automaticamente sem autorizacao.

### Aproveitamento
- Validar duplicidades e regras de aprovacao.
- Conferir reflexos financeiros antes da integracao.

### Historico e rastreabilidade
- Preservar eventos anteriores.
- Processar correcoes retroativas.
- Garantir idempotencia e reconciliacao.
- Manter trilha de auditoria.

## Estrategia
Priorizar integracao e melhoria dos processos existentes.

A troca de Gioconda, Lyceum ou Protheus somente
devera ser considerada apos estudo de viabilidade.

## Dependencias
- Dicionario e chaves dos sistemas.
- Mapeamento dos eventos academicos.
- Regras de faturamento e cancelamento.
- Integracoes e responsabilidades de TI.
- Validacao financeira, contabil e fiscal.
- Estrategia de captura incremental.
- Testes de regressao nos processos existentes.

## Indicadores propostos
- Taxa de divergencia academico-financeira.
- Titulos pendentes de conciliacao.
- Tempo entre evento e ajuste financeiro.
- Quantidade de correcoes manuais.
- Estornos por cobranca indevida.
- Ocorrencias sem responsavel financeiro definido.

## Homologacao
Exigir testes por instituicao, fluxo academico,
tipo de bolsa, competencia e tipo de ajuste.

Status: arquitetura-alvo proposta, nao implantada.
