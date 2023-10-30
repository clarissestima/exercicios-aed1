frase = input("Digite uma frase: ")
cont = 0
nova = ""
espaço = False


while cont < len(frase):
    if cont == 0 and frase[cont] != " ":
        nova += chr(ord(frase[cont]) - 32)
        cont += 1

    if frase[cont] == chr(32):
        espaço = True
        nova += chr(32)
    
    if espaço == True:
        nova += chr(ord(frase[cont+1]) - 32)
        espaço = False
        cont += 1
    else:
        nova += frase[cont]
    cont += 1

print(nova)