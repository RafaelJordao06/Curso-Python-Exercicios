'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar
ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo
 que falta ou que passou do prazo.
'''
import datetime

anoNascimento = int(input('Digit o ano de nascimento: '))
anoAtual = datetime.date.today().year
idade = anoAtual - anoNascimento
if idade > 18:
    saldo = idade - 18
    print('Você tem {} anos, e não pode mais se alistar!'.format(idade))
    print('Voce deveria ter se alistado a {} anos!'.format(saldo))
elif idade < 18:
    saldo = 18 - idade
    print('Voce tem {} anos, assim que fizer 18 precisa se alistar!'.format(idade))
    print('Ainda falta {} para voce se alistar!'.format(saldo))
elif idade == 18:
    print("Voce precisa se alistar imediatamente!!")