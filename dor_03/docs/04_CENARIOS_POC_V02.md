# DOR 03 - Cenarios da POC v0.2

Todos os dados serao sinteticos.

| Caso | Cenario | Resultado esperado |
|---|---|---|
| CT03-01 | Cancelamento com titulo posterior | Sinalizar para revisao |
| CT03-02 | Trancamento com cobranca posterior | Solicitar validacao da regra |
| CT03-03 | Bolsa integral com saldo divergente | Identificar inconsistencia candidata |
| CT03-04 | Estorno registrado como cancelamento | Sinalizar classificacao |
| CT03-05 | Pagamento do polo como engajamento | Identificar origem do pagador |
| CT03-06 | Pre-candidato com nota zerada | Encaminhar para validacao fiscal |
| CT03-07 | Aproveitamento duplicado | Detectar possivel duplicidade |
| CT03-08 | Disciplina removida sem recalculo | Sinalizar divergencia |
| CT03-09 | Tombamento com valor diferente | Comparar valores e vigencias |
| CT03-10 | Financeiro publicado sem conferencia | Sinalizar falha de controle |
| CT03-11 | Correcao retroativa | Preservar ambas as datas |
| CT03-12 | Reprocessamento de lote | Nao duplicar resultados |

## Estados de saida sugeridos
CONCILIADO
DIVERGENCIA_CANDIDATA
PENDENTE_REGRA
PENDENTE_EVIDENCIA

## Testes transversais
- Idempotencia.
- Unicidade de chaves.
- Integridade referencial.
- Reconstrucao temporal.
- Rastreabilidade de cada alerta.
- Separacao das regras por instituicao.

## Gate
Nenhum resultado da POC autoriza automaticamente
correcao de titulos ou contabilizacao.
