'''
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas
ainda não atingiram a maioridade e quantas já são maiores.
'''
from datetime import datetime
now = datetime.now()
maior = 0
menor = 0
anoAtual = (now.year)
for c in range (1, 8):
    ano = int(input('Em que ano a {}° pessoa nasceu? '.format(c)))
    if (anoAtual - ano) > 18:
        maior += 1
    else:
        menor +=1
print('\nAo todo tivemos {} pessoas maiores de idade\nE também tivemos {} pessoas menores de idade'.format(maior,menor))