import PySimpleGUI as sg
from tela.tela_abstrata import TelaAbstrata


class TelaCliente(TelaAbstrata):
    def __init__(self):
        self.__window = None
        self.init_opcoes()
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    def close(self):
        self.__window.Close()
    
    def init_opcoes(self):
    #sg.theme_previewer()
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ CLIENTE ------ ', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Cadastrar', "RD1", key='1')],
        [sg.Radio('Alterar (cadastre-se)', "RD1", key='2')],
        [sg.Radio('Remover', "RD1", key='3')],
        [sg.Radio('Listar', "RD1", key='4')],
        [sg.Radio('Voltar', "RD1", key='0')],
        [sg.Button('Confirmar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
    
    def opcoes(self):
        self.init_opcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        # cobre os casos de Retornar, fechar janela, ou clicar cancelar
        #Isso faz com que retornemos a tela do sistema caso qualquer uma dessas coisas aconteca
        if values['0']:
            opcao = 0
        self.close()
        return opcao
    
    def dados_cliente(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ CADASTRAR CLIENTE ------ ', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(8, 1)), sg.InputText('', key='nome')],
        [sg.Text('CPF:', size=(8, 1)), sg.InputText('', key='cpf')],
        [sg.Text('Contato:', size=(8, 1)), sg.InputText('', key='contato')],
        [sg.Text('Tem visto? :', size=(8, 1)), sg.InputText('', key='visto')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        
        nome = values['nome']
        cpf = values['cpf']
        contato = values['contato']
        visto = values['visto']
        if button in (None, 'Cancelar'):
            self.close()
            return None

        self.close()
        return {"nome": nome,"cpf":cpf, "contato": contato, "visto":visto}
    
    def tem_visto(self, dados_visto: str = "") -> bool:
        possui_visto = dados_visto.strip().lower()
        if possui_visto in ["s", "sim","sm"]:
            return True
        return False
            
    
    def dados_alterar(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ ALTERAR CLIENTE ------ ', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Text('Nome:', size=(8, 1)), sg.InputText('', key='nome')],
        [sg.Text('Contato:', size=(8, 1)), sg.InputText('', key='contato')],
        [sg.Text('Tem visto? :', size=(8, 1)), sg.InputText('', key='visto')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        
        nome = values['nome']
        contato = values['contato']
        visto = values['visto']
        if button in (None, 'Cancelar'):
            self.close()
            return None

        self.close()
        return {"nome": nome, "contato": contato, "visto":visto}
    
    
    def seleciona(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ SELECIONAR CLIENTE ------ ', font=("Helvica", 25))],
        [sg.Text('CPF:', size=(8, 1)), sg.InputText('', key='cpf')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        button, values = self.open()
        cpf = values['cpf']
        if button in (None, 'Cancelar'):
            self.close()
            return None
        self.close()
        return cpf
    
    def confirma_exclusao_opcoes(self, dados_cliente):
        data = [
            ["NOME: ", dados_cliente["nome"]],
            ["CPF: ", dados_cliente["cpf"]],
            ["CONTATO: ", dados_cliente["contato"]],
            ["VISTO: ", self.mostrar_visto(dados_cliente["visto"])]
        ]
        header = ["Dados","Cliente"]
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
            [sg.Text(' ------ CONFIRMAR EXCLUSÃO ------ ', font=("Helvetica", 25))],
            [sg.Table(values=data, headings=header,pad=((200, 200), (0, 0)), alternating_row_color='DarkSlateGray', justification='center')],
            [sg.Button('Confirmar', pad=((200,20),(0, 0)), button_color=('white', 'black')), sg.Cancel('Cancelar', pad=((30,100),(0, 0)),button_color=('white', 'black'))]
        ]
        self.__window  = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        button, values = self.open()
        self.close()
        return button
        
    
        
    def mostra_cliente(self, dados_cliente):
        data = []

        for cliente in dados_cliente:
            cliente_data = [
                ["NOME: ", cliente["nome"]],
                ["CPF: ", cliente["cpf"]],
                ["CONTATO: ", cliente["contato"]],
                ["VISTO: ", self.mostrar_visto(cliente["visto"])],
                ["#####################"],
                ["\n"]
            ]
            data.extend(cliente_data)
        header = ["Dados","Cliente"]
        sg.ChangeLookAndFeel('DarkBlue')

        layout = [
            [sg.Text(' ------ Listar ------ ', pad=((100, 100), (0, 0)),justification='center', font=("Helvetica", 25))],
            [sg.Table(values=data, headings=header, pad=((100, 100), (0, 0)),  alternating_row_color='DarkSlateGray',justification='center')],
            [sg.Cancel('Voltar',  pad=((200, 200), (0, 0)),button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        self.close()
        
        
    def mostrar_visto(self, dados):
        if self.tem_visto(dados):
            return 'Sim'
        else:
            return 'Não'

        
