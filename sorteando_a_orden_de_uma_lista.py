import random
n_alunos = int(input('Digite o numero de alunos a ser listados: '))
alunos = []
for x in range(n_alunos):
    nome = input('Digite o nome do aluno: ')
    alunos.append(nome)

random.shuffle(alunos)
print('A orden de apresentação será \n{}'.format(alunos))
