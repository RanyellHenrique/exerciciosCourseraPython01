x1 = float(input('Digite o primeiro X: '))
y1 = float(input('Digite o primeiro Y: '))
x2 = float(input('Digite o segundo X: '))
y2 = float(input('Digite o segundo Y: '))

distancia = (((x1 - x2)**2) + ((y1 - y2)**2))**(1/2)

if distancia >= 10:
    print('longe')
else:
    print('perto')


