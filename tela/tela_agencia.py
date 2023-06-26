import PySimpleGUI as sg
from tela.tela_abstrata import TelaAbstrata

class TelaAgencia(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    
    
    def init_opcoes(self):
    #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ Agência de Viagem ------ ', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Cliente (cadastre-se)', "RD1", key='1')],
        [sg.Radio('Funcionario (cadastre-se)', "RD1", key='2')],
        [sg.Radio('Acessar', "RD1", key='3')],
        [sg.Radio('Finalizar Sistema', "RD1", key='0')],
        [sg.Button('Confirmar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
    
    def opcoes(self):   
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0']:
            opcao = 0
        self.close()
        return opcao
    
    
    
    def acessar_opcoes(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ Agência de Viagem ------ ', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Sou Cliente', "RD1", key='1')],
        [sg.Radio('Sou Funcionario', "RD1", key='2')],
        [sg.Radio('Voltar', "RD1", key='0')],
        [sg.Button('Confirmar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
    
    
    def acessar(self):
        self.acessar_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0']:
            opcao = 0
        self.close()
        return opcao

    
    def tela_agencia_cliente_opcoes(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ AGÊNCIA DE VIAGEM - CLIENTE ------ ', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Listar viagens disponíveis', "RD1", key='1')],
        [sg.Radio('Reservar', "RD1", key='2')],
        [sg.Radio('Listar Reservas', "RD1", key='3')],
        [sg.Radio('Voltar', "RD1", key='0')],
        [sg.Button('Confirmar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
    
    def tela_agencia_cliente(self):
        self.tela_agencia_cliente_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0']:
            opcao = 0
        self.close()
        return opcao

    
    def total_vendas(self,total):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ TOTAL DE VENDAS ------ ', font=("Helvica", 25))],
        [sg.Text(f'TOTAL DE VENDAS:  R$ {total}', font=("Helvica", 15))],        
        [sg.Cancel('Voltar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        self.close()
    
    def tela_agencia_funcionario_opcoes(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ AGÊNCIA DE VIAGEM - FUNCIONARIO ------ ', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Cadastrar Viagem', "RD1", key='1')],
        [sg.Radio('Listar Reserva', "RD1", key='2')],
        [sg.Radio('Total de vendas', "RD1", key='3')],
        [sg.Radio('Voltar', "RD1", key='0')],
        [sg.Button('Confirmar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
    
    def tela_agencia_funcionario(self):
        self.tela_agencia_funcionario_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0']:
            opcao = 0
        self.close()
        return opcao

    
    
