'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
'''
vCasa = float(input('Digite o valor da casa: R$'))
Salario = float(input('Digite seu salário: R$'))
Anos = int(input('Digite quantos anos deseja parcelar o pagamento da casa: '))

parcelas = (vCasa/Anos)/12
valorMinimo = ((Salario*30)/100)

if parcelas <= valorMinimo:
    print('Emprestimo aprovado!')
else:
    print('Não será possivel fazer o emprestimo!')