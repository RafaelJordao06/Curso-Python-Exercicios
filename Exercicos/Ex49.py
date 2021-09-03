'''
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora ultilizando um laço for
'''
n = int(input('Digite o numero que estar criando a tabuada: '))
for c in range(1,11):
    print('{} X {:2} = {}'.format(n,c,(n*c)))