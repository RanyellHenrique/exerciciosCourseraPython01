def computador_escolhe_jogada(n, m):
    remove = 1
    while remove != m:
        if (n - remove) % (m+1) == 0:
            return remove
        else:
            remove += 1
    return remove
    
def usuario_escolhe_jogada(n, m):
    digito = False
    while not digito:
        remove = int(input('Quantas peças vai tirar? '))
        if remove > m or remove < 1:
            print()
            print('Oops! Jogada inválida! Tente de novo.')
            print()
        else:
            digito = True
    return remove

def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    pc = False
    if n % (m+1) == 0:
        print()
        print('Voce começa!')
    else:
        print()
        print('Computador começa!')
        pc = True

    while n > 0:
        if pc:
            removepc = computador_escolhe_jogada(n, m)
            n = n - removepc
            if removepc == 1:
                print()
                print('O computador tirou uma peça.')
            else:
                print()
                print(f'O computadoer tirou {removepc} peças.')
            pc = False
        else:
            remove = usuario_escolhe_jogada(n, m)
            n = n - remove
            if remove == 1:
                print()
                print('Você tirou uma peça')
            else:
                print()
                print('Você tirou', remove, 'peças')
            pc = True
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
            print()
        else:
            if n != 0:
                print(f'Agora restam, {n} peças no tabuleiro.')
                print()
    print('Fim do jogo! O computador ganhou!')

print('Bem-vindo ao jogo do NIM! Escolha:')
print()

print('1 - para jogar uma partida isolada')

tipoDePartida = int(input('2 - para jogar um campeonato '))

if tipoDePartida == 2:
    print()
    print('Voce escolheu um campeonato!')
    print()
    campeonato()
else:
    if tipoDePartida == 1:
        print()
        partida()

def campeonato():
    numeroRodada = 1
    while numeroRodada <= 3:
        print()
        print('**** Rodada', numeroRodada, '****')
        print()
        partida()
        numeroRodada += 1
    print()
    print('Placar: Você 0 X 3 Computador')
            
