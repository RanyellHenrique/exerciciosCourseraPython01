a = float(input('Digite o parâmetro a: '))
b = float(input('Digite o parâmetro b: '))
c = float(input('Digite o parâmetro c: '))

bhaskara = b**2 -(4*a*c)


if bhaskara < 0:
    print('esta equação não possui raízes reais')
elif bhaskara == 0:
    x = (-b/(2*a))
    print(f'a raiz desta equação é {x}')
else:
    x1 = (-b + (bhaskara**(1/2)))/(2*a)
    x2 = (-b - (bhaskara**(1/2)))/(2*a)
    if x1 > x2:
        print(f'as raízes da equação são {x2} e {x1}')
    else:
        print(f'as raízes da equação são {x1} e {x2}')
