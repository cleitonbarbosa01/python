km = int(input('Qual  a distancia da viagem que voce vai?: '))
if km <= 200:
   print('O valor da sua passagem é {}'.format(km*0.50))
else:
   print('O valor da sua passagem vai custar {} por que a viagem é maior que 200km'.format(km*0.45))