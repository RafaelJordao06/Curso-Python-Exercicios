'''
Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um segundo numero:'))
if num1 > num2:
    print('O primeiro valor é mairo {} > {}'.format(num1,num2))
elif num2 > num1:
    print('O segundo valor é maior {} > {}'.format(num2,num1))
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais {} = {}'.format(num1,num2))