# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteora. Ex: Digite um numero: 6.127 tem a parte inteira 6.
from math import trunc
num = float(input('Digite um numero: '))
print('O numero {} tem a parte inteira {}'.format(num,trunc(num)))