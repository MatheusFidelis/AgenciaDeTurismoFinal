from controlador.controlador_abstrato import ControladorAbstrato
from tela.tela_cliente import TelaCliente
from entidade.cliente import Cliente
from persistencia.cliente_dao import ClienteDAO

class ControladorCliente(ControladorAbstrato):
    __instance = None
    def __init__(self):
        self.__dao = ClienteDAO()
        self.__tela = TelaCliente()
        

    def __new__(cls):
        if ControladorCliente.__instance is None:
            ControladorCliente.__instance = object.__new__(cls)
        return ControladorCliente.__instance
    
    def inicia(self):
        while True:
            opcao = self.__tela.opcoes()
            if opcao == 0:
                break
            elif opcao == 1:
                self.cadastro()
            elif opcao == 2:
                self.alterar()
            elif opcao == 3:
                self.remover()
            elif opcao == 4:
                self.listar()
    
    
    def encerra_sistema(self):
        exit(1)
    
    def cadastro(self):
        
        while True:
            dados = self.__tela.dados_cliente()
            if dados is None:
                return self.encerra_sistema
            if not self.verificar_dados(dados):
                continue
            cpf_duplicado = False
            for cliente in self.__dao.get_all():
                if cliente.cpf == int(dados["cpf"]):
                    self.__tela.mensagem_erro("Cpf duplicado")
                    cpf_duplicado = True
                    continue
            if not cpf_duplicado:
                cliente = Cliente(dados["nome"], int(dados["cpf"]), int(dados["contato"] ),dados["visto"] )
                self.__dao.add(cliente)
                self.__tela.mensagem("cadastro realizada com sucesso")
            break
            
    def verificar_dados(self, dados):
        if dados["nome"].strip() == "":
            self.__tela.mensagem_erro("Nome não pode estar vazio")
            return False
        if not self.verifica_cpf(dados["cpf"]):
            self.__tela.mensagem_erro("Cpf Invalido")
            return False
        if not dados["contato"].isnumeric():
            self.__tela.mensagem_erro("Contato Invalido")
            return False
        if dados["visto"] == None:
            self.__tela.mensagem_erro("Informe se possui visto")
            return False
        return True
    
    def verificar_dados_alterar(self, dados):
        if dados["nome"].strip() == "":
            self.__tela.mensagem_erro("Nome não pode estar vazio")
            return False
        if not dados["contato"].isnumeric():
            self.__tela.mensagem_erro("Telefone Invalido")
            return False
        if dados["visto"] == None:
            self.__tela.mensagem_erro("Informe se possui visto")
            return False
        return True
    
    
        
    def verifica_cpf(self, cpf):
        if len(cpf) == 0:
            print("Cpf Invalido! Está vazio.")
        else:
            try:
                valor_inteiro = int(cpf)
                if valor_inteiro != 0:
                    return True
                else:
                    print("O cpf não pode ser zero.")
            except ValueError:
                print("Cpf Invalido!")
    
    def dados_cliente(self, cliente):
        dados = {
            "nome": cliente.nome,
            "cpf": cliente.cpf,
            "contato": cliente.contato,
            "visto": cliente.visto
        }
        return dados
    
    def seleciona_cliente(self):
        cpf = self.__tela.seleciona()
        if cpf is None:
            return None
        for cliente in self.__dao.get_all():
            if cliente.cpf == int(cpf):
                return cliente
    
    def seleciona_cliente_externo(self,cpf):
        
        for cliente in self.__dao.get_all():
            if cliente.cpf == int(cpf):
                return cliente
    
    def alterar(self):
        cliente = self.seleciona_cliente()
        
        if isinstance (cliente, Cliente):
            
            while True:
                dados = self.__tela.dados_alterar()
                dados["cpf"] = cliente.cpf
                if not self.verificar_dados_alterar(dados):
                    continue
                cliente.nome = dados["nome"]
                cliente.contato = dados["contato"]
                cliente.visto = dados["visto"]
                self.__tela.mensagem("Alteração realizada com sucesso")
                break
        else:
            self.__tela.mensagem_erro("Cliente não encontrado")
        
        
    def remover(self):
        cliente = self.seleciona_cliente()
        
        if isinstance(cliente, Cliente):
            confirmacao = self.__tela.confirma_exclusao_opcoes(self.dados_cliente(cliente))
            if confirmacao == 'Confirmar':
                self.__dao.remove(cliente.cpf)
                self.__tela.mensagem("Exclusão realizada com sucesso")
            else:
                self.__tela.mensagem("Exclusão cancelada com sucesso")
        else:
            self.__tela.mensagem_erro("Cliente não encontrado")
    
            
    def listar(self):
        
        dados_clientes = []

        for cliente in self.__dao.get_all():
            dados_cliente = self.dados_cliente(cliente)
            dados_clientes.append(dados_cliente)

        self.__tela.mostra_cliente(dados_clientes)
    
