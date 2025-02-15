num = int(input('Me informe um número qualquer: '))
print('[1] converter para Binário')
print('[2] converter para Octal')
print('[3] converter para Hexadecimal')
op = int(input('Escolha uma dessas opcoes: '))
if op==1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)))
elif op==2:
    print('{} convertido pra Octal é {}'.format(num, oct(num)))
elif op==3:
    print('{} convertidod para Hexadecimal é {}'.format(num, hex(num)))
else:
    print('Opção inválida, tente novamente!!')
    for
    