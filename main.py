# from casa_tabuleiro import *
# from funcoes import *

from partida import Partida
from simulacao import Simulacao

simulacao = Simulacao()

while simulacao.numero_simulacoes < 300:
    partida_atual = Partida()
    for i in range(1000):

        for jogador in partida_atual.ordem_lancamento_jogadores:
            
                j = partida_atual.proximo_jogador()
                if j.saldo >= 0:
                    nova_posicao = j.joga_dado()
                    # se a casa em que caiu nao possui proprietario
                    if partida_atual.casa_tabuleiro[nova_posicao].proprietario == "":
                        # se possui saldo para a compra
                        if partida_atual.casa_tabuleiro[nova_posicao].valor_imovel < j.saldo:
                            j.compra_imovel(partida_atual.casa_tabuleiro[nova_posicao])
                    
                    # esta casa possui proprietario
                    else:
                        # esse jogador nao é proprietário da casa entao deve pagar
                        if partida_atual.casa_tabuleiro[nova_posicao].proprietario != j.__class__.__name__ :
                            j.saldo -= partida_atual.casa_tabuleiro[nova_posicao].valor_imovel
                            if j.saldo < 0:
                                partida_atual.jogadores_falidos += 1
                                # se houverem 3  falidos existe um vencedor
                                if partida_atual.jogadores_falidos > 2:
                                    # houve vencedor
                                    simulacao.vitoriosos.append(j.vencedor())

                            



                

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


