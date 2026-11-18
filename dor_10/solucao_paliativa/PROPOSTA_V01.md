# POC 10 - Solucao Paliativa v0.1

## Nome
Consolidador e Conciliador Financeiro FIES.

## Problema
Inconsistencias no acompanhamento de cobertura,
aditamentos, repasses, coparticipacao e saldos.

## Proposta
Construir motor de importacao e conciliacao
utilizando arquivos e extracoes autorizadas.

Complementar o RPA/ETL e o manual FIES previstos.

## Fluxo
1. Receber extratos autorizados do SisFIES.
2. Receber base academica e financeira.
3. Padronizar aluno, contrato e periodo.
4. Separar repasse FIES e coparticipacao.
5. Validar situacao e vigencia da cobertura.
6. Identificar divergencias de valores.
7. Detectar aditamentos retroativos.
8. Identificar cancelamentos e perdas de cobertura.
9. Produzir relatorio de excecoes.
10. Encaminhar ressarcimentos para analise.

## Regras por hipotese

### H10.1
Separar valor de repasse e coparticipacao.

### H10.2
Comparar relatorios gerenciais com extracoes
individuais autorizadas e identificar inconsistencias.

### H10.3
Identificar pagamentos potencialmente abrangidos
por aditamentos retroativos e casos para ressarcimento.

### H10.4
Apontar pendencias apos cancelamento do FIES,
sem recalculo financeiro automatico nesta fase.

### H10.5
Comparar vigencia de cobertura, situacao FIES,
matricula e saldo atribuido ao programa.

### H10.6
Inventariar o RPA existente, dependencias,
falhas e requisitos regulatorios aplicaveis.

## Dados minimos propostos
- Instituicao, aluno e contrato.
- Periodo academico e competencia financeira.
- Situacao do FIES e sua vigencia.
- Identificador e data do aditamento.
- Valor financiado e coparticipacao.
- Titulos, pagamentos e saldos.
- Eventos de cancelamento e renovacao.
- Data de captura e sistema de origem.

## Entregaveis
- Base sintetica de aditamentos.
- Motor de conciliacao Python.
- Relatorio de saldos divergentes.
- Lista de alunos com cobertura irregular.
- Casos de ajuste retroativo.
- Trilha de processamento e auditoria.

## Limites
- Nao automatizar acesso nao autorizado ao SisFIES.
- Nao executar ressarcimentos.
- Nao alterar contratos ou saldos na origem.
- Nao declarar conformidade regulatoria sem validacao.

## Criterios de aceite
- Separar corretamente os componentes sinteticos.
- Identificar irregularidades simuladas.
- Preservar periodos e alteracoes retroativas.
- Reprocessar sem duplicidade.
- Gerar justificativa rastreavel por divergencia.

Status: proposta tecnica, nao implementada.
