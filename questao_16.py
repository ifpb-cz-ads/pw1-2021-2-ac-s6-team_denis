#16) Escreva um programa que leia um número e verifique se é ou não um número primo. 
# Para fazer essa verificação, calcule o resto da divisão do número por 2 e depois por
# todos os números ímpares até o número lido. Se o resto de uma dessas divisões for igual a zero,
# o número não é primo. Observe que 0 e 1 não são primos e que 2 é o único número primo que é par.
numero = int(input("Informe um numero ou digite 0 para sair"))
cont = 0
n = 1
while n <= numero:
    resto = numero % n
    if resto == 0:
         cont = cont + 1
    n = n+1
if cont == 2:
        print(f'O numero {numero} é um numero primo!')
else:
        print(f'O numero {numero} nao é primo!')

    