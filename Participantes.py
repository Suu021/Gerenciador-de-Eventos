class Participante:

    def __init__(self, nome, sobrenome, sala_etapa1, sala_etapa2, sala_cafe_I1, sala_cafe_I2):
        self.nome = nome
        self.sobrenome = sobrenome
        self.nome_completo = self.nome + " " + self.sobrenome
        self.sala_etapa1 = sala_etapa1
        self.sala_etapa2 = sala_etapa2
        self.sala_cafe_I1 = sala_cafe_I1
        self.sala_cafe_I2 = sala_cafe_I2

    def conversao_dicionario(self):
        dic_p = {'Nome completo': self.nome_completo, 'Nome': self.nome, 'Sobrenome': self.sobrenome,
                 'Sala_etapa1': self.sala_etapa1, 'Sala_etapa2': self.sala_etapa2, 'Café_intervalo1':
                     self.sala_cafe_I1, "Café_intervalo2": self.sala_cafe_I2}
        return dic_p
