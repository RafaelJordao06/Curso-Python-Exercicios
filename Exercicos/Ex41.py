'''
A Confederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Ate 9 anos : MIRIM
- Ate 14 anos : INFANTIL
- Ate 19 anos : JÚNIOR
- Ate 25 anos : SÊNIOR
- Acima de 25 anos : MASTER
'''
from datetime import date
nascimento = int(input('Digite o ano de nascimento: '))
idade = (date.today().year) - nascimento
print('O atetla tem {}'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
elif idade > 25:
    print('MASTER')
else:
    print('Idade não corresponde a nenhuma categoria!')