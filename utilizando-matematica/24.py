# João recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1 = R$ 200,00 e C2 = R$120,00)
# que estão atrasadas. Como as contas estão atrasadas, João terá de pagar multa de 2% sobre cada conta. Faça
# um algoritmo que calcule e mostre quanto restará do salário do João.

joao = 1200
C1 = 200
C2 = 120

multa_C1 = C1 + (C1 * 0.2)
multa_C2 = C2 + (C2 * 0.2)

joao_multado = joao - (multa_C1 + multa_C2)

print(f"Sobrou {joao_multado} do salário do João")