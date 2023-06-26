from persistencia.dao_abstrato import DAO
from entidade.viagem import Viagem

class ViagemDAO(DAO):
    def __init__(self):
        super().__init__('viagens.pkl')
    
    def add(self, viagem: Viagem):
        if(isinstance(viagem.codigo, int)) and (viagem is not None) and isinstance(viagem, Viagem):
            super().add(viagem.codigo, viagem)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
