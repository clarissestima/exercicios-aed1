trab = int(input("Digite a nota do trabalho:"))
prov = int(input("Digite a nota da prova:"))

if trab <= 10 and trab >= 0 and prov <= 10 and prov >= 0:

    nota_final = ((trab * 3) + (prov * 7)) / 10

    if nota_final < 7:
        print("Está em exame.")

    else:
        print(f"Aprovado com a nota {nota_final}")

else:
    print("Nota inválida")