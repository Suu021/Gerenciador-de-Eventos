import unittest
from Gerenciador import salvar_dados, carregar_dados, formatar_nome

class MyTestCase(unittest.TestCase):
    def test_carregar_dados(self):
        self.assertEqual(carregar_dados("Dados dos Participantes.json"), list)
        self.assertEqual(carregar_dados("Dados das salas de evento.json"), list)
        self.assertEqual(carregar_dados("Dados das salas de café.json"), list)

    def test_salvar_dados(self):
        self.assertEqual(salvar_dados("Dados dos Participantes.json"), list)
        self.assertEqual(salvar_dados("Dados das salas de evento.json"), list)
        self.assertEqual(salvar_dados("Dados das salas de café.json"), list)

    def test_formatar_nome(self):
        self.assertEqual(formatar_nome("CAIO LUAN DOS ANJOS"), "Caio Luan dos Anjos")
        self.assertEqual(formatar_nome("DiNo Da sIlVa sAuRo"), "Dino da Silva Sauro")
        self.assertEqual(formatar_nome("  erwin smith    "), "Erwin Smith")



if __name__ == '__main__':
    unittest.main()
