nota1 = float(input('Digite a primeria nota:'))
nota2 = float(input('Digite a segunda nota:'))
média = (nota1 + nota2)/2
if média >= 6:
    print('Parabéns, você foi aprovado com a média {}'.format(média))
else:
    print('Infelizmente foi reprovado com a média {}'.format(média))