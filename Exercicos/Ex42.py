'''
Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes
'''
lado1 = int(input('Digite o lado 1: '))
lado2 = int(input('Digite o lado 2: '))
lado3 = int(input('Digite o lado 3: '))

if ((lado1 + lado2) > lado3) and ((lado2 + lado3) > lado1) and ((lado1 + lado3) > lado2):
    if lado1 == lado2 == lado3:
        print('Os segmentos acima PODEM FORMAR um TRIANGULO EQUILÁTERO! ')
    elif lado1 == lado2 or lado1 == lado3 or lado3 == lado2:
        print('Os segmentos acima PODEM FORMAR um TRIANGULO ISÓSCELES! ')
    else:
        print('Os segmentos acima PODEM FORMAR um TRIANGULO ESCALENO! ')
else:
    print('Não forma um triangulo!')