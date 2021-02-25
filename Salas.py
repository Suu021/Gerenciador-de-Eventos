from typing import Dict


class Sala:

    def __init__(self, nome, lotacao, participantes_etapa1, participantes_etapa2):
        self.nome = nome
        self.lotacao = lotacao
        self.participantes_etapa1 = participantes_etapa1
        self.participantes_etapa2 = participantes_etapa2

    def conversao_dicionario(self):
        sala: Dict[str, int, str, str] = {'Nome': self.nome, 'Lotação': self.lotacao, 'Participantes - etapa 1': self.participantes_etapa1, 'Participantes - etapa 2': self.participantes_etapa2}
        return sala