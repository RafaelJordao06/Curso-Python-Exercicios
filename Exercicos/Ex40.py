'''
 Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- media abaixo de 5.0 : REPROVADO
- media entre 5.0 6.9: RECUPERAÇÃO
- media 7.0 e superior: APROVADO
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2)/2
print('Sua media é: {:.1f}'.format(media))
if media <= 5.0:
    print('REPROVADO!')
elif media > 5.0 and media <= 6.9:
    print('RECUPERAÇÃO!')
elif media >= 7.0:
    print('APROVADO!')