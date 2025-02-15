casa = float(input('Qual é o valor da casa?: '))
sal = float(input('Qual seu salário?: '))
x = int(input('Em quantos anos vai pagar?: '))
prestacao = casa / (x * 12)
min = sal * 30 / 100
if prestacao <= min:
    print('para pagar uma casa de R${:.2f} em {} anos '.format(casa, x), end='')
    print('a prestação será de R$ {:.2f} foi APROVADO!!'.format(prestacao))
else:
    print('O valor da prestação ultrapassa os 30% do seu salário, a compra foi NEGADA!!')