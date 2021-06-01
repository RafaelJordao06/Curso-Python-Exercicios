'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em
seguida o primeiro e o último nome separadamente.
Ex: And Maria de Souza
Primeiro = Ana
último = Souza
'''
nome = str(input('Digite seu nome: ')).strip()
divisao = nome.split()
print(divisao[0])
print(divisao[len(divisao)-1])