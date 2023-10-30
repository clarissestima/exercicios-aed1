lista = []
n = 0
while n >= 0: #para quando digita -1
    n = int(input("Digite um elemento: "))
    lista.append(n)

valor = int(input("Digite um valor a ser buscado: "))

def buscarValor_vezes(valor):
    indice = 0
    vezes = 0
    while indice < len(lista):
        if valor == lista[indice]:
            vezes += 1
        indice += 1
    return vezes

print(buscarValor_vezes(valor))