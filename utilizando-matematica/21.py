# Criar um algoritmo que auxilie vendedores. A partir de um valor total informado para uma venda,
# mostrar:
#- o total a pagar, considerando um desconto de 10%, se for à vista;
#- o valor de cada parcela, no parcelamento de 3x sem juros;
#- a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto);
#- a comissão do vendedor, no caso da venda ser parcelada (7% sobre o valor total)

valor = int(input("Digite o valor do produto:"))
desconto = valor * 0.1
vista = valor - desconto
print(f"Ao pagar a vista, o valor será {vista}")
parcela = valor / 3
print(f"Ao parcelar em 3x, o valor de cada parcela será de {parcela}")
com_vista = vista * 0.05
print(f"A comissão do vendedor caso a venda for à vista é de {com_vista}")
com_parcela = valor * 0.07
print(f"A comissão do vendedor caso a venda for parcelada é de {com_parcela}")