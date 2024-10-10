r1 = float(input('Primeiro sigmento:'))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r3+ r1 and r3 < r1 + r2:
   print('E possivel formar um TRIANGULO')
else:
   print('Nao é possivel formar um triangulo')