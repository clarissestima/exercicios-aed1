def verificarPalindromo(frase):
  frase_invertida = ""
  frase_desespaçada = ""
  cont = len(frase) - 1
  for i in frase:
    if i != " ":
      frase_desespaçada += i
  while cont >= 0:
    if frase[cont] != " ":
      frase_invertida += frase[cont]
    cont -= 1
  if frase_invertida == frase_desespaçada:
    return True
  else:
    return False
  

texto = "a grama é amarga"
print(verificarPalindromo(texto))