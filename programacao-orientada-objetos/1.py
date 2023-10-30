class Triangulo:
    def __init__(self, a, b, c):
        self.ladoA = a
        self.ladoB = b
        self.ladoC = c
    
    def calcularPerimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro 
    
    def obterMaiorLado(self):
        maior_lado = self.ladoA
        lado = "A"
        if self.ladoB > maior_lado:
            maior_lado = self.ladoB
            lado = "B"
        if self.ladoC > maior_lado:
            maior_lado = self.ladoC
            lado = "C"
        if self.ladoA == self.ladoB and self.ladoA == self.ladoC:
            return "lados iguais"
        return lado
    
    def ehTriangulo(self):
        if self.ladoA + self.ladoB > self.ladoC or self.ladoA + self.ladoC > self.ladoA or self.ladoC + self.ladoB > self.ladoA:
            return True
        return False
    
    def informaTipoTriangulo(self):
        if self.ladoA == self.ladoB and self.ladoA == self.ladoC:
            return "equilátero"
        if self.ladoA != self.ladoB and self.ladoA != self.ladoC:
            return "escaleno"
        return "isósceles"


t = Triangulo(5, 5, 5)

if Triangulo.ehTriangulo(t) == True:
    print(Triangulo.calcularPerimetro(t))
    print(Triangulo.obterMaiorLado(t))
    print(Triangulo.informaTipoTriangulo(t))
else:
    print("ERRO! Não é um triângulo")

