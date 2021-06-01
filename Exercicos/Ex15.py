#Escreva um programa ue pergunte a uantidade de Km percorrido por um carro alugado e a uantidade de dias pelo quais ele foi alugado. Calcule o preço a pagar, sabendo ue o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Digite a quantidade de km percorrida: '))
dia = float(input('Digite a quantidade de dias pelos quais ele foi alugado: '))
preco = (60 * dia) + (0.15 * km)
print('Preço a pagar: {:.2f}'.format(preco))
