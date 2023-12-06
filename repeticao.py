# Comandos de repetição
listaCarros = ["Opala", "Chevelle", "Mustang", "Omega", "Fusca", "Uno com escada", "Kadet"]

"""
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

#

for x in listaCarros:
    print(x)

#

i = 0
while i <len(listaCarros):
    if listaCarros[i] == "Omega":
        print(i, " - ", listaCarros[i])
        break
    i += 1

#

i = 0
while i <len(listaCarros):
    print( i ," - ", listaCarros[i])
    if listaCarros[i] =="Omega":
        break
    i += 1

#

for x in listaCarros:
    if x == "Omega":
        continue
    print(x)

#

i = 0
while i <len(listaCarros):
    if listaCarros[i] == "Omega":
        break
    i+=1
while i <len(listaCarros):
    print(listaCarros)
    i+=1
"""

#print(listaCarros)
#listaCarros.sort()
#print(listaCarros)


#listaCarros.sort(reverse = True)
#print(listaCarros)

print(listaCarros)
posicao = 0
i = 0
while i <len(listaCarros):
    if listaCarros[i] == "Mustang":
        posicao = i
    i+=1

print(posicao)

listaNova = []
while posicao < len(listaCarros):
    listaNova.append(listaCarros[posicao])
    posicao += 1
print(listaNova)