lista = []
lista_reversa = []
n = -1
cont = 0
while True:
    n = int(input("Digite um elemento: "))
    if n == 0:
        break
    lista.append(n)
print(lista)

while cont < len(lista):
    cont += 1
    lista_reversa.append(lista[len(lista) - cont])
print(lista_reversa)