from controlador.controlador_abstrato import ControladorAbstrato
from tela.tela_funcionario import TelaFuncionario
from entidade.funcionario import Funcionario
from persistencia.funcionario_dao import FuncionarioDAO

class ControladorFuncionario(ControladorAbstrato):
    __instance = None
    def __init__(self):
        self.__dao = FuncionarioDAO()
        self.__tela = TelaFuncionario()
    
    def __new__(cls):
        if ControladorFuncionario.__instance is None:
            ControladorFuncionario.__instance = object.__new__(cls)
        return ControladorFuncionario.__instance
        
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
            dados = self.__tela.dados_funcionario()
            if dados is None:
                return self.encerra_sistema
            if not self.verificar_dados(dados):
                continue
            matricula_duplicada = False
            for funcionario in self.__dao.get_all():
                if funcionario.matricula == int(dados["matricula"]):
                    self.__tela.mensagem_erro("Matricula duplicado")
                    matricula_duplicada = True
                    continue
            if not matricula_duplicada:
                funcionario = Funcionario(dados["nome"], int(dados["matricula"]), int(dados["contato"] ) )
                self.__dao.add(funcionario)
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
    
    def dados_funcionario(self,funcionario):
        dados = {"nome": funcionario.nome,"matricula": funcionario.matricula,"contato": funcionario.contato,}
        return dados
    
    def seleciona_funcionario(self):
        matricula = self.__tela.seleciona()
        if matricula is None:
            return None
        for funcionario in self.__dao.get_all():
            if funcionario.matricula == int(matricula):
                return funcionario
    
    def alterar(self):
        funcionario = self.seleciona_funcionario()
        if isinstance (funcionario, Funcionario):
            
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
        if isinstance (funcionario, Funcionario):

            confirmacao = self.__tela.confirma_exclusao_opcoes(self.dados_funcionario(funcionario))
            if confirmacao == "Confirmar":
                self.__dao.remove(funcionario.cpf)
                self.__tela.mensagem("Exclusão realizada com sucesso")
            else:
                self.__tela.mensagem("Exclusão cancelada com sucesso")
        else:
            self.__tela.mensagem_erro("Funcionario não encontrado")
    
            
    def listar(self):
        dados_funcionarios = []

        for funcionario in self.__dao.get_all():
            dados_funcionario = self.dados_funcionario(funcionario)
            dados_funcionarios.append(dados_funcionario)

        self.__tela.mostra_funcionario(dados_funcionarios)
    
