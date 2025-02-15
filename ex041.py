ano = int(input('Ano de nascimento:'))
idade = 2025 - ano
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL:')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SêNIOR')
else:
    print('Classificação: MASTER')