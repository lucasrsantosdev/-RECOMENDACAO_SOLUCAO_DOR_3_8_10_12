# FOURD VITRU - POCs 03, 08, 10 e 12

## Visao geral

Projeto de investigacao, engenharia de dados e
demonstracao de solucoes para quatro dores
academicas, financeiras, fiscais e cadastrais
da Vitru, envolvendo processos da Uniasselvi
e UniCesumar.

**Versao:** POCs funcionais v0.1.
**Investigacao:** Documentacao tecnica v0.2.
**Situacao:** Implementadas e testadas com dados
sinteticos; fontes e regras reais ainda pendentes
de homologacao.

## Objetivo

Compreender as causas das divergencias, propor
controles paliativos e arquiteturas definitivas,
desenvolver mecanismos de validacao e preparar
uma evolucao segura para os dados reais.

## Dores investigadas

| Dor | Tema | Hipoteses |
|---|---|---|
| 03 | Conciliacao Academico-Financeira | H3.1-H3.4 |
| 08 | Conciliacao NDD e Faturamento | H8.1-H8.4 |
| 10 | Governanca Financeira FIES | H10.1-H10.6 |
| 12 | Qualidade Cadastral e Enderecos | H12.1-H12.3 |

## Dor 03 - Conciliacao Academico-Financeira

**Problema investigado:**
Divergencias potenciais entre matriculas,
cancelamentos, trancamentos, disciplinas,
aproveitamentos, bolsas, titulos e faturamento.

**Solucao paliativa:**
Motor independente de conciliacao academica
e financeira, com relatorios de excecoes.

**Solucao definitiva:**
Plataforma de integracao e conciliacao continua
entre sistemas academicos e financeiros,
com historico, auditoria e regras homologadas.

**POC atual:**
9 cenarios sinteticos e 3 testes aprovados.

## Dor 08 - Conciliacao NDD e Faturamento

**Problema investigado:**
Necessidade de comprovar a consistencia entre
documentos fiscais, valores faturados,
fechamentos e aprovacoes.

**Solucao paliativa:**
Validacao dos controles existentes de conciliacao
documental, monetaria, temporal e gerencial.

**Solucao definitiva:**
Governanca automatizada do fechamento fiscal,
com excecoes justificadas e evidencias auditaveis.

**Diretriz:**
Evoluir o processo existente, sem criar solucao
concorrente. O limite de 1% permanece experimental.

**POC atual:**
6 cenarios sinteticos e 3 testes aprovados.

## Dor 10 - Governanca Financeira FIES

**Problema investigado:**
Divergencias potenciais entre cobertura,
aditamentos, repasses, coparticipacao,
pagamentos, cancelamentos e saldos.

**Solucao paliativa:**
Consolidador e conciliador financeiro FIES,
utilizando dados sinteticos ou extratos
devidamente autorizados.

**Solucao definitiva:**
Motor historico de cobertura e conformidade
financeira, integrado aos processos academicos
e financeiros.

**Diretriz:**
Complementar e evoluir o RPA/ETL existente,
sem duplicar automacoes em producao.

**POC atual:**
7 cenarios sinteticos e 3 testes aprovados.

## Dor 12 - Qualidade Cadastral e Enderecos

**Problema investigado:**
Cadastros legados incompletos, alteracoes
de endereco e possivel uso de endereco de polo.

**Solucao paliativa:**
Validador de qualidade cadastral e gerador
de alertas para saneamento.

**Solucao definitiva:**
Governanca preventiva de enderecos,
integrada ao Projeto RT existente.

**Diretriz:**
CEP valido nao comprova residencia efetiva.
Coincidencias com polos exigem revisao humana.

**POC atual:**
7 cenarios sinteticos e 3 testes aprovados.

## Metodologia

Diagnostico -> Hipoteses -> Evidencias ->
Investigacao de causas-raiz ->
Solucao paliativa -> Solucao definitiva ->
POC sintetica -> Testes -> Homologacao ->
Integracao autorizada.

