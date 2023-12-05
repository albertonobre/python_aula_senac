# Escrever um algoritmo que leia o nome e as três notas obtidas por um aluno durante o semestre. Calcular a sua
# média (aritmética), informar o nome e sua menção aprovado (media >= 7), Reprovado (media <= 5) e Recuperação
# (media entre 5.1 a 6.9).

nomeDoAluno = input("Digite o nome do aluno:")

nota1 = float(input("digite a nota de sua primeira prova:"))
nota2 = float(input("Digite a nota de sua segunda prova:"))
nota3 = float(input("Digite a nota de sua terceira prova:"))

media = (nota1 + nota2 + nota3) / 3

#exibindo a média
print(media)

#condição para saber se o aluno esta aprovado, reprovado ou em recuperação

if media >= 7:
    print(nomeDoAluno, "está Aprovado/a")
elif media <= 5:
    print(nomeDoAluno, "está Reprovado/a")
else:
    print(nomeDoAluno, "está de Recuperação")
    