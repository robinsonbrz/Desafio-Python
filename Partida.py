import random

from jogador import (Jogador_aleatorio, Jogador_cauteloso, Jogador_exigente,
                     Jogador_impulsivo)


class Partida:
    def __init__(self):
        self.rodada = 0
        self.ultimo_jogador = 3
        self.jogadores_falidos = 0
        lista_jogadores = [
            Jogador_impulsivo(),
            Jogador_exigente(),
            Jogador_cauteloso(),
            Jogador_aleatorio()
        ]
        random.shuffle(lista_jogadores)
        self.ordem_lancamento_jogadores = lista_jogadores


    def proximo_jogador(self):
        if self.ultimo_jogador == 3:
            self.ultimo_jogador = 0
        else:
            self.ultimo_jogador += 1
        proximo_jogador_jogar = self.ordem_lancamento_jogadores[self.ultimo_jogador]
        return proximo_jogador_jogar
