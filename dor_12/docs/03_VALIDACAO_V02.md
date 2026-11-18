# DOR 12 - Validacao do Projeto RT v0.2

## Direcionamento
Acompanhar projeto existente de saneamento
e prevencao de enderecos incorretos.

## Hipoteses
H12.1 - Enderecos legados.
H12.2 - Edicao manual apos preenchimento do CEP.
H12.3 - Uso do endereco do polo.

## Cenarios para homologacao
1. Endereco legado incompleto.
2. CEP divergente de cidade ou UF.
3. Alteracao de dados apos busca de CEP.
4. Cadastro com endereco coincidente com polo.
5. Atualizacao legitima com numero e complemento.
6. Monitoramento de regularizacao cadastral.

## Cuidados
CEP valido nao comprova residencia efetiva.
Endereco coincidente com polo exige revisao,
nao classificacao automatica como irregularidade.

## Evidencias necessarias
- Plano de saneamento do Projeto RT.
- Regras de validacao implementadas.
- Resultado de testes dos cadastros.
- Dashboard de acompanhamento.
- Indicadores antes e depois da correcao.

Status: acompanhamento e homologacao pendentes.
