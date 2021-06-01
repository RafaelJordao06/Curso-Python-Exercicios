# Faça um programa que leia um angulo qualquer e mostre na tela o valor do
# Seno, Cosseno e a Tangente desse angulo
from math import radians,sin,cos,tan
angulo = float(input('Digite o angulo: '))
seno = sin(radians(angulo))
cons = cos(radians(angulo))
tang = tan(radians(angulo))
print('Angulo = {}\nSeno = {:.2f}\nCosseno = {:.2f}\nTangente = {:.2f}'.format(angulo,seno,cons,tang))