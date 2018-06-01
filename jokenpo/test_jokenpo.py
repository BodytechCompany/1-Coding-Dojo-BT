import unittest
from jokenpo import Jokenpo
    

class TestJokenpo(unittest.TestCase):
    def test_validar_primeira_entrada(self):
        jokenpo = Jokenpo()
        p1 = 'mamoa'
        p2 = 'pedra'
        retorno = jokenpo.efetua_jogada(p1,p2)

        self.assertEquals('Jogada 1 errada', retorno)

    def test_validar_segunda_entrada(self):
        jokenpo = Jokenpo()
        p1 = 'pedra'
        p2 = 'preda'
        retorno = jokenpo.efetua_jogada(p1,p2)

        self.assertEquals('Jogada 2 errada', retorno)

    def test_validar_primeira_entrada_vazia(self):
        jokenpo = Jokenpo()
        p1 = None
        p2 = 'pedra'
        retorno = jokenpo.efetua_jogada(p1,p2)

        self.assertEquals('Jogada 1 vazia', retorno)

    def test_validar_segunda_entrada_vazia(self):
        jokenpo = Jokenpo()
        p1 = 'papel'
        p2 = None
        retorno = jokenpo.efetua_jogada(p1,p2)

        self.assertEquals('Jogada 2 vazia', retorno)

    def test_valores_iguais(self):
        p1 = 'pedra'
        p2 = 'pedra'

        jokenpo = Jokenpo()
        retorno = jokenpo.efetua_jogada(p1,p2)

        self.assertEquals('Empatou!', retorno)

    def test_p1_pedra_p2_tesoura_p1_vencedor(self):
        p1 = 'pedra'
        p2 = 'tesoura'

        jokenpo = Jokenpo()
        retorno = jokenpo.efetua_jogada(p1,p2)

        self.assertEqual('Jogador 1 Vencedor', retorno)

    def test_p1_tesoura_p2_papel_p1_vencedor(self):
        p1 = 'tesoura'
        p2 = 'papel'

        jokenpo = Jokenpo()
        retorno = jokenpo.efetua_jogada(p1,p2)

        self.assertEqual('Jogador 1 Vencedor', retorno)

    def test_p1_papel_p2_pedra_p1_vencedor(self):
        p1 = 'papel'
        p2 = 'pedra'

        jokenpo = Jokenpo()
        retorno = jokenpo.efetua_jogada(p1,p2)

        self.assertEqual('Jogador 1 Vencedor', retorno) 
        
    def test_p2_pedra_p1_tesoura_p2_vencedor(self):
        p2 = 'pedra'
        p1 = 'tesoura'

        jokenpo = Jokenpo()
        retorno = jokenpo.efetua_jogada(p1,p2)

        self.assertEqual('Jogador 2 Vencedor', retorno)

    def test_p2_tesoura_p1_papel_p2_vencedor(self):
        p2 = 'tesoura'
        p1 = 'papel'

        jokenpo = Jokenpo()
        retorno = jokenpo.efetua_jogada(p1,p2)

        self.assertEqual('Jogador 2 Vencedor', retorno)


    def test_p2_papel_p1_pedra_p2_vencedor(self):
        p2 = 'papel'
        p1 = 'pedra'

        jokenpo = Jokenpo()
        retorno = jokenpo.efetua_jogada(p1,p2)

        self.assertEqual('Jogador 2 Vencedor', retorno)



    

