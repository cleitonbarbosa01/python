num1 = int(input('Digite o primeiro sigmento: '))
num2 = int(input('Digite o segundo sigmento: '))
num3 = int(input('Digite o terceiro sigmento: '))
if num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2:
    print('É possivel formar um triângulo ', end='')
    if num1 == num2 and num2 == num3:
        print('EQUILÁTERO')
    if num1 != num2 and num2 != num3 and num3 != num1:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('Não é possivel formar um triângulo')