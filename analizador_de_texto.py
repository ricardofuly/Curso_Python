nome = str(input('Digite o seu nome completo: ')).strip()

n_maiusculo = nome.upper()
n_minusculo = nome.lower()
n_tamanho = len(nome)
n_primeiro_nome = nome.find(' ')

print('Seu nome em Maiusculo é {} '
      '\n Seu nome em Minusculo é {} '
      '\n Seu nome tem ao todo {} letras'
      '\n Seu primeiro nome tem {} letras'.format(n_maiusculo, n_minusculo, n_tamanho, n_primeiro_nome))
