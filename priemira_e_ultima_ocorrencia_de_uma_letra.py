s = str(input('Digite uma frase: ')).upper().strip()
s_count = s.count('A')
s_primeira = s.find('A') + 1
s_ultima = s.rfind('A') + 1

print('A letra A aparece {} vezes na frase'
      '\n A primeira letra A apareceu na posição {}'
      '\n A última letra A apareceu na posição {}'.format(s_count, s_primeira, s_ultima))
