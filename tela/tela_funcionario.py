import PySimpleGUI as sg
from tela.tela_abstrata import TelaAbstrata


class TelaFuncionario(TelaAbstrata):
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
        [sg.Text(' ------ FUNCIONÁRIO ------ ', font=("Helvica", 25))],
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

    
    def dados_funcionario(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ CADASTRAR FUNCIONÁRIO ------ ', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Text('Nome:', size=(10, 1)), sg.InputText('', key='nome')],
        [sg.Text('MATRICULA:', size=(10, 1)), sg.InputText('', key='matricula')],
        [sg.Text('Contato:', size=(10, 1)), sg.InputText('', key='contato')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        
        nome = values['nome']
        matricula = values['matricula']
        contato = values['contato']
        if button in (None, 'Cancelar'):
            self.close()
            return None

        self.close()
        
        return {"nome": nome,"matricula":matricula, "contato": contato}
    
    def dados_alterar(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ CADASTRAR FUNCIONÁRIO ------ ', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Text('Nome:', size=(8, 1)), sg.InputText('', key='nome')],
        [sg.Text('Contato:', size=(8, 1)), sg.InputText('', key='contato')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        
        nome = values['nome']
        contato = values['contato']
        if button in (None, 'Cancelar'):
            self.close()
            return None

        self.close()
        return {"nome": nome, "contato": contato}
    
    
    def seleciona(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ SELECIONAR FUNCIONÁRIO ------ ', font=("Helvica", 25))],
        [sg.Text('Matricula:', size=(8, 1)), sg.InputText('', key='matricula')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        button, values = self.open()
        matricula = values['matricula']
        if button in (None, 'Cancelar'):
            self.close()
            return None
        self.close()
    
        return matricula
    
    def confirma_exclusao_opcoes(self,dados_funcionario):
        data = [
            ["NOME: ", dados_funcionario["nome"]],
            ["MATRICULA: ", dados_funcionario["matricula"]],
            ["CONTATO: ", dados_funcionario["contato"]]
        ]
        header = ["Dados","Funcionário"]
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
        

    def mostra_funcionario(self, dados_funcionario):
        data = []

        for funcionario in dados_funcionario:
            funcionario_data = [
                ["NOME: ", funcionario["nome"]],
                ["MATRICULA: ", funcionario["matricula"]],
                ["CONTATO: ", funcionario["contato"]],
                ["#####################"],
                ["\n"]
            ]
            data.extend(funcionario_data)
        header = ["Dados","Funcionário"]
        sg.ChangeLookAndFeel('DarkBlue')

        layout = [
            [sg.Text(' ------ Listar ------ ', pad=((100, 0), (0, 0)),justification='center', font=("Helvetica", 25))],
            [sg.Table(values=data, headings=header, pad=((80, 0), (0, 0)),  alternating_row_color='DarkSlateGray',justification='center')],
            [sg.Cancel('Voltar',  pad=((200, 200), (0, 0)),button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        if button in (None, 'Voltar'):
            self.close()
            return None
        self.close()
        
        
        
