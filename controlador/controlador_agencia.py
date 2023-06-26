from datetime import datetime
from entidade.reserva import Reserva
from entidade.viagem_internacional import ViagemInternacional
from entidade.viagem_nacional import ViagemNacional
from entidade.funcionario import Funcionario
from tela.tela_agencia import TelaAgencia
from tela.tela_reserva import TelaReserva
from controlador.controlador_abstrato import ControladorAbstrato
from controlador.controlador_viagem import ControladorViagem
from controlador.controlador_funcionario import ControladorFuncionario
from controlador.controlador_cliente import ControladorCliente
from persistencia.reserva_dao import ReservaDAO

class ControladorAgencia(ControladorAbstrato):
    __instance = None
    def __init__(self):
        self.__dao = ReservaDAO()
        self.__tela_agencia = TelaAgencia()
        self.__tela_reserva = TelaReserva()
        self.__controlador_viagem = ControladorViagem()
        self.__controlador_funcionario = ControladorFuncionario()
        self.__controlador_cliente = ControladorCliente()
    
    def __new__(cls):
        if ControladorAgencia.__instance is None:
            ControladorAgencia.__instance = object.__new__(cls)
        return ControladorAgencia.__instance
        
    def inicia(self): 
        opcoes = {1: self.__controlador_cliente.inicia, 2: self.__controlador_funcionario.inicia, 3: self.acessar,
                        0: self.encerra_sistema}
        while True:
            opcao = self.__tela_agencia.opcoes()
            if opcao in opcoes.keys():
                opcoes[opcao]()
    
    
    def controlador_cliente(self):
        return self.__controlador_cliente
    
    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario
    
    
    
    @property
    def controlador_viagem(self):
        return self.__controlador_viagem
    
    def encerra_sistema(self):
        exit(1)
    
    def acessar(self):
        opcoes = {1: self.cliente, 2: self.funcionario, 0: self.inicia}
        while True:
            opcao_escolhida = self.__tela_agencia.acessar()
            funcao_escolhida = opcoes[opcao_escolhida]
            funcao_escolhida()
        

    
    def cliente(self):
        return self.agencia_cliente()

    
    def funcionario(self):
        return self.agencia_funcionario()

    def agencia_cliente(self):
        while True:
            opcao = self.__tela_agencia.tela_agencia_cliente()
            if opcao == 0:
                break
            if opcao == 1:
                self.listar_viagens_disp()
            elif opcao == 2:
                self.reservar()
            elif opcao == 3:
                self.listar_reservas_feitas()
            
        
    
    def listar_viagens_disp(self):
        self.__controlador_viagem.listar_viagens_com_vagas()


    
                    
    def seleciona_reserva(self):
        codigo = self.__tela_reserva.seleciona()
        for reserva in self.__dao.get_all():
            if reserva.codigo == int(codigo):
                return reserva
            
    def reservar(self):
        dados_reserva = self.__tela_reserva.dados_reserva()
        if dados_reserva is None:
                return self.encerra_sistema

        codigo = len(self.__dao.get_all()) + 1
        # Verificar se já existe uma reserva com o mesmo código
        if any(reserva.codigo == codigo for reserva in self.__dao.get_all()):
            codigo += 1
            return

        viagem = self.__controlador_viagem.seleciona_externo(codigo)
        if not viagem:
            self.__tela_reserva.mensagem_erro("Viagem não encontrada.")
            return
        
        cliente = dados_reserva["cliente"]
        cliente = self.__controlador_cliente.seleciona_cliente_externo(cliente)
        if not cliente:
            self.__tela_reserva.mensagem_erro("Cliente não encontrado.")
            return
        nome_cliente = cliente.nome         
        pais = viagem.pais_origem if isinstance(viagem, ViagemInternacional) else viagem.estado_origem
        origem = viagem.estado_origem if isinstance(viagem, ViagemNacional) else viagem.pais_origem
        destino = viagem.estado_destino if isinstance(viagem, ViagemNacional) else viagem.pais_destino
        descricao = viagem.descricao
        ida = viagem.data_ida
        volta = viagem.data_volta
        data_reserva = datetime.now()
        qtd_vagas = viagem.qtd_vagas
        n_pessoas = int(dados_reserva["n_pessoas"]) 
        preco_unitario = viagem.preco
        tipo = viagem.tipo
        visto = viagem.visto if tipo == "INTERNACIONAL" else None
        valor_final = preco_unitario * n_pessoas
        
        if n_pessoas > qtd_vagas:
            return self.__tela_reserva.mensagem_erro("A quantidade de pessoas excede o número de vagas disponíveis.")
        
        if visto and not cliente.visto:
            return self.__tela_reserva.mensagem_erro("O cliente não possui visto válido para esta viagem.")
        
        
        reserva = Reserva(codigo, cliente, nome_cliente, viagem, pais, origem, destino, descricao, ida, volta, data_reserva, qtd_vagas, n_pessoas, preco_unitario, tipo, visto, valor_final)
        self.__dao.add(reserva)
        
        viagem.qtd_vagas -= n_pessoas

        self.__tela_reserva.mensagem("Reserva cadastrada com sucesso.")
            
    def listar_reservas_feitas(self):
        if not self.__dao.get_all():
            self.__tela_agencia.mensagem("Não há reservas cadastradas.")
            return self.agencia_cliente()

        dados_reservas = []

        for reserva in self.__dao.get_all():
            dados_reserva = self.dados_reserva(reserva)
            dados_reservas.append(dados_reserva)

        self.__tela_reserva.mostrar_reserva(dados_reservas)
                    
        
    def dados_reserva(self,reserva):
        dados = {"codigo": reserva.codigo, "cliente": reserva.cliente,"nome_cliente": reserva.nome_cliente, "viagem": reserva.viagem,"pais":reserva.pais, "origem":reserva.origem, "destino":reserva.destino ,"descricao":reserva.descricao, "ida":reserva.ida, "volta":reserva.volta,"data_reserva": reserva.data_reserva, "qtd_vagas":reserva.qtd_vagas,"n_pessoas": reserva.n_pessoas,"preco_unitario":reserva.preco_unitario,"tipo":reserva.tipo,"visto":reserva.visto,"valor_final": reserva.valor_final }
        return dados
    
    
    def agencia_funcionario(self):
        funcionario = self.__controlador_funcionario.seleciona_funcionario()
        
        if isinstance(funcionario, Funcionario):
            self.__tela_agencia.mensagem("Acesso permitido")
            opcoes = {1: self.controlador_viagem}
            while True:
                opcao = self.__tela_agencia.tela_agencia_funcionario()
                if opcao == 0:
                    self.acessar()
                elif opcao == 2:
                    return self.listar_reservas_feitas()
                elif opcao == 3:
                    return self.total_vendas()
                elif opcao in opcoes.keys():
                    opcoes[opcao].inicia()
        else:
            self.__tela_agencia.mensagem_erro("Acesso negado")
            self.acessar()
            
    def total_vendas(self):
        total = 0
        for reserva in self.__dao.get_all():
            total += reserva.valor_final
        self.__tela_agencia.total_vendas(total)
        self.acessar()
