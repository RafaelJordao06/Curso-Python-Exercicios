'''
Faça um programa que leia uma frase pelo teclado e mostre:
1 Quantas vezes aparece a letra "A"
2 Em que posoção ela aparece a primeira vez
3 Em que posição ela aparece a última vez
'''
frase = str(input('Digite a frase: ')).strip()
print(frase.upper().count('A'))
print(frase.upper().find('A')+1)
print(frase.upper().rfind('A')+1)