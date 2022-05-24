import random

from casa_tabuleiro import Casa_tabuleiro


# Inicia tabuleiros com valor e alugueis
def init_tabuleiro():
    casa_tabuleiro = []

    for i in range(20):
        valor_imovel = (i + 1) * 8
        casa_tabuleiro.append(Casa_tabuleiro(valor_imovel))
    return casa_tabuleiro


def face_dado():
    return random.randint(1, 6)
