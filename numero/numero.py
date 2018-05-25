class Numero():

    def verifica_numero(self, numero):
        resultado = numero%2

        if resultado == 0 :
            return "Par"
        else:
            return "Impar"