#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento 
salario = float(input('Digite o salario: '))
porcentagem = (salario * 15)/100
nvsalario = porcentagem + salario
print('Novo salario : {}'.format(nvsalario))