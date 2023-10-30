senha = input("Digite sua senha: ")
força = ""
maiuscula = 0
minuscula = 0
numero = 0
especial = 0

for i in range (len(senha)):
    if ord(senha[i]) >= 65 and ord(senha[i]) <= 90:
        maiuscula = 1
    if ord(senha[i]) >= 97 and ord(senha[i]) <= 122:
        minuscula = 1 
    if ord(senha[i]) >= 48 and ord(senha[i]) <= 57:
        numero = 1
    else:
        especial = 1

soma = maiuscula + minuscula + numero + especial

if soma <= 2:
    força = "Fraca"
elif soma <= 3:
    força = "Média"
else:
    força = "Forte"

print(força)
print(maiuscula, minuscula, numero, especial)



"""if maiuscula == True and minuscula == True and numero == True and especial == True:
    força = "Forte"
elif maiuscula == False and minuscula == True and numero == True and especial == True:
    força = "Média"
elif maiuscula == False and minuscula == True and numero == True and especial == False:
    força = "Fraca"""
    