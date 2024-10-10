#DA PRA CALCULAR A AREA MULTIPLICANDO A ALTURA PELA LARGURA
x = int(input('Qual a altura da sua parede em metos?: ')) 
y = int(input('Qual a largura da sua parede em metros?: '))
s = x*y
print('A area em metrosQ é de: {}m quadrados'.format(s))
print('serao necessario {} litros de tinta '.format(s/2))
