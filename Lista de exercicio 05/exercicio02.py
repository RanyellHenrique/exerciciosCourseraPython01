def imprime(l, a):
    n = l
    m = a
    while a > 0:
        while l > 0:
            if (l == 1 or l == n) or (a == m or a == 1) :
                print('#', end = '')
            else:
                print('', end = ' ')
            l = l - 1
        print()
        a = a - 1
        l = n
def main():
    l = int(input('Digite a largura:'))
    a = int(input('Digite a altura:'))
    imprime(l, a)

main()
