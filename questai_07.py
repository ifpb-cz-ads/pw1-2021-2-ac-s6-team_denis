#7) Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo segundo. 
# Utilize apenas os operadores de soma e subtração para calcular o resultado. 
# Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas de um deles. 
# Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
n1 = int(input("Informe o primeiro numero:"))
n2 = int(input("Informe o segundo numero:"))

def multiplica(n1,n2):
    resultado = 0
    for k in range(n1):
        resultado = resultado + n2
    return resultado
    
print(multiplica(n1,n2))
