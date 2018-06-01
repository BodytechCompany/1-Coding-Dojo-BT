class Jokenpo():

    def __init__(self):
        self.p1_winner = "Jogador 1 Vencedor"
        self.p2_winner = "Jogador 2 Vencedor"

        
    def efetua_jogada(self,p1,p2):

        if p2 is None:
            return 'Jogada 2 vazia'

        elif p1 is None:
            return 'Jogada 1 vazia'
        

        p1 = p1.lower()
        p2 = p2.lower()

        if p1 not in ['pedra','papel','tesoura']:
            return 'Jogada 1 errada'
        
        elif p2 not in ['pedra','papel','tesoura']:
            return 'Jogada 2 errada'
            
        elif p1 == p2:
            return 'Empatou!'

        elif p1 == 'pedra' and p2 =='tesoura':
            return self.p1_winner

        elif p1 == 'tesoura' and p2 =='papel':
            return self.p1_winner

        elif p1 == 'papel' and p2 =='pedra':
            return self.p1_winner

        elif p1 == 'tesoura' and p2 =='pedra':
            return self.p2_winner

        elif p1 == 'papel' and p2 =='tesoura':
            return self.p2_winner

        elif p1 == 'pedra' and p2 =='papel':
            return self.p2_winner    


if __name__=="__main__":
    p1 = input("Jogador 1:")
    p2 = input("Jogador 2:")

    j = Jokenpo()
    print(j.efetua_jogada(p1,p2))