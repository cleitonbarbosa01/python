v = int(input('Qual a velocidade do seu carro?: '))
m = v - 80
if m > 0:
   print('Voce foi multado em {}'.format(m*7))
else:
   print('Tenha uma boa viagem arrombado')