# Escrever um algoritmo que leia o nome de um aluno e as notas das três provas que ele obteve no semestre. No final
# informar o nome do aluno e a sua média (aritmética).

nome = input("Digite o nome do aluno/a:")
nota1 = float(input("Digite a primeira nota do aluno/a:"))
nota2 = float(input("Digite a segunda nota do aluno/a:"))
nota3 = float(input("Digite a terceira nota do aluno/a:"))

print("Nome do Aluno/a:", nome)
print("Sua média aritmética é:", (nota1 + nota2 + nota3)/3)
