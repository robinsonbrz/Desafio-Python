

# Desafio Python


## Banco Imobiliário

Execução do programa

```console
python main.py
```




<br>
<br>

## Descrição do programa e classes
_______________________

## Arquivo principal main.py
Arquivo onde o fluxo da execução e o controle principal dos loops foi desenvolvido

<br>

## Classe Simulação no arquivo simulacao.py
Esta classe é inicializada apenas uma vez por simulação e acumula os dados das simulações, e também faz a exibição do relatório final.

O objeto simulação intanciado acumula quantidades de rodadas antes do fim das partidas, vencedores, para depois calcular e exibir vencedores e os valores acumulados.

<br>

## Classe Casa_tabuleiro no arquivo casa_tabuleiro.py
Cada objeto representa uma casa do tabuleiro com seus valores e proprietários.

Uma lista de casas será criada na classe Partida, descrita abaixo. 

<br>

## Classe Partida no arquivo partida.py
A classe partida inicia o tabuleiro a cada partida da simulação, com valores das propriedades, dos alugueis e os proprietários.

Também sorteia a ordem de lançamento de dados dos jogadores a cada partida.

Métodos importantes também foram iseridos, como:

Recebimento do aluguel caso alguém caia numa propriedade com um outro dono.

Retorna do vencedor da partida quando uma partida termina.

Também inicializa uma lista de objetos do tipo Casa_tabuleiro, que representa cada propriedade, com seus valores e proprietários da rodada.

<br>

## Classe Jogador no arquivo jogador.py
O objeto dessa classe armazenará o saldo de cada jogador, sua posição no tabuleiro.

Também existem diferentes tipos de classes jogadores com os diferentes tipos de comportamento de compra.








23/05/2022
Robinson Enedino e Silva
