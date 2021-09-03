'''
Faça um programa que leia um número interio e diga se ele é ou não um número primo.
'''
n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[35m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso que ele NÃO É PRIMO!')