temp_f = int(input("Digite a temperatura em Fahrenheit:"))

if temp_f < 0:
    print("Por favor digite uma temperatura positiva")

temp_c_aprox = (temp_f - 30) / 2
temp_c_exata = (temp_f - 32) / 1.8

diferença = temp_c_aprox - temp_c_exata

print(f"A temperatura em Celsius aproximada é {temp_c_aprox}")
print(f"A temperatura em Celsius exata é {temp_c_exata}")

if diferença > 4:
    print("A diferença é maior que 4")

else:
    print("A diferença é menor que 4")