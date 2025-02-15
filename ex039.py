ano = int(input('Ano de nascimento:'))
ano_atual = 2025
idade = ano_atual - ano
if ano > 18:
    print('''Quem nasceu em {} tem {} anos em {}.
          você ja deveria estar alistado!!'''.format(ano, idade, ano_atual))
elif ano == 18:
    print('''Quem nasceu em {} tem {} anos em {}.
          você ja pode se alistar'''.format(ano, idade, ano_atual))
else:
    print('''Quem nasceu em {} tem {} anos em {}.
          ainda faltam { } anos para o alistamento'''.format(ano, idade, ano_atual) )