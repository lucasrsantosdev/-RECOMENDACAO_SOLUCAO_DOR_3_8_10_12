
# FOURD VITRU - POC 08

## Dominio
Validacao de Controles NDD

## Implementado
- Motor de regras candidatas em Python.
- Dados de entrada exclusivamente sinteticos.
- Captura RAW com hash de integridade.
- Bronze com identificacao de lote.
- Silver com classificacao por hipotese.
- Gold com indicadores e contagens.
- Manifesto com hashes de entrada e motor.
- Reexecucao idempotente.
- Protecao contra alteracao dos resultados gravados.
- Testes automatizados.

## Execucao
python .\dor_08\poc\executar.py

## Testes
python -m unittest discover -s .\dor_08\poc\tests -v

## Limites
Esta POC nao acessa sistemas corporativos.
Nao valida conformidade regulatoria ou fiscal.
Nao executa baixas, estornos ou ressarcimentos.
Nao comprova que os erros sinteticos existem na origem.

## Evolucao
Consultar as propostas de solucao paliativa e
definitiva existentes no repositorio.

As regras reais dependem de evidencias, dicionarios
de dados, autorizacoes e homologacao.
