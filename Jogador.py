class Jogador:
    def __init__(self):
        self.saldo = 300
        self.numero_vitorias = 0


class Jogador_impulsivo(Jogador):
    def compra_imovel(self):
        # verificar se o saldo é suficiente
        self.saldo -= 5
        return True


class Jogador_exigente(Jogador):
    def compra_imovel(self):
        # verificar se o saldo é suficiente
        # compra qualquer propriedade com valor de aluguel maior do que 50
        # se compra subtrai valor movel do saldo
        self.saldo -= 10
        return


class Jogador_cauteloso(Jogador):
    def compra_imovel(self):
        # compra qualquer imovel mas deve lhe sobrar 80 de saldo na transação
        self.saldo -= 15
        return


class Jogador_aleatorio(Jogador):
    def compra_imovel(self):
        self.saldo -= 20
        return
        # verificar se o saldo é suficiente
        # Comprador aleatório, com 50% de chance de comprar
