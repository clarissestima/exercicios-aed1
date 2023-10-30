anos = int(input("Digite a quantidade de anos:"))
meses = int(input("Digite a quantidade de meses:"))
dias = int(input("Digite a quantidade de dias:"))

anos_dias = anos * 365
meses_dias = dias * 30

idade_dias = anos_dias + meses_dias + dias
print(f"Sua idade é equivalente a {idade_dias} dias")