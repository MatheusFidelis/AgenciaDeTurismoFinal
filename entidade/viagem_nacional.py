from entidade.viagem import Viagem


class ViagemNacional(Viagem):
    def __init__(self,  codigo, pais_origem, pais_destino, descricao, data_ida, data_volta,  preco, qtd_vagas, tipo, estado_origem: str, estado_destino: str,):
        super().__init__(codigo, pais_origem, pais_destino, descricao, data_ida, data_volta,  preco, qtd_vagas, tipo)
        self.__estado_origem = estado_origem
        self.__estado_destino = estado_destino
    
    @property
    def estado_origem(self):
        return self.__estado_origem
    
    @estado_origem.setter
    def estado_origem(self, estado_origem: str):
        self.__estado_origem = estado_origem
    
    
    @property
    def estado_destino(self):
        return self.__estado_destino
    
    @estado_destino.setter
    def estado_destino(self, estado_destino: str):
        self.__estado_destino = estado_destino
