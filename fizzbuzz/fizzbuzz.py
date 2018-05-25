class Fizzbuzz():
    def __init__(self):
        self.lista_numero = range(1,101)

    def verifica_numero(self,numero):
        if not isinstance(numero,int):
            return "Não é um número"
        elif (numero % 3 == 0 and numero % 5 == 0):
            return "FizzBuzz"
        elif (numero % 3 == 0):
            return "Fizz"
        elif (numero % 5 == 0):
            return "Buzz"
        else:
            return numero
    
    def imprimir_lista(self):
        for i in self.lista_numero:
           print(self.verifica_numero(i))

if __name__ == "__main__":
    f = Fizzbuzz()
    f.imprimir_lista()
        
