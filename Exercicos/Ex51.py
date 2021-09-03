'''
Desenvolva um programa que leia o primeiro termo e a razão de um P.A. No final, mostre os 10 primeiros termos dessa progressão.
'''
PT = int(input('Digite o primeiro termo: '))
Razao = int(input('Digite a razao: '))
n = PT + (10 - 1)* Razao
for c in range(PT, n+Razao, Razao):
    print(c)
print('ACABOU')