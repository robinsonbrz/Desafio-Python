import random


class Partida:
    def __init__(self):
        self.rodada = 0
        lista_jogadores = [0, 1, 2, 3]
        random.shuffle(lista_jogadores)
        self.ordem_lancamento_jogadores = lista_jogadores
        self.ultimo_jogador = 3

    def proximo_jogador(self):
        if self.ultimo_jogador == 3:
            self.ultimo_jogador = 0
        else:
            self.ultimo_jogador += 1
        proximo_jogador_jogar = self.ordem_lancamento_jogadores[self.ultimo_jogador]
        return proximo_jogador_jogar
