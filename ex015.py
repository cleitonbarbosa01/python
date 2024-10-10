a = float(input('Quantos dias alugados?: '))
b = float(input('Quantos Km rodados?: '))
d = 60*a
km = 0.15*b
print('O total a pagar é de: R${:.2f}'.format(d+km))