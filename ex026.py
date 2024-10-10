frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira posiçao da letra A na frase é {}'.format(frase.find('A')+1))
print('A última posiçao da letra A na frase é {}'.format(frase.rfind('A')+1))
