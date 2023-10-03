medida = float(input('Digite a sua medida em metros: '))
dc = medida * 10
cm = medida * 100
mm = medida * 1000
dam = medida / 10
hec = medida / 100
km = medida / 1000

print('A medida de {}m corresponde a \n{:.0f}dc \n{:.0f}cm \n{:.0f}mm \n{:.0f}dam \n{:.0f}hec \n{}km'.format(medida, dc, cm, mm, dam, hec, km))

