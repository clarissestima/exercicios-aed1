string = input("digita ai caralho: ")
string_nova = ""
cont = 0

while cont < len(string):
    if string[cont] == " " and string[cont + 1] ==  " ":
        cont += 1
        continue
    else:
        string_nova += string[cont]
    cont += 1

print(string_nova)
