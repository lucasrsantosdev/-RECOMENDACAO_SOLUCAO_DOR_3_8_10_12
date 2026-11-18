# Arquitetura e Governanca

## Objetivo
Construir quatro POCs independentes usando metodologia comum.

## Camadas
RAW: preservar capturas e proveniencia.
Bronze: padronizar formatos e tipos.
Silver: aplicar regras de negocio e historico.
Gold: publicar conciliacoes e indicadores validados.

As camadas serao implementadas progressivamente.

## Requisitos
- Dados sinteticos na fase inicial.
- Processamento idempotente.
- Controle de competencia e data de processamento.
- Inclusoes, alteracoes e exclusoes logicas.
- Tratamento de eventos retroativos.
- Auditoria das regras e resultados.
- Historico de execucoes e excecoes.
- Rejeicao ou quarentena de registros invalidos.
- Gate de qualidade antes da publicacao BI.
- Nenhuma alteracao automatica na origem nesta fase.

## Integracoes
Os sistemas reais, schemas, tabelas, colunas, chaves e
responsaveis ainda precisam de confirmacao pela TI.

## Seguranca
Nao publicar dados de alunos, relatorios reais,
credenciais ou capturas de ambientes corporativos.

A utilizacao futura de dados reais depende de
autorizacao, controles de acesso e minimizacao.

