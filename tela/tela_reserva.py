import PySimpleGUI as sg
from tela.tela_abstrata import TelaAbstrata
import datetime

class TelaReserva(TelaAbstrata):
    def __init__(self):
        self.__window = None
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
    
    def mostrar_reserva(self,dados):
        data = []

        for reserva in dados:
            reserva_data = [
                ["Codigo: ", reserva["codigo"]],
                ["Cliente: ", reserva["nome_cliente"]],
                ["País: ", reserva["pais"]],
                ["Origem: ", reserva["origem"]],
                ["Destino: ", reserva["destino"]],
                ["Descrição: ", reserva["descricao"]],
                ["Ida: ", reserva["ida"]],
                ["Volta: ", reserva["volta"]],
                ["Data da Reserva: ", reserva["data_reserva"]],
                ["Número de Vagas: ", reserva["qtd_vagas"]],
                ["Número de Vagas Preenchidas: ", reserva["n_pessoas"]],
                ["Preço Unitario: ", reserva["preco_unitario"]],
                ["Total: ", reserva["valor_final"]],
                ["#####################"],
                ["\n"]
            ]
            data.extend(reserva_data)
        header = ["Dados","Reserva"]
        sg.ChangeLookAndFeel('DarkBlue')

        layout = [
            [sg.Text(' ------ Listar ------ ', pad=((150, 100), (0, 0)),justification='center', font=("Helvetica", 25))],
            [sg.Table(values=data, headings=header, pad=((100, 100), (0, 0)),  alternating_row_color='DarkSlateGray',justification='center')],
            [sg.Cancel('Voltar',  pad=((250, 50), (0, 0)),button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        if button in (None, 'Voltar'):
            self.close()
            return None
        self.close()
        
    
    def dados_reserva(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ RESERVA ------ ',pad=((100, 100), (0, 0)),justification='center', font=("Helvica", 25))],
        [sg.Text('Codigo da viagem:', size=(15, 1)), sg.InputText('', key='viagem')],
        [sg.Text('Cpf do cliente:', size=(15, 1)), sg.InputText('', key='cliente')],
        [sg.Text('Quantas pessoas:', size=(15, 1)), sg.InputText('', key='n_pessoas')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        
        codigo = int
        cliente = values['cliente']
        nome_cliente = str
        viagem = values['viagem']
        pais = str
        origem = str
        destino = str
        descricao = str
        ida = datetime
        volta = datetime
        data_reserva = datetime
        qtd_vagas = None
        n_pessoas = values['n_pessoas']
        preco_unitario = float
        tipo = str
        visto = False
        valor_final = float
        if button in (None, 'Cancelar'):
            self.close()
            return None

        self.close()
        
        return {"codigo": codigo, "cliente": cliente,"nome_cliente":nome_cliente, "viagem": viagem,"pais":pais, "origem":origem, "destino":destino ,"descricao":descricao, "ida":ida, "volta":volta,"data_reserva": data_reserva, "qtd_vagas":qtd_vagas,"n_pessoas": n_pessoas,"preco_unitario":preco_unitario,"tipo":tipo,"visto":visto,"valor_final": valor_final }
    
    def seleciona(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ SELECIONAR v ------ ', font=("Helvica", 25))],
        [sg.Text('codigo:', size=(8, 1)), sg.InputText('', key='codigo')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        button, values = self.open()
        codigo = values['codigo']
        if button in (None, 'Cancelar'):
            self.close()
            return None
        self.close()
        return codigo
