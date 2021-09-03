'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M e F. Caso esteja errado peça até ter um
valor correto.
'''
sexo = str(input('Digite o sexo: [M/F] ')).upper()
while sexo not in 'MF':
        print('Por favor digite um sexo valido!')
        sexo = str(input('Digite o sexo: ')).upper()

print('fim')