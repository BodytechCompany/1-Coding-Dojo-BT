class Jokenpo():

        
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
            return 'Jogador 1 Vencedor'

        elif p1 == 'tesoura' and p2 =='papel':
            return 'Jogador 1 Vencedor'

        elif p1 == 'papel' and p2 =='pedra':
            return 'Jogador 1 Vencedor'

        elif p1 == 'tesoura' and p2 =='pedra':
            return 'Jogador 2 Vencedor'

        elif p1 == 'papel' and p2 =='tesoura':
            return 'Jogador 2 Vencedor'

        elif p1 == 'pedra' and p2 =='papel':
            return 'Jogador 2 Vencedor'

 
    



        