from controlador.controlador_abstrato import ControladorAbstrato
from tela.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario


class ControladorFuncionario(ControladorAbstrato):
    def __init__(self):
        self.__funcionarios = []
        self.__tela = TelaFuncionario()

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
            dados = self.__tela.dados_funcionario()
            if not self.verificar_dados(dados):
                continue
            for funcionario in self.__funcionarios:
                if funcionario.matricula == int(dados["matricula"]):
                    self.__tela.mensagem_erro("Matricula duplicado")
                    continue
            funcionario = Funcionario(dados["nome"], int(dados["matricula"]), int(dados["contato"]))
            self.__funcionarios.append(funcionario)
            self.__tela.mensagem("cadastro realizada com sucesso")
            break

    def verificar_dados(self, dados):
        if dados["nome"].strip() == "":
            self.__tela.mensagem_erro("Nome não pode estar vazio")
            return False
        if not self.verifica_matricula(dados["matricula"]):
            self.__tela.mensagem_erro("Matricula Invalido")
            return False
        if not dados["contato"].isnumeric():
            self.__tela.mensagem_erro("Contato Invalido")
            return False
        return True

    def verifica_matricula(self, matricula):
        return True

    def dados_funcionario(self, funcionario):
        dados = {"nome": funcionario.nome, "matricula": funcionario.matricula, "contato": funcionario.contato, }
        return dados

    def seleciona_funcionario(self):
        matricula = self.__tela.seleciona()
        for funcionario in self.__funcionarios:
            if funcionario.matricula == int(matricula):
                return funcionario

    def alterar(self):
        funcionario = self.seleciona_funcionario()
        if isinstance(funcionario, Funcionario):
            self.__tela.mostra_funcionario(self.dados_funcionario(funcionario))
            while True:
                dados = self.__tela.dados_alterar()
                dados["matricula"] = funcionario.matricula
                if not self.verificar_dados(dados):
                    continue
                funcionario.nome = dados["nome"]
                funcionario.contato = dados["contato"]
                self.__tela.mensagem("Alteração realizada com sucesso")
                break
        else:
            self.__tela.mensagem_erro("Funcionario não encontrado")

    def remover(self):
        funcionario = self.seleciona_funcionario()
        if isinstance(funcionario, Funcionario):
            self.__tela.mostra_funcionario(self.dados_funcionario(funcionario))
            confirmacao = self.__tela.confirma_exclusao()
            if confirmacao == "0":
                for i in range(len(self.__funcionarios)):
                    if self.__funcionarios[i] == funcionario:
                        self.__funcionarios.pop(i)
                        self.__tela.mensagem("Exclusão realizada com sucesso")
                        break
            else:
                self.__tela.mensagem("Exclusão cancelada com sucesso")
        else:
            self.__tela.mensagem_erro("Funcionario não encontrado")

    def listar(self):
        for funcionario in self.__funcionarios:
            self.__tela.mostra_funcionario(self.dados_funcionario(funcionario))
