# Comandos de repetição

for x in range(0,10):
    print(x)

#

listaNomes = ["Maria", "Ana", "Pedro", "João"]
for x in listaNomes:
    print(x)

#

numeros = (3,6,4,9)
soma = 0
for x in numeros:
    soma += x
print(soma)

#

i = 0
while i<10:
    print(i)
    i+=1

#

lista = ["a", "b", "c", "d", "e", "f"]
i = 0
while i < len(lista):
    print(i, " - ", lista[i])
    i += 1
