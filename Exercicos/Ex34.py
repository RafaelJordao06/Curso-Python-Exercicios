'''
Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
Para salarios superiores a R$1.200, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''
salario = float(input('Digite o salario: '))
s10 = (salario * 10)/100
s15 = (salario * 15)/100
if salario <= 1200:
    print('Salario com aumento: R${}'.format(salario + s15))
else:
    print('Salario com aumento: R${}'.format(salario + s10))