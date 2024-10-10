s = float(input('Informe seu salario: '))
r1 = s*15/100
r2 = s*10/100
if s<=1250.0:
   print('Seu novo salario será: {}'.format(r1+s))
else:
   print('Seu novo salario será: {}'.format(r2+s))
   