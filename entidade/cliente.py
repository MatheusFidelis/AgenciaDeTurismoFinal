from entidade.pessoa import Pessoa

class Cliente(Pessoa):
    def __init__(self, nome: str, cpf: int, contato: int, visto=False):
        super().__init__(nome, contato)
        self.__cpf = cpf
        self.__visto = visto

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

    @property
    def visto(self):
        return self.__visto

    @visto.setter
    def visto(self, visto):
        self.__visto = visto