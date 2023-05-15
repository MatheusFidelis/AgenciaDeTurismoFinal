from entidade.pessoa import Pessoa

class Funcionario(Pessoa):
    def __init__(self, nome: str, matricula: int, contato: int):
        super().__init__(nome, contato)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
