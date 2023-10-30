# Sobre o salário bruto de um funcionário, são descontados 8% de INSS, 10% de IR (Imposto de Renda) e,
# sobre o restante, 0,5% referente à filiação sindical. Ao ser fornecido o valor do salário bruto do funcionário,
# calcule:
#• Os descontos de INSS, IR e filiação sindical;
#• O total dos descontos;
#• O salário líquido.

sb = int(input("Digite o seu salário bruto:"))

inss = sb * 0.08
print(f"O desconto do INSS é de {inss}")
ir = sb * 0.1
print(f"O desconto do imposto de renda é de {ir}")
fs = sb * 0.005
print(f"O desconto da filiação sindical é de {fs}")

total = inss + ir + fs
print(f"Foi descontado {total} do seu salário ao total")

sl = sb - total
print(f"Seu salário líquido é de {sl}")