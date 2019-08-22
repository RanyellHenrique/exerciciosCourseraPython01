def imprime(l, a):
    n = l
    m = a
    while a > 0:
        while l > 0:
            print('#', end = '')
            l = l - 1
        print()
        a = a - 1
        l = n
        
def main():
    l = int(input('Digite a largura:'))
    a = int(input('Digite a altura:'))
    imprime(l, a)

main()

    

