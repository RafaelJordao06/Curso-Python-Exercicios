'''
Faça um programa que leia 3 números e mostre qual é o maior e o menor.
'''
num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
num3 = int(input('Digite o terceiro numero: '))
if num1 > num2:
    if num1 > num3:
        print('{} maior'.format(num1))
    else:
        print('{} Maior'.format(num3))
else:
    if num2 > num3:
        print('{} Maior'.format(num2))
    else:
        print('{} Maior'.format(num3))
if num1 < num2:
    if num1 < num3:
        print('{} Menor'.format(num1))
    else:
        print('{} Menor'.format(num3))
else:
    if num2 < num3:
        print('{} Menor'.format(num2))
    else:
        print('{} Menor'.format(num3))