class Simulacao:
    def __init__(self):
        self.numero_simulacoes = 0
        self.encerradas_timeout = 0
        self.rodadas_partida = []
        self.vitoriosos = []


    def __str__(self):
        # quantidade_de_partidas encerradas por timeout
        # média de roddadas das partidas
        # percentagem de vitórias por comportamento de jogadores
        # comportamento que mais venceu
        comportamentos = set(self.vitoriosos)

        nome = []
        valor = []
        percentual = []
        maior = 0

        media = round(self.media_rodadas(),2)
        saida = f"\n\n\nPartidas finalizadas por timeout: {self.encerradas_timeout}\nMédia de rodadas para o fim de partida: {media}\n\n"


        for comportamento in comportamentos:
            nome.append(comportamento)
            valor.append(self.vitoriosos.count(comportamento))
            percent = round((self.vitoriosos.count(comportamento)/300)*100,2)
            percentual.append(percent)
            saida += f"Quantidade de vitórias de {comportamento}: {self.vitoriosos.count(comportamento)} que representou {percent}%  de vitórias\n"
            saida += f"Percentual de vitórias de {comportamento}: {percent}\n\n"
            
        maior = max(valor)
        index = valor.index(maior)
        nome_maior = nome[index]

        saida += f"Comportamento com maior vitórias: {nome_maior}\n_________________________________________________________"
        return saida


    def media_rodadas(self):
        return sum(self.rodadas_partida)/len(self.rodadas_partida)

