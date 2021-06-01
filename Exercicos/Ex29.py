'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele
foi multado. A multa vai custar R$7,00 por cada km acima do limite.
'''
vel = float(input('Digite a velocidade do carro: '))
if vel > 80:
    print('Voce foi multado!\nMulta = R${}'.format((vel - 80)*7))
else:
    print('Continue assim!')