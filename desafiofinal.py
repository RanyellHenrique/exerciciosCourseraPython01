import re

def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    s = frase
    s = re.sub(r'[.\!\:\;\,\?]' , ' ' ,s)
    return s.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def tamanho_medio_de_palavra(texto):
    palavras = []
    palavras  = separa_palavras(texto)
    soma_de_letras = 0
    soma_de_palavras = len(palavras)
    for palavra in palavras:
        soma_de_letras = soma_de_letras + len(palavra)
    return soma_de_letras / soma_de_palavras

def type_token(texto):
    lista = separa_palavras(texto)
    palavras = len(lista)
    palavras_diferentes = n_palavras_diferentes(lista)
    return palavras_diferentes / palavras

def hapax_legomana(texto):
    lista = separa_palavras(texto)
    soma_de_palavras = len(lista)
    palavras_unicas = n_palavras_unicas(lista)
    return palavras_unicas / soma_de_palavras

def tamanho_medio_de_sentenca(texto):
    separacao_sentencas = separa_sentencas(texto)
    soma_de_letras = 0
    sentencas = len(separacao_sentencas)
    for palavra in separacao_sentencas:
        soma_de_letras = soma_de_letras + len(palavra)
    return soma_de_letras / sentencas
    
def complexidade_de_sentenca(texto):
    sentencas = separa_sentencas(texto)
    tamanho_da_sentenca = len(separa_sentencas(texto))
    tamanho_da_frase = len(separa_frases(texto))
    return (tamanho_da_frase + 1) / tamanho_da_sentenca

def tamanho_medio_da_frase(texto):
    lista = separa_palavras(texto)
    palavras = len(lista)
    soma_de_letras = 0
    soma_das_frases = len(separa_frases(texto))
    for palavra in lista:
        soma_de_letras = soma_de_letras + len(palavra)
    return soma_de_letras / soma_das_frases

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    soma_a = sum(as_a)
    soma_b = sum(as_b)
    if soma_a > soma_b:
        return (soma_a - soma_b)/ 6
    return (soma_b - soma_a) / 6
   

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    return [tamanho_medio_de_palavra(texto)
            , type_token(texto), hapax_legomana(texto)
            , tamanho_medio_de_sentenca(texto)
            , complexidade_de_sentenca(texto)
            , tamanho_medio_da_frase(texto)]

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    resultado = []
    texto1 = 0
    for texto in range(0, len(textos), 1):
        resultado.append(calcula_assinatura(textos[texto]))
    return resultado

            