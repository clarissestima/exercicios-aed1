class Pessoa:
    def __init__(self, nome, data, altura):
        self.__nome = nome 
        self.__data = data
        self.__altura = altura
    
    def setNome(self, nome):
        self.__nome = nome

    def setData(self, data):
        self.__data = data

    def setAltura(self, altura):
        self.__altura = altura
    
    def getNome(self):
        return self.__nome

    def getData(self):
        return self.__data

    def getAltura(self):
        return self.__altura
    
    def getPessoa(self):
        return self.__nome, self.__data, self.__altura
    
    def getIdade(self):
        ano = " "
        for i in range (4):
            ano += self.__data[i + 6]
        return 2023 - int(ano)
    
p = Pessoa("Nairo", "02/06/2000", "1,75m")
print(Pessoa.getIdade(p))