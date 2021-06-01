#Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
n = int(input('Digite um numero: '))
print('numero = {}\nDobro do numero = {}\nTriplo do numero = {}\nRaiz do numero = {:.2f}'.format(n,(n*2),(n*3),(n**(1/2))))
