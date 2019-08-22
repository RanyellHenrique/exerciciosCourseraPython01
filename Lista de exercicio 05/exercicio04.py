def é_hipotenusa(n):
    resultado = False
    a = b = n - 1
    a**2 + b**2
    while a > 1:
        while b > 1:
            if n**2 == a**2 + b**2:
                resultado = True
            b = b - 1
        a = a - 1
        b = n - 1
    return resultado

def soma_hipotenusas(n):
    soma = []
    while n > 1:
        if é_hipotenusa(n):
            soma.append(n)
        n = n - 1
    soma1 = set(soma)
    resultado = sum(soma1)
    return resultado
        
