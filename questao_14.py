#14) Escreva um programa para controlar uma pequena máquina registradora.
# Você deve solicitar ao usuário que digite o código do produto e a quantidade 
# comprada. Utilize a tabela de códigos abaixo para obter o preço de cada produto
#Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro “Código inválido”


#Tabela de cada preço de acordo com o codigo
apagar = 0
while True:
    código = int(input("Código da mercadoria (0 para sair):"))
    preço = 0
    if código == 0:
        break;
    elif código == 1:
        preço = 0.50
    elif código == 2:
        preço = 1.00
    elif código == 3:
        preço = 4.00
    elif código == 5:
        preço = 7.00
    elif código == 9:
        preço = 8.00
    else:
        print("Código inválido!")
    if preço != 0:
        quantidade = int(input("Quantidade:"))
        apagar = apagar + (preço * quantidade)
print("Total a pagar R$%8.2f" % apagar)