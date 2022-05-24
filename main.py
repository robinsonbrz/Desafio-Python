# from casa_tabuleiro import *
# from funcoes import *

from ast import Break

from partida import Partida
from simulacao import Simulacao

simulacao = Simulacao()

while simulacao.numero_simulacoes < 300:
    partida_atual = Partida()
    flag_vencedor = False
    for rodada in range(1000):
        if flag_vencedor == True:
            break
        # print("\nRodada: ",rodada,"Simulacao: ",simulacao.numero_simulacoes)
        for jogador in partida_atual.ordem_lancamento_jogadores:
            j = partida_atual.proximo_jogador()
            # print(j.__class__.__name__, " saldo: ", j.saldo)
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
                        j.saldo -= partida_atual.casa_tabuleiro[nova_posicao].valor_aluguel
                        # adicionar valor ao proprietário
                        # print(j.__class__.__name__, " pagou aluguel ", j.saldo, "aluguel ", partida_atual.casa_tabuleiro[nova_posicao].valor_aluguel)
                        if j.saldo < 0:
                            partida_atual.jogadores_falidos += 1
                            partida_atual.reseta_propriedades_de_perdedor(j)
                            # se houverem 3  falidos existe um vencedor
                            if partida_atual.jogadores_falidos > 2:
                                # houve vencedor
                                simulacao.vitoriosos.append(partida_atual.vencedor())
                                simulacao.rodadas_partida.append(rodada)
                                
                                flag_vencedor = True
                                break

    
    else:
        # caso timeout
        simulacao.encerradas_timeout += 1
        # checar o vencedor
        simulacao.vitoriosos.append(partida_atual.vencedor())

    simulacao.numero_simulacoes += 1
# print(simulacao.numero_simulacoes)
print(simulacao)






















# tabuleiro = init_tabuleiro()


#proximo_jogador = partida.proximo_jogador()











'''
print("face do dado", face_dado())


impulsivo = Jogador_impulsivo()
exigente = Jogador_exigente()
cauteloso = Jogador_cauteloso()
aleatrio = Jogador_aleatrio()
'''


