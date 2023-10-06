import random

print('Tente adivinhar o numero que estou pensando entre 0 e 5!')

numero = random.randint(0, 5)
restart = True
while restart:
    n = int(input('Digite um numero:'))
    if n == numero:
        print('Boa! você acertou!')
        restart = False
    else:
        print('F! você errou!')

