trab = int(input("Digite a nota do trabalho:"))
prov = int(input("Digite a nota da prova:"))

nota_final = ((trab * 2.5) + (prov * 7.5)) / 10

if nota_final < 7:
    print("Está em exame.")
else:
    print(f"Aprovado com a nota {nota_final}")