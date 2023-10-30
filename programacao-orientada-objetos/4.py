class Aluno:
    def __init__(self, nome, curso, tempo):
        self.__nome = nome
        self.__curso = curso
        self.__tempo_sem_dormir = tempo
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setCurso(self, curso):
        self.__curso = curso
    
    def setTempo(self, tempo):
        self.__tempo_sem_dormir = tempo
    
    def getNome(self):
        return self.__nome
    
    def getCurso(self):
        return self.__curso
    
    def getTempo(self):
        return self.__tempo_sem_dormir
    
    def estudar(self, horas_estudadas):
        self.__tempo_sem_dormir = self.__tempo_sem_dormir + horas_estudadas
    
    def dormir(self, horas_de_sono):
        if self.__tempo_sem_dormir > 0:
            self.__tempo_sem_dormir = self.__tempo_sem_dormir - horas_de_sono
        return "Já dormiu o suficiente"

aluno1 = Aluno("Clarsse", "Sistemas", 1)
aluno2 = Aluno("Nairo", "Sistemas", 6)

aluno1.estudar(5)
aluno2.estudar(10)

if aluno1.getTempo() > aluno2.getTempo():
    print(f"{aluno1.getNome()} está a mais tempo sem dormir")
else:
    print(f"{aluno2.getNome()} está a mais tempo sem dormir")