As causas-raiz nao comprovadas permanecem
classificadas como hipoteses.

## Arquitetura implementada

Dados sinteticos
-> RAW
-> Bronze
-> Silver (regras candidatas)
-> Gold (indicadores)
-> Auditoria

As camadas sao arquivos JSON locais utilizados
para demonstracao e testes. Nao representam
integracoes com plataformas corporativas.

## Componentes desenvolvidos

- Quatro motores Python independentes.
- Biblioteca compartilhada poc_shared.py.
- Regras candidatas por hipotese.
- Fixtures com dados sinteticos.
- Processamento e classificacao de excecoes.
- Manifestos e hashes de entrada e codigo.
- Controle de reexecucao idempotente.
- Protecao contra sobrescrita divergente.
- Testes automatizados por POC.

## Estrutura principal

```text
README.md
poc_shared.py
docs/
dor_03/
    solucao_paliativa/
    solucao_definitiva/
    docs/
    poc/
dor_08/
    solucao_paliativa/
    solucao_definitiva/
    docs/
    poc/
dor_10/
    solucao_paliativa/
    solucao_definitiva/
    docs/
    poc/
dor_12/
    solucao_paliativa/
    solucao_definitiva/
    docs/
    poc/
```

Cada pasta poc/ possui motor.py, executar.py,
fixtures, testes e resultados locais ignorados
pelo controle de versao.

## Execucao das POCs

Executar a partir da raiz do repositorio:

```powershell
foreach ($Dor in @("03", "08", "10", "12")) {
    python ".\dor_$Dor\poc\executar.py"
}
```

## Testes automatizados

```powershell
foreach ($Dor in @("03", "08", "10", "12")) {
    python -m unittest discover `
        -s ".\dor_$Dor\poc\tests" `
        -p "test_*.py" -v
}
```

## Resultados da primeira validacao

| Indicador | Resultado |
|---|---|
| POCs executadas | 4 de 4 |
| Cenarios sinteticos | 29 de 29 |
| Testes automatizados | 12 de 12 |
| Auditoria de lotes | 4 de 4 |
| Escritas em sistemas corporativos | Nenhuma |

Os casos sinalizados sao simulacoes.
Nao comprovam erros em producao.

Na versao atual, CONCILIADO representa ausencia
de alertas nas regras candidatas executadas.
Nao equivale a homologacao de negocio.

## Situacao das solucoes

**Paliativas:**
Motores demonstrativos desenvolvidos e validados
com dados sinteticos.

**Definitivas:**
Arquiteturas-alvo documentadas, nao implantadas.

**Dados reais:**
Fontes, dicionarios, chaves, relacionamentos
e regras ainda precisam de confirmacao.

## Proxima fase - Investigacao com dados reais

1. Receber novos desenhos e evidencias.
2. Identificar fontes e responsaveis.
3. Mapear schemas, tabelas, views e campos.
4. Confirmar chaves e granularidade.
5. Levantar regras academicas e financeiras.
6. Mapear integracoes e processos existentes.
7. Analisar historico, ajustes e incrementalidade.
8. Atualizar contratos e testes das POCs.
9. Executar validacoes com extratos autorizados.
10. Homologar com negocio, financeiro e TI.

## Seguranca

- Proibido publicar dados pessoais de alunos.
- Nao versionar credenciais nem extratos sensiveis.
- Evidencias reais exigem armazenamento autorizado.
- Nenhum motor executa baixas ou estornos.
- Nenhum ressarcimento e realizado pela POC.
- Regras fiscais e regulatorias exigem homologacao.
- Integracoes reais dependem de autorizacao da TI.

## Responsabilidade de validacao

As demonstracoes tecnicas nao substituem
a aprovacao das areas de negocio, financeiro,
contabilidade, fiscal, academico e TI.

## Status final

**POCs v0.1: funcionais e auditadas.**

**Investigacao real: proxima fase.**

**Arquiteturas definitivas: propostas,
dependentes de evidencias e homologacao.**
