import random
n_alunos = int(input('Digite o numero de alunos a ser listados: '))
alunos = []
for x in range(n_alunos):
    nome = input('Digite o nome do aluno: ')
    alunos.append(nome)

escolhido = random.choice(alunos)
print('O Aluno(a) sorteado foi: {}'.format(escolhido))
