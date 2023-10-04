salario = float(input('Digite o seu salaraio: R$'))
aumento = float(input('Digite o aumento de salario: '))

novo_aumento = salario * aumento / 100
novo_salario = novo_aumento + salario

print('O seu salario que era de R${} teve um aumento de {}% e foi para R${}'.format(salario, aumento, novo_salario))