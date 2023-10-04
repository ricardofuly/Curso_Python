dias = int(input('Quantos dias o carro foi alugado: '))
km = float(input('Quantos km o carro percorreu: '))

valor_carro = 60
km_rodado = 0.15

total = (valor_carro * dias) + (km_rodado * km)

print('O carro foi alugado por {} dias e percorreu um total de {}km o valor total foi de R${}'. format(dias, km, total))