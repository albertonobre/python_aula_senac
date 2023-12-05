# Escrever um algoritmo que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no
# mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o
# seu nome, o salário fixo e salário no final do mês.

nome = input("Digite o nome do vendedor/a:")
salario = float(input("Digite o salário do vendedor/a:"))
vendas = float(input("Digite o total de vendas do vendedor/a em real:"))

print("Vendedor:", nome)
print("Salário Fixo:", salario)
print("Salário final do mês (Fixo + Comissão):", (vendas * 0.15) + salario)
