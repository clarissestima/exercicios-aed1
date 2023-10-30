# Construa um algoritmo que calcula a quantidade de litros de combustível gastos em uma viagem
# utilizando-se um automóvel que faz 14 km/litro. Para realizar este cálculo, o usuário deverá fornecer o tempo
# gasto da viagem e a velocidade média durante a mesma. O algoritmo deverá apresentar, como resultado, a
# distância percorrida e a quantidade de litros utilizada para a viagem.

t = int(input("Digite o tempo gasto da viagem:"))
vm = int(input("Digite a velocidade média durante a viagem:"))

d = t * vm
l = d / 14

print(f"A distância percorrida foi de {d}")
print(f"A quantidade de litros utilizada foi de {l}")