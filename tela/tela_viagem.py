import PySimpleGUI as sg
from tela.tela_abstrata import TelaAbstrata

class TelaViagem(TelaAbstrata):
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
        [sg.Text(' ------ VIAGEM ------ ', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Cadastrar', "RD1", key='1')],
        [sg.Radio('Alterar ', "RD1", key='2')],
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
    
    def seleciona_viagem(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ SELECIONAR VIAGEM ------ ', font=("Helvica", 25))],
        [sg.Text('Código:', size=(8, 1)), sg.InputText('', key='codigo')],
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
    
    def tipo_da_viagem_opcoes(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ TIPO DE VIAGEM ------ ', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Nacional', "RD1", key='1')],
        [sg.Radio('Intercional ', "RD1", key='2')],
        [sg.Radio('Voltar', "RD1", key='0')],
        [sg.Button('Confirmar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
    
    def tipo_da_viagem(self):
        self.tipo_da_viagem_opcoes()
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
        
    def dados_internacional(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ VIAGEM INTERNACIONA ------ ', font=("Helvica", 25))],
        [sg.Text('Código: ', size=(15, 1)), sg.InputText('', key='codigo')],
        [sg.Text('País de Origem: ', size=(15, 1)), sg.InputText('', key='pais_origem')],
        [sg.Text('País de Destino: ', size=(15, 1)), sg.InputText('', key='pais_destino')],
        [sg.Text('Descricao: ', size=(15, 1)), sg.InputText('', key='descricao')],
        [sg.Text('Data Ida DD-MM-YYYY: ', size=(15, 1)), sg.InputText('', key='data_ida')],
        [sg.Text('Data Volta DD-MM-YYYY: ', size=(15, 1)), sg.InputText('', key='data_volta')],
        [sg.Text('Preço do pacote: ', size=(15, 1)), sg.InputText('', key='preco')],
        [sg.Text('Quantidade de Vagas:', size=(15, 1)), sg.InputText('', key='qtd_vagas')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        
        codigo = values['codigo']
        pais_origem = values['pais_origem']
        pais_destino = values['pais_destino']
        descricao = values['descricao']
        data_ida = values['data_ida']
        data_volta = values['data_volta']
        preco = values['preco']
        qtd_vagas = values['qtd_vagas']
        tipo = 'INTERNACIONAL'
        visto = True
        
        if button in (None, 'Cancelar'):
            self.close()
            return None

        self.close()
        
        return {"codigo":codigo,"origem": pais_origem,"destino": pais_destino, "descricao": descricao,"data_ida":data_ida, "data_volta":data_volta, "preco":preco, "qtd_vagas":qtd_vagas, "tipo":tipo, "visto":visto}
    
        
    def alterar_internacional(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ ALTERAR VIAGEM INTERNACIONA ------ ', font=("Helvica", 25))],
        [sg.Text('País de Origem: ', size=(15, 1)), sg.InputText('', key='pais_origem')],
        [sg.Text('País de Destino: ', size=(15, 1)), sg.InputText('', key='pais_destino')],
        [sg.Text('Descricao: ', size=(15, 1)), sg.InputText('', key='descricao')],
        [sg.Text('Data Ida DD-MM-YYYY: ', size=(15, 1)), sg.InputText('', key='data_ida')],
        [sg.Text('Data Volta DD-MM-YYYY: ', size=(15, 1)), sg.InputText('', key='data_volta')],
        [sg.Text('Preço do pacote: ', size=(15, 1)), sg.InputText('', key='preco')],
        [sg.Text('Quantidade de Vagas:', size=(15, 1)), sg.InputText('', key='qtd_vagas')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        
        pais_origem = values['pais_origem'].title()
        pais_destino = values['pais_destino'].title()
        descricao = values['descricao']
        data_ida = values['data_ida']
        data_volta = values['data_volta']
        preco = values['preco']
        qtd_vagas = values['qtd_vagas']
        tipo = 'INTERNACIONAL'
        visto = True
        
        if button in (None, 'Cancelar'):
            self.close()
            return None

        self.close()
        
        
        return {"origem": pais_origem,"destino": pais_destino, "descricao": descricao,"data_ida":data_ida, "data_volta":data_volta, "preco":preco, "qtd_vagas":qtd_vagas, "tipo":tipo,"visto":visto}
    
    
    def dados_nacional(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ VIAGEM INTERNACIONA ------ ', font=("Helvica", 25))],
        [sg.Text('Código: ', size=(15, 1)), sg.InputText('', key='codigo')],
        [sg.Text('País de Origem: ', size=(15, 1)), sg.InputText('', key='pais_origem')],
        [sg.Text('País de Destino: ', size=(15, 1)), sg.InputText('', key='pais_destino')],
        [sg.Text('Descricao: ', size=(15, 1)), sg.InputText('', key='descricao')],
        [sg.Text('Data Ida DD-MM-YYYY: ', size=(15, 1)), sg.InputText('', key='data_ida')],
        [sg.Text('Data Volta DD-MM-YYYY: ', size=(15, 1)), sg.InputText('', key='data_volta')],
        [sg.Text('Preço do pacote: ', size=(15, 1)), sg.InputText('', key='preco')],
        [sg.Text('Quantidade de Vagas:', size=(15, 1)), sg.InputText('', key='qtd_vagas')],
        [sg.Text('Estado de Origem: ', size=(15, 1)), sg.InputText('', key='estado_origem')],
        [sg.Text('Estado de Destino: ', size=(15, 1)), sg.InputText('', key='estado_destino')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        
        codigo = values['codigo']
        pais_origem = values['pais_origem'].title()
        pais_destino = values['pais_destino'].title()
        descricao = values['descricao']
        data_ida = values['data_ida']
        data_volta = values['data_volta']
        preco = values['preco']
        qtd_vagas = values['qtd_vagas']
        tipo = 'NACIONAL'
        estado_origem = values['estado_origem']
        estado_destino = values['estado_destino']
        
        if button in (None, 'Cancelar'):
            self.close()
            return None

        self.close()
        
        return {"codigo":codigo,"origem": pais_origem,"destino": pais_destino, "descricao": descricao,"data_ida":data_ida, "data_volta":data_volta, "preco":preco, "qtd_vagas":qtd_vagas, "tipo":tipo,"estado_origem": estado_origem, "estado_destino": estado_destino}
    
    def alterar_nacional(self):
        sg.ChangeLookAndFeel('DarkBlue')
        layout = [
        [sg.Text(' ------ VIAGEM INTERNACIONA ------ ', font=("Helvica", 25))],
        [sg.Text('País de Origem: ', size=(15, 1)), sg.InputText('', key='pais_origem')],
        [sg.Text('País de Destino: ', size=(15, 1)), sg.InputText('', key='pais_destino')],
        [sg.Text('Descricao: ', size=(15, 1)), sg.InputText('', key='descricao')],
        [sg.Text('Data Ida DD-MM-YYYY: ', size=(15, 1)), sg.InputText('', key='data_ida')],
        [sg.Text('Data Volta DD-MM-YYYY: ', size=(15, 1)), sg.InputText('', key='data_volta')],
        [sg.Text('Preço do pacote: ', size=(15, 1)), sg.InputText('', key='preco')],
        [sg.Text('Quantidade de Vagas:', size=(15, 1)), sg.InputText('', key='qtd_vagas')],
        [sg.Text('Estado de Origem: ', size=(15, 1)), sg.InputText('', key='estado_origem')],
        [sg.Text('Estado de Destino: ', size=(15, 1)), sg.InputText('', key='estado_destino')],
        [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)
        
        button, values = self.open()
        
        pais_origem = values['pais_origem'].title()
        pais_destino = values['pais_destino'].title()
        descricao = values['descricao']
        data_ida = values['data_ida']
        data_volta = values['data_volta']
        preco = values['preco']
        qtd_vagas = values['qtd_vagas']
        tipo = 'NACIONAL'
        estado_origem = values['estado_origem']
        estado_destino = values['estado_destino']
        
        if button in (None, 'Cancelar'):
            self.close()
            return None

        self.close()
        
        return {"origem": pais_origem,"destino": pais_destino, "descricao": descricao,"data_ida":data_ida, "data_volta":data_volta, "preco":preco, "qtd_vagas":qtd_vagas, "tipo":tipo,"estado_origem": estado_origem, "estado_destino": estado_destino}
    
    def confirma_exclusao(self, dados_viagens):
        if dados_viagens["tipo"] == "INTERNACIONAL":
            viagem_data = [
                ["--- VIAGEM " + dados_viagens["tipo"] + " ---"],
                ["CÓDIGO: ", dados_viagens["codigo"]],
                ["ORIGEM: ", dados_viagens["origem"]],
                ["DESTINO: ", dados_viagens["destino"]],
                ["DESCRIÇÃO: ", dados_viagens["descricao"]],
                ["IDA: ", dados_viagens["data_ida"]],
                ["VOLTA: ", dados_viagens["data_volta"]],
                ["PREÇO: ", dados_viagens["preco"]],
                ["QUANTIDADE DE VAGAS: ", dados_viagens["qtd_vagas"]],
                ["TIPO: ", dados_viagens["tipo"]],
                ["\n"]
            ]
        elif dados_viagens["tipo"] == "NACIONAL":
            viagem_data = [
                ["--- VIAGEM " + dados_viagens["tipo"] + " ---"],
                ["CÓDIGO: ", dados_viagens["codigo"]],
                ["PAÍS: ", dados_viagens["origem"]],
                ["DESCRIÇÃO: ", dados_viagens["descricao"]],
                ["IDA: ", dados_viagens["data_ida"]],
                ["VOLTA: ", dados_viagens["data_volta"]],
                ["PREÇO: ", dados_viagens["preco"]],
                ["QUANTIDADE DE VAGAS: ", dados_viagens["qtd_vagas"]],
                ["TIPO: ", dados_viagens["tipo"]],
                ["ESTADO DE ORIGEM: ", dados_viagens["estado_origem"]],
                ["ESTADO DE DESTINO: ", dados_viagens["estado_destino"]],
                ["\n"]
            ]


        header = ["Dados", "Viagem"]
        sg.ChangeLookAndFeel('DarkBlue')

        layout = [
            [sg.Text(' ------ Listar ------ ', justification='center', font=("Helvetica", 25))],
            [sg.Table(values=viagem_data, headings=header, alternating_row_color='DarkSlateGray', justification='left')],
            [sg.Button('Confirmar', button_color=('white', 'black')), sg.Cancel('Cancelar', pad=((30,100),(0, 0)),button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)

        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        self.close()

        return button


    

    def mostrar_viagens(self, dados_viagens):
        data = []

        for viagem in dados_viagens:
            if viagem["tipo"] == "INTERNACIONAL":
                viagem_data = [
                    ["--- VIAGEM " + viagem["tipo"] + " ---"],
                    ["CÓDIGO: ", viagem["codigo"]],
                    ["ORIGEM: ", viagem.get("origem", "")],
                    ["DESTINO: ", viagem.get("destino", "")],
                    ["DESCRIÇÃO: ", viagem.get("descricao", "")],
                    ["IDA: ", viagem.get("data_ida", "")],
                    ["VOLTA: ", viagem.get("data_volta", "")],
                    ["PREÇO: ", viagem.get("preco", "")],
                    ["QUANTIDADE DE VAGAS: ", viagem.get("qtd_vagas", "")],
                    ["TIPO: ", viagem.get("tipo", "")],
                    ["\n"]
                ]
            elif viagem["tipo"] == "NACIONAL":
                viagem_data = [
                    ["--- VIAGEM " + viagem["tipo"] + " ---"],
                    ["CÓDIGO: ", viagem["codigo"]],
                    ["PAÍS: ", viagem.get("origem", "")],
                    ["DESCRIÇÃO: ", viagem.get("descricao", "")],
                    ["IDA: ", viagem.get("data_ida", "")],
                    ["VOLTA: ", viagem.get("data_volta", "")],
                    ["PREÇO: ", viagem.get("preco", "")],
                    ["QUANTIDADE DE VAGAS: ", viagem.get("qtd_vagas", "")],
                    ["TIPO: ", viagem.get("tipo", "")],
                    ["ESTADO DE ORIGEM: ", viagem.get("estado_origem", "")],
                    ["ESTADO DE DESTINO: ", viagem.get("estado_destino", "")],
                    ["\n"]
                ]
            data.extend(viagem_data)

        header = ["Dados", "Viagem"]
        sg.ChangeLookAndFeel('DarkBlue')

        layout = [
            [sg.Text(' ------ Listar ------ ', pad=((110, 0), (0, 0)), justification='center', font=("Helvetica", 25))],
            [sg.Table(values=data, headings=header, pad=((80, 0), (0, 0)), alternating_row_color='DarkSlateGray', justification='left')],
            [sg.Cancel('Voltar', pad=((200, 200), (0, 0)), button_color=('white', 'black'))]
        ]
        self.__window = sg.Window('AGÊNCIA DE VIAGEM').Layout(layout)

        button, values = self.open()
        if button in (None, 'Cancelar'):
            self.close()
            return None
        self.close()


    
    
