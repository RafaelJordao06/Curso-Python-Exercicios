#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço. com 5% de descontos.
preco = float(input('Digite o preco do produto: '))
nv = (preco * 5)/100
nvpreco = preco - nv

print('Novo preco com desconto: {:.2f}'.format(nvpreco))