from persistencia.dao_abstrato import DAO
from entidade.funcionario import Funcionario

class FuncionarioDAO(DAO):
    def __init__(self):
        super().__init__('funcionarios.pkl')
    
    def add(self, funcionario: Funcionario):
        if(isinstance(funcionario.matricula, int)) and (funcionario is not None) and isinstance(funcionario, Funcionario):
            super().add(funcionario.matricula, funcionario)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)
    
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
