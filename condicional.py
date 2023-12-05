
a = False
print(type(a))
if a:
    print("Verdadeiro")
else:
    print("Falso")

# a>b a<b a>=b a<=b
# a!=b diferentes
# a==b igauis

# n1 > n2

# Setando os números, ex:
n1 = 50
n2 = 12

# Buscando os números, ex:
#n1 = int(input("Digite o primeiro número:"))
#n2 = int(input("Digite o segundo número:"))


if n1>n2:
    print(n1, "É maior que", n2)
else:
    print(n1, "È menor que", n2)


# Verificando nome

nome = input("Digite um nome:")
if nome == "Jose":
    print("È igual a Jose")
else:
    print("É diferente de Jose")


# Condição dupla

nomeDoAluno = input("Digite seu nome:")

nota1 = float(input("digite a note de sua primeira prova:"))
nota2 = float(input("Digite a nota de sua segunda prova:"))
nota3 = float(input("Digite a nota de sua terceira prova:"))

media = (nota1 + nota2 + nota3) / 3

#exibindo a média
print(media)

#condição para saber se o aluno esta aprovado, reprovado ou em recuperação

if media >= 7:
    print(nomeDoAluno, "está Aprovado/a")
elif media < 5:
    print(nomeDoAluno, "está Reprovado/a")
else:
    print(nomeDoAluno, "está de Recuperação")
