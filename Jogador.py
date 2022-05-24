import random


class Jogador:
    def __init__(self):
        self.saldo = 300
        self.posicao_no_tabuleiro = 0


    def joga_dado(self):
        posicao_nova = 0
        face_dado = random.randint(1, 6)
        posicao_nova = self.posicao_no_tabuleiro + face_dado
        if posicao_nova > 19:
            posicao_nova -= 20
            self.saldo += 100
        self.posicao_no_tabuleiro = posicao_nova
        return posicao_nova


class Jogador_impulsivo(Jogador):
    def compra_imovel(self, casa_tabuleiro):
        casa_tabuleiro.propietario = self.__class__.__name__
        self.saldo -= casa_tabuleiro.valor_imovel
        return


class Jogador_exigente(Jogador):
    def compra_imovel(self, casa_tabuleiro):
        # compra qualquer propriedade com valor de aluguel maior do que 50
        # se compra subtrai valor movel do saldo
        if casa_tabuleiro.valor_aluguel > 50:
            casa_tabuleiro.propietario = self.__class__.__name__
            self.saldo -= casa_tabuleiro.valor_imovel
        return


class Jogador_cauteloso(Jogador):
    def compra_imovel(self, casa_tabuleiro):
        # compra qualquer imovel mas deve lhe sobrar 80 de saldo na transação
        if (self.saldo - casa_tabuleiro.valor_imovel) >= 80:
            casa_tabuleiro.propietario = self.__class__.__name__
            self.saldo -= casa_tabuleiro.valor_imovel
        return


class Jogador_aleatorio(Jogador):
    def compra_imovel(self, casa_tabuleiro):
        # Comprador aleatório, com 50% de chance de comprar
        compra = random.randint(1, 2)
        if compra == 1:
            casa_tabuleiro.propietario = self.__class__.__name__
            self.saldo -= casa_tabuleiro.valor_imovel
        return




