def numero_primo(numero):
    if  0 != numero != 1:
        n = 2
        while n < numero:
            resultado = numero % n
            n += 1
            if resultado == 0:
                return False
        return True
    return False

def maior_primo(numero):
    if numero > 1:
        primo = numero_primo(numero)
        if primo:
            return numero
        n = numero
        while primo == False:
            n -= 1
            primo = numero_primo(n)
            if primo == True:
                return n
    return numero



        




