#8) Escreva um programa que leia dois números. Imprima a divisão inteira do primeiro pelo segundo,
# assim como o resto da divisão. Utilize apenas os operadores de soma e subtração para calcular o resultado.
# Lembre-se de que podemos entender o quociente da divisão de dois números como a quantidade de vezes que 
# podemos retirar o divisor do dividendo. Logo, 20 ÷ 4 = 5, uma vez que podemos subtrair 4 cinco vezes de 20
n1 = int(input("Informe o primeiro numero:"))
n2 = int(input("Informe o segundo numero:"))
cont = 0 
while n2 <= n1:
    cont = cont +1
    n1 = n1 - n2    
print(cont)
print(n1)

