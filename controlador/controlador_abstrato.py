from abc import ABC, abstractmethod

class ControladorAbstrato(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def inicia():
        pass
