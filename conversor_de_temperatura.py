temperatura = float(input('Digite a temperatura em graus celsius: '))

f = (temperatura * 9 / 5) + 32
k = temperatura + 273.15

print('A temperatura  de {}°C corrsponde a {}°F e {}°K'.format(temperatura, f, k))
