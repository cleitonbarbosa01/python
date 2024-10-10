import random
num = random.randint(0, 5)
resp = int(input('Qual sera o numero que a IA escolheu?: '))
if num == resp:
   print('Voce acertou o numero, PARABEN!!!')
else:
   print('Voce errou, tente novamente!!!')
