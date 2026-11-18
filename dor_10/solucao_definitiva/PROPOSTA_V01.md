# POC 10 - Solucao Definitiva v0.1

## Nome
Motor de Governanca e Conformidade Financeira FIES.

## Objetivo
Comprovar que faturamento e saldos do programa
correspondem a cobertura e responsabilidade
financeira dos alunos em cada periodo.

## Arquitetura
SisFIES e fontes internas autorizadas
-> Captura incremental ou periodica
-> RAW / Bronze
-> Historico de cobertura e aditamentos
-> Silver de regras financeiras
-> Conciliacao por aluno e contrato
-> Gold de controle e auditoria.

## Capacidades

### Cobertura e aditamentos
- Historico de situacoes por aluno e periodo.
- Identificacao de aditamentos e renovacoes.
- Controle de vigencias e alteracoes retroativas.
- Comparacao com a situacao da matricula.

### Concilicacao financeira
- Separacao de repasse e coparticipacao.
- Vinculo com titulos, pagamentos e saldos.
- Identificacao de diferencas financeiras.
- Registro de justificativas e aprovacoes.

### Ressarcimentos
- Identificacao de pagamentos potencialmente
  abrangidos por cobertura retroativa.
- Calculo demonstrativo sujeito a validacao.
- Encaminhamento ao fluxo autorizado.
- Historico da decisao e do ajuste.

### Cancelamentos e irregularidades
- Identificacao de perda ou ausencia de renovacao.
- Alertas para analise academica e financeira.
- Sinalizacao antes da rematricula, se viavel.
- Recalculo proposto conforme regras homologadas.

### Integracao e auditoria
- Capturas com proveniencia e data.
- Historico sem sobrescrever versoes anteriores.
- Processamento idempotente.
- Tratamento de falhas e excecoes.
- Controles de qualidade e conciliacao.
- Aprovacao antes de ajustes financeiros.

## Indicadores
- Coberturas vencidas ou irregulares.
- Saldos divergentes por periodo.
- Tempo de identificacao de irregularidade.
- Aditamentos retroativos pendentes.
- Casos de ressarcimento sob analise.
- Percentual de contratos conciliados.
- Dependencia de processamento manual.

## Dependencias
- Fontes oficiais e permissoes.
- Regras do SisFIES e contrato.
- Dicionario financeiro e academico.
- Politica de ressarcimento.
- Responsabilidade pelo monitoramento.
- Revisao dos requisitos regulatorios.
- Avaliacao do RPA existente.
- Homologacao por negocio, TI e financeiro.

## Estrategia
Evoluir progressivamente o RPA/ETL existente,
evitando duplicar automacoes em producao.

Status: arquitetura-alvo proposta, nao implantada.
