def fatoracao(digito):
    fatorial = 1
    while digito > 1:
        fatorial = fatorial * digito
        digito = digito - 1
    return fatorial
    

def main():
        digito = int(input('Digite um número: '))
        while digito >= 0:
            fatorial = fatoracao(digito)
            print(fatorial)
            digito = int(input('Digite um número: '))


main()
