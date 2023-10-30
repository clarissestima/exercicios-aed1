def splitNAMARRA(texto, sep):
    lista_final = []
    tempo = ""
    cont = 0
    cont_sep = 0
    while cont < len(texto):
        if texto[cont] == sep[cont_sep]:
            achei = True

            while cont_sep < len(sep):
                if texto[cont+cont_sep] != sep[cont_sep]:
                    achei = False
                cont_sep += 1

            if achei:
                lista_final.append(tempo)
                tempo = ""
                cont += cont_sep
            
            else:
                tempo += texto[cont]
                cont += 1
            cont_sep = 0
        else:
            tempo += texto[cont]
            cont += 1            

    return lista_final


string = "Andréx-xPriscox-xVargas"
separador = "x-x"
print(splitNAMARRA(string, separador))