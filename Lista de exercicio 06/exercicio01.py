def remove_repetidos(lista):
    novo_conjunto = set(lista)
    nova_lista = [] 
    for item in novo_conjunto:
        nova_lista.append(item)
    nova_lista.sort()
    return nova_lista
