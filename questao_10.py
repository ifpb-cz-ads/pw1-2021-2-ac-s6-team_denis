#10) Escreva um programa que pergunte o depósito inicial e a taxa de juros de uma poupança.
# Exiba os valores mês a mês para os 12 primeiros meses. Escreva o total ganho com juros no período

deposito = float(input("Informe o deposito inicial:"))
taxa_juros = float(input("Informe a taxa de juros:"))
mes = 1
saldo = deposito
while mes <= 12:
    saldo = saldo+ (saldo * (taxa_juros  /  100))
    print(f'O valor do saldo do mês {mes} foi de R${saldo:8.2f}')
    mes =  mes +1
    ganho_total = saldo - deposito
print('Ganho total: %.2f'%ganho_total)


