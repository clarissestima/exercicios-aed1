# Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada uma sendo vendida
# respectivamente por 10, 12 e 15 reais. Construa um algoritmo em que o usuário forneça a quantidade de
# camisetas pequenas, médias e grandes referentes a uma venda, e a máquina informe quanto será o valor
# arrecadado.

p = int(input("Digite a quantidade de camisetas pequenas:"))
m = int(input("Digite a quantidade de camisetas médias:"))
g = int(input("Digite a quantidade de camisetas grandes:"))

valor_p = p * 10
valor_m = m * 12
valor_g = g * 15

total_arrecadado = valor_p + valor_m + valor_g

print(f"O valor arrecadado de camisetas pequenas é de {valor_p}")
print(f"O valor arrecadado de camisetas médias é de {valor_m}")
print(f"O valor arrecadado de camisetas grandes é de {valor_g}")
print(f"O valor total arrecadado de camisetas é de {total_arrecadado}")