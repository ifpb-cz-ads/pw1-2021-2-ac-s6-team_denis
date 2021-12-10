#11) Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
# Esse valor será depositado no início de cada mês, e você deve considerá-lo 
# para o cálculo de juros do mês seguinte.
deposito = float(input("Informe o deposito inicial:"))
taxa_juros = float(input("Informe a taxa de juros:"))
deposito_mensal =float(input("Vai depositar quando por mês meu bom ?:"))
mes = 1
saldo = deposito
while mes <= 12:
    saldo = saldo+ (saldo * (taxa_juros  /  100)) + deposito_mensal
    print(f'O valor do saldo do mês {mes} foi de R${saldo:8.2f}')
    mes =  mes +1
    ganho_total = saldo - deposito
print('Ganho total: %.2f'%ganho_total)