from controlador.controlador_abstrato import ControladorAbstrato
from tela.tela_cliente import TelaCliente
from entidade.cliente import Cliente


class ControladorCliente(ControladorAbstrato):
    def __init__(self):
        self.__clientes = []
        self.__tela = TelaCliente()

    def inicia(self):
        opcoes = {"1": self.cadastro, "2": self.alterar, "3": self.remover, "4": self.listar}
        while True:
            opcao = self.__tela.opcoes()
            if opcao == "0":
                break
            if opcao in opcoes.keys():
                opcoes[opcao]()
            else:
                self.__tela.mensagem_erro("Comando Inválido")

    def cadastro(self):
        while True:
            dados = self.__tela.dados_cliente()
            if not self.verificar_dados(dados):
                continue
            for cliente in self.__clientes:
                if cliente.cpf == int(dados["cpf"]):
                    self.__tela.mensagem_erro("Cpf duplicado")
                    continue
            cliente = Cliente(dados["nome"], int(dados["cpf"]), int(dados["contato"]), dados["visto"])
            self.__clientes.append(cliente)
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
        dados = {"nome": cliente.nome, "cpf": cliente.cpf, "contato": cliente.contato, "visto": cliente.visto}
        return dados

    def seleciona_cliente(self):
        cpf = self.__tela.seleciona()
        for cliente in self.__clientes:
            if cliente.cpf == int(cpf):
                return cliente

    def seleciona_cliente_externo(self, cpf):
        for cliente in self.__clientes:
            if cliente.cpf == int(cpf):
                return cliente

    def alterar(self):
        cliente = self.seleciona_cliente()
        if isinstance(cliente, Cliente):
            self.__tela.mostra_cliente(self.dados_cliente(cliente))
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
            self.__tela.mostra_cliente(self.dados_cliente(cliente))
            confirmacao = self.__tela.confirma_exclusao()
            if confirmacao == "0":
                for i in range(len(self.__clientes)):
                    if self.__clientes[i] == cliente:
                        self.__clientes.pop(i)
                        self.__tela.mensagem("Exclusão realizada com sucesso")
                        break
            else:
                self.__tela.mensagem("Exclusão cancelada com sucesso")
        else:
            self.__tela.mensagem_erro("Cliente não encontrado")

    def listar(self):
        for cliente in self.__clientes:
            self.__tela.mostra_cliente(self.dados_cliente(cliente))
