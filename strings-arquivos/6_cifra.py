def cripto(nome_arq, deslocamento, saida_arq):
    arq = open(nome_arq, "r")
    texto = arq.read()
    converte = ""
    for i in texto:
        converte += chr(ord(i) + deslocamento)
    arq.close()
    arq = open(saida_arq, "w")
    arq.write(converte)
    arq.close()
    return converte

def descripto(ori_arq, deslocamento, rec_arq):
    arq = open(ori_arq, "r")
    texto = arq.read()
    converte = ""
    for i in texto:
        converte += chr(ord(i) - deslocamento)
    arq = open(rec_arq, "w")
    arq.write(converte)
    arq.close()
    return converte

print(cripto("/Users/Paulo/Documents/aulas/AED10_08_22.py/texto.txt", 3, "texto_cripto.txt"))
print(descripto("/Users/Paulo/Documents/aulas/AED10_08_22.py/texto_cripto.txt", 3, "texto_reconstruido.txt"))