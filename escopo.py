# escopo / variavel global

x = "Senac"
# Variavel global, criada fora do escopo(função)

def Mostrar():
    print(x)

Mostrar()

x = "Alberto"

def MostrarNome():
    x = "SENAC"
    print(x)

MostrarNome()
print(x)
