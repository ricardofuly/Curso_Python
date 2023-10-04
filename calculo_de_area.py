largura = float(input('Insira a largura da sua parede: '))
altura = float(input('Insira a altura da sua parede: '))

area = largura * altura
tinta = area * 2

print('A sua parede tem de {} x {} tem uma area de {}m, e voce vai precisar de {}l de tinta para pinta-la'.format(largura, altura, area, tinta))