'''
 Crie um programa que faça o computador jogar Jokenpô com você.
'''
import random
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2)
print('''SUAS OPÇÕES
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jogador = int(input('Qual é a sua jogada: '))
print('-='*15)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('-='*15)
if computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('PAPEL ganha de PEDRA!\n VOCÊ VENCEU!!!!')
    elif jogador == 2:
        print('TESOURA NÃO ganha de PEDRA\n VOCÊ PERDEU!!!!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 1:
    if jogador == 0:
        print('PEDRA NÃO ganha de PAPEL!\n VOCÊ PERDEU!!!!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('TESOURA ganha de PAPEL"\n VOÊ VENCEU!!!!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2:
    if jogador == 0:
        print('PEDRA ganha de TESOURA"\n VOÊ VENCEU!!!!')
    elif jogador == 1:
        print('PAPEL NÃO ganha de TESOURA!\n VOCÊ PERDEU!!!!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVALIDA!')