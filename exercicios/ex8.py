# Elaborar um algoritmo que efetue a apresentação do valor da conversão em real (R$) de um valor lido em dólar
# (US$). O algoritmo deverá solicitar o valor da cotação do dólar e também a quantidade de dólares disponíveis com o
# usuário.

cotacao = float(input("Digite a cotação do dólar:"))
carteira = int(input("Digite o valor possuido em dólar:"))

real = cotacao * carteira

print("O valor possuído em reais é de:", real)
