""" Implemente a classe Carro com os seguintes atributos:
Atributos privados: consumo de combustível (medido em km/litro) e
quantidade de combustível no tanque; o consumo é especificado no método
construtor e o nível de combustível inicial é 0.
Métodos públicos necessários para sets (atribuir) e gets (obter) os atributos;
Método andar(), que simule o ato de dirigir o veículo por uma certa distância,
reduzindo o nível de combustível no tanque de gasolina. Esse método recebe como
parâmetro a distância em km;
Método obterGasolina(), que retorna o nível atual de combustível;
Método adicionarGasolina(), para abastecer o tanque; informar a quantidade de
litros por parâmetro, e verificar eventuais inconsistências;
Faça um programa para testar a classe Carro. Exemplo de uso:
meuCarro = Carro(15); #consumo de 15 km/l.
meuCarro.adicionarGasolina(30); #abastece com 30 litros de
combustível.
meuCarro.andar(100); #anda 100 quilômetros.
print(meuCarro.obterGasolina()) #imprime o combustível que resta
no tanque."""

class Carro:
    def __init__(self, consumo):
        self.__consumo_de_combustivel = consumo
        self.__combustivel_no_tanque = 0
    
    def setConsumo(self, consumo):
        self.__consumo_de_combustivel = consumo

    def setGasolina(self, combustivel):
        self.__combustivel_no_tanque += combustivel
    
    def getConsumo(self):
        return self.__consumo_de_combustivel

    def getGasolina(self):
        return self.__combustivel_no_tanque
    
    def andar(self, distancia):
        gasta = distancia / self.__consumo_de_combustivel
        self.__combustivel_no_tanque += gasta
        

meuCarro = Carro(15); #consumo de 15 km/l.
meuCarro.setGasolina(30); #abastece com 30 litros de
meuCarro.andar(100); #anda 100 quilômetros.
print(meuCarro.getGasolina())