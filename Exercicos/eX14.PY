#Escreva um programa que converta uma temperatura digitada em °C e converta para °F
tempc = float(input('Temperatura ºC: '))
tempf = float((1.8 * tempc) + 32)
tempk = float(tempc + 273)
print('Temperatura: {:.2f}ºF\nTemperatura: {:.2f}K'.format(tempf, tempk))