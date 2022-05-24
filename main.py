# from casa_tabuleiro import *
# from funcoes import *

from partida import Partida
from simulacao import Simulacao

simulacao = Simulacao()

while simulacao.numero_simulacoes < 300:
    partida_atual = Partida()
    for i in range(1000):

        for jogador in partida_atual.ordem_lancamento_jogadores:
            if partida_atual.jogadores_falidos < 3:
                j = partida_atual.proximo_jogador()
                if j.saldo >= 0:
                    nova_posicao = j.joga_dado()
                    if partida_atual.casa_tabuleiro[nova_posicao].proprietario == "":
                        if partida_atual.casa_tabuleiro[nova_posicao].valor_imovel < j.saldo:
                            j.compra_imovel(partida_atual.casa_tabuleiro[nova_posicao])

                    else:
                        if partida_atual.casa_tabuleiro[nova_posicao].proprietario != j.__class__.__name__ :
                            j.saldo -= partida_atual.casa_tabuleiro[nova_posicao].valor_imovel
                            if j.saldo < 0:
                                partida_atual.jogadores_falidos += 1
                            



                

            else:
                break

            pass
            # print(i, " ", simulacao.numero_simulacoes, partida.proximo_jogador().__class__.__name__)
            # partida.proximo_jogador()



    
    else:
        # caso timeout
        simulacao.encerradas_timeout += 1
        # checar o vencedor


    simulacao.numero_simulacoes += 1






















# tabuleiro = init_tabuleiro()


#proximo_jogador = partida.proximo_jogador()











'''
print("face do dado", face_dado())


impulsivo = Jogador_impulsivo()
exigente = Jogador_exigente()
cauteloso = Jogador_cauteloso()
aleatrio = Jogador_aleatrio()
'''


