from abc import ABC, abstractmethod
from datetime import datetime

class Viagem(ABC):
    @abstractmethod
    def __init__(self, codigo: int, pais_origem: str, pais_destino: str,descricao: str, data_ida: datetime, data_volta: datetime,  preco: float, qtd_vagas: int, tipo: str):
        self.__codigo = codigo
        self.__pais_origem = pais_origem
        self.__pais_destino = pais_destino
        self.__descricao = descricao
        self.__data_ida = data_ida
        self.__data_volta = data_volta
        self.__preco = preco
        self.__qtd_vagas = qtd_vagas
        self.__tipo =  tipo
    
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self, codigo:int):
        self.__codigo = codigo
        
    
    @property
    def pais_origem(self):
        return self.__pais_origem
    
    @pais_origem.setter
    def pais_origem(self, pais_origem: str):
        self.__pais_origem = pais_origem
    
    
    @property
    def pais_destino(self):
        return self.__pais_destino
    
    @pais_destino.setter
    def pais_destino(self, pais_destino: str):
        self.__pais_destino = pais_destino
    
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao:str):
        self.__descricao = descricao
    
    @property
    def data_ida(self):
        return self.__data_ida
    
    @data_ida.setter
    def data_ida(self, data_ida:datetime):
        self.__data_ida = data_ida
    
    @property
    def data_volta(self):
        return self.__data_volta
    
    @data_volta.setter
    def data_volta(self, data_volta:datetime):
        self.__data_volta = data_volta
        
    
    @property
    def preco(self):
        return self.__preco
    
    @preco.setter
    def preco(self, preco:float):
        self.__preco = preco
        
    
    @property
    def qtd_vagas(self):
        return self.__qtd_vagas
    
    @qtd_vagas.setter
    def qtd_vagas(self, qtd_vagas:int):
        self.__qtd_vagas = qtd_vagas
        
    
    @property
    def tipo(self):
        return self.__tipo
    
    @tipo.setter
    def tipo(self, tipo:str):
        self.__tipo = tipo
