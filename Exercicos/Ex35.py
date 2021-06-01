'''
Desenvolva um programa que leia o comprimento de 3 retas e diga ao úsuario se elas podem ou não formar um triangulo.
'''
lado1 = int(input('Digite o lado 1: '))
lado2 = int(input('Digite o lado 2: '))
lado3 = int(input('Digite o lado 3: '))

if ((lado1 + lado2) > lado3) and ((lado2 + lado3) > lado1) and ((lado1 + lado3) > lado2):
    print('Forma um triangulo!')
else:
    print('Não forma um triangulo!')