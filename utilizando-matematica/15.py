a = int(input("Digite o valor de A:"))
b = int(input("Digite o valor de B:"))
c = int(input("Digite o valor de C:"))

if a + b > c and b + a > c and c + a > b:

    if a == b and a == c:
        triangulo = "equilátero"
        print(f"O triângulo é {triangulo}")
    elif a != b and a != c and b != c:
        triangulo = "escaleno"
        print(f"O triângulo é {triangulo}")
    else:
        triangulo = "isósceles"
        print(f"O triângulo é {triangulo}")
else:
    print("O formato não é um triângulo")