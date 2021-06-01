'''
Crie um programa que leia um número inteiro e mostre tela se ele é par ou impar.
'''
num = int(input('Digite um número:'))
div = num % 2
if div == 0:
    print('Par')
else:
    print('Impar')