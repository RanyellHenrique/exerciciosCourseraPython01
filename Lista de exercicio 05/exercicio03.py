def n_primos(n):
    primo = True
    qtd = 0
    primeiro = segundo = n - 1
    while segundo >= 1:
        primo = True
        while primeiro >= 2 and primo:
            if n % primeiro == 0:
                primo = False
                primeiro = primeiro - 1
            else:
                primeiro = primeiro - 1
        if primo:
            qtd = qtd + 1
        primeiro = n = n - 1
        primeiro = primeiro - 1
        segundo = segundo - 1
    return qtd

            
        
                

