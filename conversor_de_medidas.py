medida = float(input('Digite a sua medida em metros: '))
cm = medida * 100
mm = medida * 1000
km = medida / 1000

print('A medida de {}m corresponde a \n{:.0f}cm \n{:.0f}mm \n{}km'.format(medida, cm, mm, km))

