import random

from casa_tabuleiro import Casa_tabuleiro
from jogador import (Jogador_aleatorio, Jogador_cauteloso, Jogador_exigente,
                     Jogador_impulsivo)


class Partida:
    def __init__(self):
        self.rodada = 0
        self.ultimo_jogador = 3
        self.jogadores_falidos = 0
        self.lista_jogadores = [
            Jogador_impulsivo(),
            Jogador_exigente(),
            Jogador_cauteloso(),
            Jogador_aleatorio()
        ]
        random.shuffle(self.lista_jogadores)
        self.ordem_lancamento_jogadores = self.lista_jogadores
        self.casa_tabuleiro = self.init_tabuleiro()


    def proximo_jogador(self):
        if self.ultimo_jogador == 3:
            self.ultimo_jogador = 0
        else:
            self.ultimo_jogador += 1
        proximo_jogador_jogar = self.ordem_lancamento_jogadores[self.ultimo_jogador]
        return proximo_jogador_jogar


    def paga_proprietario(self, casa):
        for jog in self.lista_jogadores:
            jog.saldo = jog.saldo
            if jog.__class__.__name__ == casa.proprietario:
                jog.saldo += casa.valor_aluguel
        return


    # Inicia tabuleiros com valor e alugueis
    def init_tabuleiro(self):
        tabuleiro = []

        for i in range(20):
            valor_imovel = (i + 1) * 8
            tabuleiro.append(Casa_tabuleiro(valor_imovel))
        return tabuleiro

    
    def vencedor(self):
        saldos = []
        ganhador = []
        for jogador in self.ordem_lancamento_jogadores:
            if jogador.saldo >= 0:
                saldos.append(jogador.saldo)
                
        tmp = max(saldos)

        for jogador in self.ordem_lancamento_jogadores:
            if jogador.saldo == tmp:
                ganhador.append(jogador.__class__.__name__)

        # retorna o maior em caso de empate o primeiro da lista que seria o próximo a jogar
        return ganhador[0]

    
    def reseta_propriedades_de_perdedor(self, jogador):
        for casa in self.casa_tabuleiro:
            if casa.proprietario == jogador.__class__.__name__ :
                casa.proprietario = ""
        return
