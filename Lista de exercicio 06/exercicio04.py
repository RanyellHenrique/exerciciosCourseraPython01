lista = []
numero = int(input('Digite um número: '))
while numero > 0:
    lista.append(numero)
    numero = int(input('Digite um número: '))

for item in range(len(lista), 0, -1):
    print(lista[item - 1])
