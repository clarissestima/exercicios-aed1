import random as r
arq = open("/Users/Paulo/Documents/aulas/AED10_08_22.py/embaralhar.csv", "r")
palavras = arq.readlines()

indice = r.randint(0, len(palavras) - 1)
palavra = palavras[indice]
palavra = palavra[:-1]

lista = []
cont = 0
embaralhada = ""
tentativas = 6

for i in palavra:
    lista += [""]

while cont < len(palavra):
    vazio = r.randint(0, (len(palavra) - 1))
    if len(lista[vazio]) == 0:
        lista[vazio] = palavra[cont]
        cont += 1

for i in range (len(lista)):
    embaralhada += lista[i]

while True:
    print(f"A palavra embaralhada é {embaralhada}, você tem {tentativas} tentativas. Boa sorte!")
    tentativa = input("Digite sua resposta: ")
    tentativas -= 1
    if tentativa == palavra:
        print("Você adivinhou! Parabéns!")
        break
    if tentativas == 0:
        print(f"Você perdeu, a resposta era {palavra}")
        break
    