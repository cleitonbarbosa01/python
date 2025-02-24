from random import randint
itens = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)
print(''''Suas opções:
      [ 0 ] Pedra
      [ 1 ] Papel
      [ 2 ] tesoura''')
jogador = int(input('Qual sua jogada: '))
if computador == 0 and jogador == 1 or computador == 1 and jogador == 2 or computador == 2 and jogador == 0:
      print('Jogador venceu com {} e npc perdeu com {}'.format(itens[jogador], itens[computador]))
elif computador == 1 and jogador == 0 or computador == 2 and jogador == 1 or computador == 0 and jogador == 2:
      print('Jogador perdeu com {} e npc ganhou com {}'.format(itens[jogador], itens[computador]))
else:
      print('Empate')