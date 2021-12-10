#13) Escreva um programa que leia números inteiros do teclado. 
# O programa deve ler os números até que o usuário digite 0 (zero).
# No final da execução, exiba a quantidade de números digitados, 
# assim como a soma e a média aritmética
valor = int(input("Informe um numero inteiro:"))
cont = 0
soma = 0
while valor != 0:
    soma = soma + valor
    cont = cont + 1
    valor = int(input("Informe um numero inteiro:"))
print(f'Quantidade de numeros digitados:{cont}')
print('Media Aritmetica foi de: %2.f'%(soma / cont))