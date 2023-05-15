from entidade.viagem import Viagem

class ViagemInternacional(Viagem):
    def __init__(self, codigo, pais_origem, pais_destino,descricao, data_ida, data_volta,  preco, qtd_vagas, tipo,visto: bool):
        super().__init__(codigo, pais_origem, pais_destino,descricao, data_ida, data_volta,  preco, qtd_vagas, tipo)
        self.__visto = visto
        
    
    @property
    def visto(self):
        return self.__visto
    
    @visto.setter
    def visto(self, visto):
        self.__visto = visto
    
    
        
