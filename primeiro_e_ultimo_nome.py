n = str(input('Digite o seu nome completo: ')).strip()
nome = n.split()
primeiro_n = nome[0]
ultimo_n = nome[len(nome)-1]
print('Seu Primeiro nome é {} '
      '\n seu ultimo nome é {}'.format(primeiro_n, ultimo_n))
