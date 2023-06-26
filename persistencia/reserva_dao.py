from persistencia.dao_abstrato import DAO
from entidade.reserva import Reserva

class ReservaDAO(DAO):
    def __init__(self):
        super().__init__('reservas.pkl')
    
    def add(self, reserva: Reserva):
        if(isinstance(reserva.codigo, int)) and (reserva is not None) and isinstance(reserva, Reserva):
            super().add(reserva.codigo, reserva)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
