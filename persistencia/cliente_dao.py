from persistencia.dao_abstrato import DAO
from entidade.cliente import Cliente

class ClienteDAO(DAO):
    def __init__(self):
        super().__init__('clientes.pkl')
    
    def add(self, cliente: Cliente):
        if(isinstance(cliente.cpf, int)) and (cliente is not None) and isinstance(cliente, Cliente):
            super().add(cliente.cpf, cliente)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
