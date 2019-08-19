numero = int(input('Digite um número: '))
soma = 0
while numero > 0:
    n1 = numero % 10
    numero = numero // 10
    soma = soma + n1

print(f'A soma é {soma}')
    
