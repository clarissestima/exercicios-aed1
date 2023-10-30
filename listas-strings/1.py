lista = []
n = 0
while n >= 0: #para quando digita -1
    n = int(input("Digite um elemento: "))
    lista.append(n)

valor = int(input("Digite um valor a ser buscado: "))

def buscarValor(valor):
    indice = 0
    while indice < len(lista):
        if valor == lista[indice]:
            return indice
        indice += 1

print(buscarValor(valor))
