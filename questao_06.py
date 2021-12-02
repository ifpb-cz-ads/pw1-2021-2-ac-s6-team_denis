#6) Modifique o programa anterior de forma que o usuário também digite o início e o fim da tabuada, 
# em vez de começar com 1 e 10
n = int(input("Informar a tabuada do numero:"))
inicio = int(input("Digite o numero inicial:"))
fim = int(input("Digite o numero final:"))
x = inicio
while x <= fim:
    print(f'{n} X {x} = {n*x}')
    x = x +1
