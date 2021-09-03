'''
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escrever qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal
'''

numero = int(input('Digite o numero: '))
print('Escolha uma das bases para conversão:\n[ 1 ] para binário\n[ 2 ] para octal\n[ 3 ] para hexadecimal')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero,bin(numero)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(numero,oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero,hex(numero)[2:]))
else:
    print('{} Invalido!'.format(numero))