num1 = int(input("Digite o 1º número:"))
num2 = int(input("Digite o 2º número:"))
num_res = 0
cont = 0

while cont < num2:
    num_res = num_res + num1
    cont += 1

print(num_res)