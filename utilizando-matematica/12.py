peso = int(input("Digite seu peso:"))
altura = float(input("Digite sua altura:"))
sexo = input("Digite seu sexo:")

if sexo == "feminino":
    peso_ideal = (62.1 * altura) - 44.7
    variação = (peso_ideal * 8) / 100
    peso_minimo = peso_ideal - variação
    peso_maximo = peso_ideal + variação
    print(f"Seu peso ideal é aproximadamente {int(peso_ideal)}")
    print(f"Seu peso mínimo é aproximadamente {int(peso_minimo)}")
    print(f"Seu peso máximo é aproximadamente {int(peso_maximo)}")
    if peso > peso_minimo and peso < peso_maximo:
        print("Seu peso está na média")
    elif peso < peso_minimo:
        print("Seu peso está abaixo da média")
    elif peso > peso_maximo:
        print("Seu peso está acima da média")

elif sexo == "masculino":
    peso_ideal = (72.7 * altura) - 58.0
    variação = (peso_ideal * 8) / 100
    peso_minimo = peso_ideal - variação
    peso_maximo = peso_ideal + variação
    print(f"Seu peso ideal é aproximadamente {int(peso_ideal)}")
    print(f"Seu peso mínimo é aproximadamente {int(peso_minimo)}")
    print(f"Seu peso máximo é aproximadamente {int(peso_maximo)}")
    if peso > peso_minimo and peso < peso_maximo:
        print("Seu peso está na média")
    elif peso < peso_minimo:
        print("Seu peso está abaixo da média")
    elif peso > peso_maximo:
        print("Seu peso está acima da média")