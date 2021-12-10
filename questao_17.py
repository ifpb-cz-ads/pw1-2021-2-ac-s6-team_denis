#17) Modifique o programa anterior de forma a ler um número n. Imprima os n primeiros números primos
n = int(input("Digite um número: "))
if n < 0:
    print("Número inválido. Digite apenas valores positivos")
else:
    if n >= 1:
        print("2")
        p = 1
        y = 3
        while p < n:
            x = 3
            while(x < y):
                if y % x == 0:
                    break
                x = x + 2
            if x == y:
                print(x)
                p = p + 1
            y = y + 2
        
        
        
        
        
        
    
        