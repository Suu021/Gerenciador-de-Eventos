class Cafe:

    def __init__(self, nome, lotacao, participantes_I1, participantes_I2):
        self.nome = nome
        self.lotacao = lotacao
        self.participantes_I1 = participantes_I1
        self.participantes_I2 = participantes_I2

    def conversao_dicionario(self):
        cafes = {'Nome': self.nome, 'Lotação': self.lotacao, 'Participantes_intervalo1': self.participantes_I1,
                 "Participantes_intervalo2": self.participantes_I2}
        return cafes