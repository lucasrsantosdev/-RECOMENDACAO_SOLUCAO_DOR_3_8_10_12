# POC 03 - Solucao Paliativa v0.1

## Nome
Motor de Conciliacao Academico-Financeira.

## Problema
Divergencias entre situacao academica, titulos,
bolsas, cancelamentos, estornos e faturamento.

## Hipoteses atendidas
H3.1, H3.2, H3.3 e H3.4.

## Proposta
Desenvolver um processo independente de conferencia
entre os registros academicos e financeiros.

O motor nao alterara os sistemas de origem.

## Funcionamento proposto
1. Importar extratos academicos e financeiros autorizados.
2. Padronizar chaves de aluno, matricula, contrato e titulo.
3. Relacionar eventos academicos com cobrancas.
4. Comparar competencia, valores, bolsa e situacao.
5. Identificar divergencias e classificar excecoes.
6. Gerar relatorio auditavel para as areas responsaveis.
7. Registrar analise, justificativa e resolucao.

## Regras prioritarias

### H3.1 - Cancelamento e cobranca
- Identificar eventos de cancelamento e trancamento.
- Detectar titulos posteriores ao evento.
- Comparar data efetiva e data de registro.
- Identificar estornos e seus motivos.
- Verificar baixa de alunos com bolsa integral.
- Investigar falhas de integracao do PROUNI.
- Investigar boletos incorretos do Studeo.
- Nao presumir cobranca indevida sem validar a regra.

### H3.2 - Pre-candidatos
- Identificar notas fiscais zeradas.
- Verificar vinculo com matricula e engajamento.
- Separar registros legitimos de possiveis erros.
- Exigir validacao da regra fiscal aplicavel.

### H3.3 - Identificacao do pagador
- Diferenciar aluno, polo e outros responsaveis.
- Verificar efeito do pagamento no engajamento.
- Coletar evidencias da correcao informada.

### H3.4 - Aproveitamento
- Detectar lancamentos duplicados.
- Comparar valores e versoes dos aproveitamentos.
- Identificar efeitos no faturamento.
- Encaminhar divergencias para revisao humana.

## Dados minimos propostos
- Instituicao e sistema de origem.
- Identificadores tecnicos de aluno e matricula.
- Contrato, periodo, titulo e parcela.
- Situacao academica e evento ocorrido.
- Data efetiva e data do registro.
- Valor original, descontos, bolsa e saldo.
- Responsavel pelo pagamento.
- Tipo e motivo do ajuste.
- Competencia financeira.
- Identificador da execucao e fonte.

## Entregaveis
- Base sintetica de eventos e titulos.
- Motor de regras em Python.
- Relatorio de excecoes.
- Matriz de conciliacao.
- Evidencias de testes.
- Resumo dos indicadores para BI.

## Limites
- Somente leitura.
- Nenhuma baixa ou estorno automatico.
- Nenhuma conclusao fiscal sem homologacao.
- Dados reais somente com autorizacao.

## Criterios de aceite da POC
- Detectar os casos sinteticos planejados.
- Nao sinalizar como erro os casos validos.
- Preservar data efetiva e data de processamento.
- Reexecutar lotes sem duplicar resultados.
- Gerar rastreabilidade para cada divergencia.

Status: proposta tecnica, nao implementada.
