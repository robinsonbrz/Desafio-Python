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

        status_comportamentos = {}
        for comportamento in comportamentos:
            status_comportamentos[comportamento] = self.vitoriosos.count(comportamento), round((self.vitoriosos.count(comportamento)/300)*100,2)


        media = self.media_rodadas()
        saida = f"Partidas finalizadas por timeout: {self.encerradas_timeout}\n Média de rodadas: {media} \n   {status_comportamentos}   "

        return saida

    def media_rodadas(self):

        return sum(self.rodadas_partida)/len(self.rodadas_partida)

