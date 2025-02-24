print('========LOJA DO MCP==========')
preço = float(input('Preço das compras: '))
pag = int(input('FORMAS DE PAGAMENTOS \n [ 1 ] á vista dinheiro \n [ 2 ] á vista cartão \n [ 3 ] 2x no cartão \n [ 4 ] 3x ou mais no cartão \n Quqal sua opção?:'))
if pag == 1:
    desconto = preço*10 / 100
    print('Sua compra de R${} vai custar R${} no final.'.format(preço, preço - desconto))
elif pag == 2:
    desconto = preço*3 / 100
    print('Sua compra de R${} vai custar R${} no final.'.format(preço, preço - desconto))
elif pag == 3:
    juros = preço*2 / 100
    print('Sua compra de R${} vai custar R${} com juros.'.format(preço, preço + juros))
elif pag == 4:
    vezes = int(input('Em quantas vezes vaidividir?'))
    porcentagem = preço*20 / 100
    total = preço + porcentagem
    parcela  = preço / vezes
    juros = total / vezes
    print('Sua compra de R${} parcelada em {}x  de {} vai custar R${} com juros'.format(preço, vezes, juros, total))