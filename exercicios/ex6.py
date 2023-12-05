# Ler dois valores para as variáveis A e B, e efetuar as trocas dos valores de forma que a variável A passe a possuir o
# valor da variável B e a variável B passe a possuir o valor da variável A. Apresentar os valores trocados.

a = int(input("Digite um valor para a:"))
b = int(input("Digite um valor para b:"))
c = a
d = b

print("Valor de a:", a)
print("Valor de b:", b)

a = d
print("Novo valor para a:", a)
b = c
print("Novo valor para b:", b)
