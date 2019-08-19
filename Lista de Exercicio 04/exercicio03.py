def vogal(letra):
    if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
        return True
    elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
        return True
    return False

letra = input('Digite uma letra: ')

print(vogal(letra))
