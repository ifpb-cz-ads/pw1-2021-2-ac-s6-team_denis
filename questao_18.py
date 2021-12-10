#18) Escreva um programa que calcule o resto da divisão inteira entre dois números. 
# Utilize apenas as operações de soma e subtração para calcular o resultado.

n1 = int(input("Informe o primeiro numero:"))
n2 = int(input("Informe o segundo numero:"))
if n1 < n2:
    print(n1)
else:
    while n1 >= n2:
        n1 = n1 - n2
    print(f'Resto é igual a :{n1}')
        
