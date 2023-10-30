class Funcionário:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario
    
    def aumentarSalario(self, percentualDeAumento):
        porcentagem = self.salario * percentualDeAumento / 100
        self.salario = self.salario + porcentagem
    
func1 = Funcionário("Roberto",2500)
func1.aumentarSalario(10)
print(func1.salario)
