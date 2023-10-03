valor = int(input('Digite um numero para saber a sua tabuada: '))

print('-' * 12)
for i in range(11):
    resultado = valor * i
    print('{} x {:2} = {} \n'.format(valor, i, resultado))
print('-' * 12)