produto = float(input('Digite o preço do produto: '))
desconto = int(input('Digite o valor do desconto: '))

total_desconto = produto * desconto / 100
total = produto - total_desconto

print('O produto teve um desconto de R${} e o valor total foi para R${}'.format(total_desconto, total))