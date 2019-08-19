numero = int(input('Digite um número inteiro: '))
contagem = numero
n = 1
divisivel = False

while contagem > 0 and not divisivel:
    resultado = numero % (n + 1)
    contagem = contagem - 1
    n = n + 1
    if n == numero:
        break
    elif resultado == 0:
        divisivel = True

if divisivel:
    print('não primo')
else:
    print('primo')
