from entidade.cliente import Cliente
from entidade.viagem import Viagem
from datetime import datetime


class Reserva:
    def __init__(self, codigo: int, cliente: Cliente, nome_cliente: str, viagem: Viagem, pais: str, origem: str,
                 destino: str, descricao: str, ida: datetime, volta: datetime, data_reserva: datetime, qtd_vagas: int,
                 n_pessoas: int, preco_unitario: float, tipo: str, visto: bool, valor_final: float):
        self.__codigo = codigo
        self.__cliente = cliente
        self.__nome_cliente = nome_cliente
        self.__viagem = viagem
        self.__pais = pais
        self.__origem = origem
        self.__destino = destino
        self.__descricao = descricao
        self.__ida = ida
        self.__volta = volta
        self.__data_reserva = data_reserva
        self.__qtd_vagas = qtd_vagas
        self.__n_pessoas = n_pessoas
        self.__preco_unitario = preco_unitario
        self.__tipo = tipo
        self.__visto = visto
        self.__valor_final = valor_final

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, valor):
        self.__codigo = valor

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, valor):
        self.__cliente = valor

    @property
    def nome_cliente(self):
        return self.__nome_cliente

    @nome_cliente.setter
    def nome_cliente(self, nome_cliente):
        self.__nome_cliente = nome_cliente

    @property
    def viagem(self):
        return self.__viagem

    @viagem.setter
    def viagem(self, valor):
        self.__viagem = valor

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, valor):
        self.__pais = valor

    @property
    def origem(self):
        return self.__origem

    @origem.setter
    def origem(self, valor):
        self.__origem = valor

    @property
    def destino(self):
        return self.__destino

    @destino.setter
    def destino(self, valor):
        self.__destino = valor

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, valor):
        self.__descricao = valor

    @property
    def ida(self):
        return self.__ida

    @ida.setter
    def ida(self, valor):
        self.__ida = valor

    @property
    def volta(self):
        return self.__volta

    @volta.setter
    def volta(self, valor):
        self.__volta = valor

    @property
    def data_reserva(self):
        return self.__data_reserva

    @data_reserva.setter
    def data_reserva(self, valor):
        self.__data_reserva = valor

    @property
    def qtd_vagas(self):
        return self.__qtd_vagas

    @qtd_vagas.setter
    def qtd_vagas(self, valor):
        self.__qtd_vagas = valor

    @property
    def n_pessoas(self):
        return self.__n_pessoas

    @n_pessoas.setter
    def n_pessoas(self, valor):
        self.__n_pessoas = valor

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, valor):
        self.__preco_unitario = valor

    @property
    def tipo(self):
        return self.__tipo

    @tipo.setter
    def tipo(self, valor):
        self.__tipo = valor

    @property
    def visto(self):
        return self.__visto

    @visto.setter
    def visto(self, valor):
        self.__visto = valor

    @property
    def valor_final(self):
        return self.__valor_final

    @valor_final.setter
    def valor_final(self, valor):
        self.__valor_final = valor

