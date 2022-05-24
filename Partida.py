import random

from casa_tabuleiro import Casa_tabuleiro
from funcoes import init_tabuleiro
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
        self.casa_tabuleiro = init_tabuleiro()


    def proximo_jogador(self):
        if self.ultimo_jogador == 3:
            self.ultimo_jogador = 0
        else:
            self.ultimo_jogador += 1
        proximo_jogador_jogar = self.ordem_lancamento_jogadores[self.ultimo_jogador]
        return proximo_jogador_jogar


    # Inicia tabuleiros com valor e alugueis
    def init_tabuleiro():
        tabuleiro = []

        for i in range(20):
            valor_imovel = (i + 1) * 8
            tabuleiro.append(Casa_tabuleiro(valor_imovel))
        return tabuleiro

    
    def vencedor(self):
        saldos = []
        for jogador in self.ordem_lancamento_jogadores:
            if jogador.saldo >= 0:
                saldos.append(jogador.saldo)
                
        tmp = max(saldos)
        indice = self.ordem_lancamento_jogadores.index(tmp)                
        return self.ordem_lancamento_jogadores[indice]
