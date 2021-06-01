'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 a 5 e peça para o úsuario tentar
descobrir qual número escolhido pelo computador.
O programa devera escrever na tela se o usuario venceu ou perdeu
'''
from random import randrange

numSort = randrange(0,5)
num = int(input('Digite um numero de 0 a 5: '))
if numSort == num:
    print('Numeros iguais!')
else:
    print('Numeros diferentes!')
print('Numero sorteado {}'.format(numSort))