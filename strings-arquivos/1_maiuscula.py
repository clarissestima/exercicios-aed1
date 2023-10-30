frase_minuscula = input("Digite uma frase: ")
frase_maiuscula = ""
cont = 0

while cont < len(frase_minuscula):
    frase_maiuscula = frase_maiuscula + chr(ord(frase_minuscula[cont]) - 32)
    cont += 1

print(frase_maiuscula)