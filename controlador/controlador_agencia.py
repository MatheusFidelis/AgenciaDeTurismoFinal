from datetime import datetime
from entidade.agencia import Agencia
from entidade.reserva import Reserva
from entidade.cliente import Cliente
from entidade.viagem_internacional import ViagemInternacional
from entidade.viagem_nacional import ViagemNacional
from entidade.funcionario import Funcionario
from tela.tela_agencia import TelaAgencia
from tela.tela_reserva import TelaReserva
from controlador.controlador_abstrato import ControladorAbstrato
from controlador.controlador_viagem import ControladorViagem
from controlador.controlador_funcionario import ControladorFuncionario
from controlador.controlador_cliente import ControladorCliente

class ControladorAgencia(ControladorAbstrato):
    def __init__(self):
        self.__reservas = []
        self.__tela_agencia = TelaAgencia()
        self.__tela_reserva = TelaReserva()
        self.__controlador_viagem = ControladorViagem()
        self.__controlador_funcionario = ControladorFuncionario()
        self.__controlador_cliente = ControladorCliente()
        
    def inicia(self): 
        opcoes = {"1": self.controlador_cliente, "2": self.controlador_funcionario}
        while True:
            opcao = self.__tela_agencia.opcoes()
            if opcao == "0":
                break
            if opcao == "3":
                return self.acessar()
            if opcao in opcoes.keys():
                opcoes[opcao].inicia()
            else:
                self.__tela.mensagem_erro("Comando Inválido")


    
    @property
    def controlador_cliente(self):
        return self.__controlador_cliente
    
    @property
    def controlador_funcionario(self):
        return self.__controlador_funcionario
    @property
    def controlador_viagem(self):
        return self.__controlador_viagem
    
    def acessar(self):
        while True:
            opcao = self.__tela_agencia.acessar()
            if opcao == "0":
                self.inicia()
            try:
                if opcao == "1":
                    return self.cliente()
                elif opcao == "2":
                    return self.funcionario()
                else:
                    raise ValueError
            except ValueError:
                self.__tela_agencia.mensagem_erro("Comando Inválido")
        

    
    def cliente(self):
        return self.agencia_cliente()

    
    def funcionario(self):
        return self.agencia_funcionario()

    def agencia_cliente(self):
        while True:
            opcao = self.__tela_agencia.tela_agencia_cliente()
            if opcao == "0":
                return self.acessar()
            if opcao == "1":
                self.listar_viagens_disp()
            elif opcao == "2":
                self.reservar()
            elif opcao == "3":
                self.listar_reservas_feitas()
            else:
                self.__tela_agencia.mensagem_erro("Comando Inválido")
        
    
    def listar_viagens_disp(self):
        viagens_disp = []
        for viagem in self.__controlador_viagem.viagens:
            codigo_viagem = viagem.codigo
            reserva_existente = False
            for reserva in self.__reservas:
                codigo_reserva = reserva["codigo"]
                if codigo_viagem == codigo_reserva:
                    reserva_existente = True
                    break
            if not reserva_existente:
                viagens_disp.append(viagem)

        for viagem in viagens_disp:
            if isinstance(viagem, ViagemInternacional):
                self.__controlador_viagem._ControladorViagem__tela.mostrar_internacional(self.__controlador_viagem.dados_viagem_internacional(viagem))
            elif isinstance(viagem, ViagemNacional):
                self.__controlador_viagem._ControladorViagem__tela.mostrar_nacional(self.__controlador_viagem.dados_viagem_nacional(viagem))
    
                    
    def seleciona_reserva(self):
        codigo = self.__tela_reserva.seleciona()
        for reserva in self.__reservas:
            if reserva.codigo == int(codigo):
                return reserva
            
    def reservar(self):
        dados_reserva = self.__tela_reserva.dados_reserva()

        codigo = dados_reserva["codigo"]
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
        visto = viagem.visto
        valor_final = preco_unitario * n_pessoas
        
        if n_pessoas > qtd_vagas:
            return self.__tela_reserva.mensagem_erro("A quantidade de pessoas excede o número de vagas disponíveis.")
        
        if visto and not cliente.visto:
            return self.__tela_reserva.mensagem_erro("O cliente não possui visto válido para esta viagem.")
        
        reserva = Reserva(codigo, cliente, nome_cliente, viagem, pais, origem, destino, descricao, ida, volta, data_reserva, qtd_vagas, n_pessoas, preco_unitario, tipo, visto, valor_final)
        self.__reservas.append(reserva)

        self.__tela_reserva.mensagem("Reserva cadastrada com sucesso.")
            
    def listar_reservas_feitas(self):
        if not self.__reservas:
            self.__tela_agencia.mensagem("Não há reservas cadastradas.")
            return self.agencia_cliente()
        for reserva in self.__reservas:
            self.__tela_reserva.mostrar_reserva(self.dados_reserva(reserva))
                
        
    def dados_reserva(self,reserva):
        dados = {"codigo": reserva.codigo, "cliente": reserva.cliente,"nome_cliente": reserva.nome_cliente, "viagem": reserva.viagem,"pais":reserva.pais, "origem":reserva.origem, "destino":reserva.destino ,"descricao":reserva.descricao, "ida":reserva.ida, "volta":reserva.volta,"data_reserva": reserva.data_reserva, "qtd_vagas":reserva.qtd_vagas,"n_pessoas": reserva.n_pessoas,"preco_unitario":reserva.preco_unitario,"tipo":reserva.tipo,"visto":reserva.visto,"valor_final": reserva.valor_final }
        return dados
        
    

    
    def agencia_funcionario(self):
        funcionario = self.__controlador_funcionario.seleciona_funcionario()
        
        if isinstance(funcionario, Funcionario):
            self.__tela_agencia.mensagem("Acesso permitido")
            opcoes = {"1": self.controlador_viagem}
            while True:
                opcao = self.__tela_agencia.tela_agencia_funcionario()
                if opcao == "0":
                    self.acessar()
                elif opcao == "2":
                    return self.listar_reservas_feitas()
                elif opcao == "3":
                    return self.total_vendas()
                elif opcao in opcoes.keys():
                    opcoes[opcao].inicia()
                else:
                    self.__tela_agencia.mensagem_erro("Comando Inválido")
        else:
            self.__tela_agencia.mensagem_erro("Acesso negado")
            
    def total_vendas(self):
        total = 0
        for reserva in self.__reservas:
            total += reserva.valor_final
        return total
