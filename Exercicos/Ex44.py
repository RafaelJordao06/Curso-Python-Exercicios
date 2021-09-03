'''
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
'''
preco = float(input('Digite o preço das compras: R$'))
print('FORMA DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista no cartão\n[ 3 ] em até 2x no cartão\n[ 4 ] 3x ou mais no cartão')
pagamento = int(input())
if pagamento == 1:
    nvpreco = preco - ((preco*10)/100)
    print('Valor a ser pago R$ {}'.format(nvpreco))
elif pagamento == 2:
    nvpreco = preco - ((preco*5)/100)
    print('Valor a se pago R$ {}'.format(nvpreco))
elif pagamento == 3:
    print('Valor a pagar {}'.format(preco))
elif pagamento == 4:
    parcelas = int(input('Quantas parcelas: '))
    print('Sua compra será parcelada em {}x de R${} COM JUROS!'.format(parcelas,(((preco*20)/100)+preco)/parcelas ))
    print('Sua compra de R${} será de R${}'.format(preco, (((preco*20)/100)+preco)))
else:
    print('Numero invalido!')