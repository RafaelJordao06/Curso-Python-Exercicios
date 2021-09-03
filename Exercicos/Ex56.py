'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
A media de idade do grupo
Qual é o nome do homem mais velho
Quantas mulheres tem nemos de 20 anos
'''
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
nomeVelho = 0
totMulher20 = 0
for p in range(1,5):
    print('----- {}° PESSOA ------'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('M/F: ')).strip()
    somaIdade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        totMulher20 +=1
mediaIdade = somaIdade / 4
print('A media do grupo é de {} anos.'.format(mediaIdade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadeHomem, nomeVelho))
print('Ao total são {} mulheres com menos de 20 anos.'.format(totMulher20))