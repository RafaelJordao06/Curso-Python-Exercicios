#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = ((co ** 2) + (ca ** 2)) ** (1/2)
h2 = math.hypot(co, ca)
print('A hipotenussa é {:.2f}'.format(h))
print('A himpotenusa 2 é {:.2f}'.format(h2))
