from abc import abstractmethod, ABC
import PySimpleGUI as sg

class TelaAbstrata(ABC):
    @abstractmethod
    def __init__():
        pass

    '''def le_num_inteiro(self, mensagem: str = "", inteiros_validos: list = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print(self.mensagem_erro("Valor numérico incorreto"))
                if inteiros_validos:
                    print("Valores validos:", inteiros_validos)'''
        
    
    def mensagem(self, msg):
        sg.popup(f"----- {msg} -----")
    
    def mensagem_erro(self, msg):
        sg.popup(f"### {msg} ###")
