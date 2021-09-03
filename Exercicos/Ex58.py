'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar
adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
'''
from random import randint

computador = randint(0, 10)
print('Sou seu computador, acabei de pensar em um número de 0 a 10.\n Acha que consegue adivinhar ele??')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual número estou pensando? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Vish... MENOS!')
        else:
            print('Vish... MAIS!')
print('Acertou com {} tentativas'.format(tentativas))