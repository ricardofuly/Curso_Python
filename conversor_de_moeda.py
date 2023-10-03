saldo = int(input("Digite o seu saldo: R$ "))

dolar = 5.13
resultado = saldo / dolar

print('Com R${:.2f} voce pode comprar U${:.2f}'.format(saldo, resultado))