'''
Crie um programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 a 50
'''
n = int
for c in range(1,51):
    n = (c%2)
    if n == 0:
        print(c)
