'''
Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50
por Km para viagem até 200km e R$0,45 para viagens mais longas.
'''
dist = float(input('Digite a distancia: '))
if dist > 200:
    print('Preço = R${}'.format(dist * 0.45))
else:
    print('Preço = R${}'.format(dist * 0.50))