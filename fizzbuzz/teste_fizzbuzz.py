import unittest
from Fizzbuzz import Fizzbuzz

class TesteFizzbuzz(unittest.TestCase):

    def teste_verificar_tamanho_lista(self):
        fizzbuzz = Fizzbuzz()
        retorno = fizzbuzz.lista_numero
        self.assertEqual(100,len(retorno))

    def teste_verificar_fizz(self):
        fizzbuzz = Fizzbuzz()
        retorno=fizzbuzz.verifica_numero(3)
        self.assertEqual("Fizz",retorno)
        
    def teste_verificar_buzz(self):
        fizzbuzz = Fizzbuzz()
        retorno=fizzbuzz.verifica_numero(5)
        self.assertEqual("Buzz",retorno)

    def teste_verificar_fizzbuzz(self):
        fizzbuzz = Fizzbuzz()
        retorno=fizzbuzz.verifica_numero(15)
        self.assertEqual("FizzBuzz",retorno)

    def teste_verificar_not_fizz_or_buzz(self):
        fizzbuzz = Fizzbuzz()
        numero_nao_divisivel_por_cinco_e_tres = 11
        retorno=fizzbuzz.verifica_numero(numero_nao_divisivel_por_cinco_e_tres)
        self.assertEqual(numero_nao_divisivel_por_cinco_e_tres,retorno)
        
    def teste_verificar_se_numero(self):        
        fizzbuzz = Fizzbuzz()
        retorno = fizzbuzz.verifica_numero("ABC")
        self.assertEqual("Não é um número", retorno)

