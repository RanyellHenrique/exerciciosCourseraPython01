numero = int(input('Digite um número: '))
numeros_iguais = False

while numero > 0 and not numeros_iguais:
    i1 = numero % 10
    numero = numero // 10
    i2 = numero % 10
    if i1 == i2:
        numeros_iguais = True

if numeros_iguais:
    print ('sim')
else:
    print('não')
