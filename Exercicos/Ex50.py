'''
Desenvolva um programa que leia seis números inteiros e mostre a soma daqueles que foram pares. Se o valor digitado for
impar, desconsidere-o.
'''
resto = int
n2 = int
n2 = 0
for c in range(1,7):
    n = int(input('Digite o {} numero: '.format(c)))
    resto = (n%2)
    if resto == 0:
        n2 = n + n2
print(n2)