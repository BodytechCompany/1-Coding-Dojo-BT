import unittest
from numero import Numero

class TesteNumero(unittest.TestCase):

    #Se o numero é par
    def teste_verifica_numero_par(self):
        numero = Numero()
        retorno = numero.verifica_numero(990000)

        self.assertEqual("Par", retorno)

    #se o numero é impar
    def teste_verifica_numero_impar(self):
        numero = Numero()
        retorno = numero.verifica_numero(55)

        self.assertEqual("Impar", retorno)