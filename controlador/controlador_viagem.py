from controlador.controlador_abstrato import ControladorAbstrato
from entidade.viagem_internacional import ViagemInternacional
from entidade.viagem_nacional import ViagemNacional
from tela.tela_viagem import TelaViagem
from datetime import datetime
import re

class ControladorViagem(ControladorAbstrato):
    def __init__(self):
        self.__viagens = []
        self.__tela = TelaViagem()
        
    
    
    
    def inicia(self):
        opcoes = {"1": self.cadastro, "2": self.alterar, "3": self.remover, "4": self.listar}
        while True:
            opcao = self.__tela.opcoes()
            if opcao == "0":
                break
            try:
                if opcao in opcoes.keys():
                    opcoes[opcao]()
            except:
                self.__tela.mensagem_erro("Comando Inválido")
    
    def cadastro(self):
        while True:
            tipo = self.__tela.tipo_da_viagem()
            if tipo == "0":
                break
            try:
                if tipo == "1":
                    return self.cadastro_nacional()
                elif tipo == "2":
                    return self.cadastro_internacional()
                else:
                    return ValueError
            except ValueError:
                self.__tela.mensagem_erro("Comando Inválido")


    
    def cadastro_nacional(self):
        while True:
            dados = self.__tela.dados_nacional()
            if not self.verificar_dados_nacional(dados):
                continue
            codigo = int(dados["codigo"])
            codigo_repetido = False

            # Verificar duplicação de código em viagens nacionais
            for viagem in self.__viagens:
                if isinstance(viagem, ViagemNacional) and viagem.codigo == codigo:
                    codigo_repetido = True
                    self.__tela.mensagem_erro("Código duplicado na viagem nacional")
                    break

            # Verificar duplicação de código em viagens internacionais
            for viagem in self.__viagens:
                if isinstance(viagem, ViagemInternacional) and viagem.codigo == codigo:
                    codigo_repetido = True
                    self.__tela.mensagem_erro("Código duplicado na viagem internacional")
                    break

            if codigo_repetido:
                continue
                
            codigo = int(dados["codigo"])
            pais_origem = dados["origem"]
            pais_destino = dados["destino"]
            descricao = dados["descricao"]
            data_ida = self.valida_data(dados["data_ida"])
            data_volta = self.valida_data(dados["data_volta"])
            preco = float(dados["preco"])
            qtd_vagas = int(dados["qtd_vagas"])
            tipo = dados["tipo"]
            estado_origem = dados["estado_origem"]
            estado_destino = dados["estado_destino"]
            
            viagem = ViagemNacional(codigo, pais_origem, pais_destino, descricao, data_ida, data_volta, preco, qtd_vagas, tipo, estado_origem, estado_destino)
            self.__viagens.append(viagem)
            self.__tela.mensagem("Cadastro realizado com sucesso")
            break
        
    def verificar_dados_nacional(self, dados):
        if not dados["codigo"].isnumeric():
            self.__tela.mensagem_erro("Codigo invalido!")
            return False
        if dados["origem"].strip() =="":
            self.__tela.mensagem_erro("País origem nao pode estar vazio!")
            return False
        if dados["destino"].strip() =="":
            self.__tela.mensagem_erro("País destino nao pode estar vazio!")
            return False
        if dados["origem"].strip() != dados["destino"].strip():
            self.__tela.mensagem_erro("País de origem e destino devem ser iguais em viagem nacional")
            return False
        if dados["descricao"].strip() =="":
            self.__tela.mensagem_erro("País destino nao pode estar vazio!")
            return False
        if not self.valida_data(dados["data_ida"]):
            self.__tela.mensagem_erro("Valor data de ida incorreto")
            return False
        if not self.valida_data(dados["data_volta"]):
            self.__tela.mensagem_erro("Valor data de volta incorreto")
            return False
        
        data_ida = self.valida_data(dados["data_ida"])
        data_volta = self.valida_data(dados["data_volta"])
        if data_ida >= data_volta:
            self.__tela.mensagem_erro("A data de ida deve ser anterior à data de volta")
            return False
        
        if not self.is_float(dados["preco"]):
            self.__tela.mensagem_erro("Preço inválido!")
            return False
        if not dados["qtd_vagas"].isnumeric():
            self.__tela.mensagem_erro("Vagas foi preenchido de forma incorreta!")
            return False
        if dados["tipo"].strip() =="":
            self.__tela.mensagem_erro("Tipo")
            return False
        if dados["estado_origem"].strip() =="":
            self.__tela.mensagem_erro("Estado origem nao pode estar vazio!")
            return False
        if dados["estado_destino"].strip() =="":
            self.__tela.mensagem_erro("Estado destino nao pode estar vazio!")
            return False
        return True
    


        
    def cadastro_internacional(self):
        while True:
            dados = self.__tela.dados_internacional()
            if not self.verificar_dados_internacional(dados):
                continue
            codigo = int(dados["codigo"])
            codigo_repetido = False

            # Verificar duplicação de código em viagens internacionais
            for viagem in self.__viagens:
                if isinstance(viagem, ViagemInternacional) and viagem.codigo == codigo:
                    codigo_repetido = True
                    self.__tela.mensagem_erro("Código duplicado na viagem internacional")
                    break

            # Verificar duplicação de código em viagens nacionais
            for viagem in self.__viagens:
                if isinstance(viagem, ViagemNacional) and viagem.codigo == codigo:
                    codigo_repetido = True
                    self.__tela.mensagem_erro("Código duplicado na viagem nacional")
                    break

            if codigo_repetido:
                continue
            
            codigo = int(dados["codigo"])
            pais_origem = dados["origem"]
            pais_destino = dados["destino"]
            descricao = dados["descricao"]
            data_ida = self.valida_data(dados["data_ida"])
            data_volta = self.valida_data(dados["data_volta"])
            preco = float(dados["preco"])
            qtd_vagas = int(dados["qtd_vagas"])
            tipo = dados["tipo"]
            visto = dados["visto"]

            viagem = ViagemInternacional(codigo, pais_origem, pais_destino, descricao, data_ida, data_volta, preco, qtd_vagas, tipo, visto)
            self.__viagens.append(viagem)
            self.__tela.mensagem("Cadastro realizado com sucesso")
            break

    def verificar_dados_internacional(self, dados):
        if not dados["codigo"].isnumeric():
            self.__tela.mensagem_erro("Codigo inválido!")
            return False
        if dados["origem"].strip() == "":
            self.__tela.mensagem_erro("País de origem não pode estar vazio!")
            return False
        if dados["destino"].strip() == "":
            self.__tela.mensagem_erro("País de destino não pode estar vazio!")
            return False
        if dados["origem"].strip() == dados["destino"].strip():
            self.__tela.mensagem_erro("País de origem e destino devem ser diferentes em viagem internacional")
            return False
        if dados["descricao"].strip() == "":
            self.__tela.mensagem_erro("Descrição não pode estar vazia!")
            return False
        if not self.valida_data(dados["data_ida"]):
            self.__tela.mensagem_erro("Valor data de ida incorreto")
            return False
        if not self.valida_data(dados["data_volta"]):
            self.__tela.mensagem_erro("Valor data de volta incorreto")
            return False
        
        data_ida = self.valida_data(dados["data_ida"])
        data_volta = self.valida_data(dados["data_volta"])
        if data_ida >= data_volta:
            self.__tela.mensagem_erro("A data de ida deve ser anterior à data de volta")
            return False
        
        if not self.is_float(dados["preco"]):
            self.__tela.mensagem_erro("Preço inválido!")
            return False
        if not dados["qtd_vagas"].isnumeric():
            self.__tela.mensagem_erro("Quantidade de vagas foi preenchida de forma incorreta!")
            return False
        if dados["tipo"].strip() == "":
            self.__tela.mensagem_erro("Tipo não pode estar vazio!")
            return False

        return True
    
    

        

    def valida_data(self, data):
        while True:
            valor_lido = data
            try:
                day, month, year = map(int, re.split(r'-|/| ', valor_lido))
                valor_data = datetime(year, month, day)
                valor_data = valor_data.date()  # Obter somente a data, sem as horas
                return valor_data.strftime("%d/" + "%m/" + "%Y")
            except ValueError:
                self.__tela.mensagem_erro("Valor de data incorreto. Digite uma data válida.")
                data = input("Insira a data novamente no formato DD-MM-YYYY: ")

    def is_float(self, value: str = ""):
        while True:
            valor_lido = value
            try:
                valor_float = float(valor_lido)
                if isinstance(valor_float, float):
                    return valor_float
                return ValueError
            except ValueError:
                print(self.mensagem_erro("Valor numérico incorreto para definir o preço"))
                print(self.mensagem("Use ponto ao invés de vírgula caso necessário"))
    
    def dados_viagem_nacional(self,viagem_nacional):
        dados_nacional = {"codigo":viagem_nacional.codigo,"origem": viagem_nacional.pais_origem,"destino": viagem_nacional.pais_destino, "descricao": viagem_nacional.descricao,"data_ida":viagem_nacional.data_ida, "data_volta":viagem_nacional.data_volta, "preco":viagem_nacional.preco, "qtd_vagas":viagem_nacional.qtd_vagas, "tipo":viagem_nacional.tipo,"estado_origem": viagem_nacional.estado_origem, "estado_destino": viagem_nacional.estado_destino}
        return dados_nacional
    
    def dados_viagem_internacional(self,viagem_internacional):
        dados_internacional = {"codigo":viagem_internacional.codigo, "origem": viagem_internacional.pais_origem,"destino": viagem_internacional.pais_destino, "descricao": viagem_internacional.descricao,"data_ida":viagem_internacional.data_ida, "data_volta":viagem_internacional.data_volta, "preco":viagem_internacional.preco, "qtd_vagas":viagem_internacional.qtd_vagas, "tipo":viagem_internacional.tipo, "visto":viagem_internacional.visto}
        return dados_internacional
    
    def seleciona(self):
        codigo = self.__tela.seleciona_viagem()
        for viagem in self.__viagens:
            if viagem.codigo == int(codigo):
                return viagem
            
    def seleciona_externo(self,codigo):
        for viagem in self.__viagens:
            if viagem.codigo == int(codigo):
                return viagem
            
    def alterar(self):
        while True:
            select = self.seleciona()
            tipo = select.tipo
            try:
                if tipo == "NACIONAL":
                    return self.alterar_nacional(select)
                elif tipo == "INTERNACIONAL":
                    return self.alterar_internacional(select)
                else:
                    return ValueError
            except ValueError:
                self.__tela.mensagem_erro("Viagem nao encontrada")

    def alterar_nacional(self,viagem):
        if isinstance (viagem, ViagemNacional):
            self.__tela.mostrar_nacional(self.dados_viagem_nacional(viagem))
            while True:
                dados = self.__tela.alterar_nacional()
                dados["codigo"] = viagem.codigo
                if not self.verificar_dados_alterar_nacional(dados):
                    continue
                viagem.pais_origem = dados["origem"]
                viagem.pais_destino = dados["destino"]
                viagem.descricao = dados["descricao"]
                viagem.data_ida = self.valida_data(dados["data_ida"])
                viagem.data_volta = self.valida_data(dados["data_volta"])
                viagem.preco = float(dados["preco"])
                viagem.qtd_vagas = int(dados["qtd_vagas"])
                viagem.estado_origem = dados["estado_origem"]
                viagem.estado_destino = dados["estado_destino"]
                self.__tela.mensagem("Alteração realizada com sucesso")

                break
        else:
            self.__tela.mensagem_erro("Viagem não encontrado")
    
    def verificar_dados_alterar_nacional(self, dados):
        if dados["origem"].strip() =="":
            self.__tela.mensagem_erro("País origem nao pode estar vazio!")
            return False
        if dados["destino"].strip() =="":
            self.__tela.mensagem_erro("País destino nao pode estar vazio!")
            return False
        if dados["origem"].strip() != dados["destino"].strip():
            self.__tela.mensagem_erro("País de origem e destino devem ser iguais em viagem nacional")
            return False
        if dados["descricao"].strip() =="":
            self.__tela.mensagem_erro("País destino nao pode estar vazio!")
            return False
        if not self.valida_data(dados["data_ida"]):
            self.__tela.mensagem_erro("Valor data de ida incorreto")
            return False
        if not self.valida_data(dados["data_volta"]):
            self.__tela.mensagem_erro("Valor data de volta incorreto")
            return False
        
        data_ida = self.valida_data(dados["data_ida"])
        data_volta = self.valida_data(dados["data_volta"])
        if data_ida >= data_volta:
            self.__tela.mensagem_erro("A data de ida deve ser anterior à data de volta")
            return False
        if not self.is_float(dados["preco"]):
            self.__tela.mensagem_erro("Preço inválido!")
            return False
        if not dados["qtd_vagas"].isnumeric():
            self.__tela.mensagem_erro("Vagas foi preenchido de forma incorreta!")
            return False
        if dados["estado_origem"].strip() =="":
            self.__tela.mensagem_erro("Estado origem nao pode estar vazio!")
            return False
        if dados["estado_destino"].strip() =="":
            self.__tela.mensagem_erro("Estado destino nao pode estar vazio!")
            return False
        return True
        
    def alterar_internacional(self,viagem):
        if isinstance (viagem, ViagemInternacional):
            self.__tela.mostrar_internacional(self.dados_viagem_internacional(viagem))
            while True:
                dados = self.__tela.alterar_internacional()
                dados["codigo"] = viagem.codigo
                if not self.verificar_dados_alterar_internacional(dados):
                    continue
                viagem.pais_origem = dados["origem"]
                viagem.pais_destino = dados["destino"]
                viagem.descricao = dados["descricao"]
                viagem.data_ida = self.valida_data(dados["data_ida"])
                viagem.data_volta = self.valida_data(dados["data_volta"])
                viagem.preco = float(dados["preco"])
                viagem.qtd_vagas = int(dados["qtd_vagas"])
                viagem.visto = dados["visto"]

                self.__tela.mensagem("Alteração realizada com sucesso")
                break
        else:
            self.__tela.mensagem_erro("Viagem não encontrado")
    
    def verificar_dados_alterar_internacional(self, dados):
        if dados["origem"].strip() == "":
            self.__tela.mensagem_erro("País de origem não pode estar vazio!")
            return False
        if dados["destino"].strip() == "":
            self.__tela.mensagem_erro("País de destino não pode estar vazio!")
            return False
        if dados["origem"].strip() == dados["destino"].strip():
            self.__tela.mensagem_erro("País de origem e destino devem ser diferentes em viagem internacional")
            return False
        if dados["descricao"].strip() == "":
            self.__tela.mensagem_erro("Descrição não pode estar vazia!")
            return False
        if not self.valida_data(dados["data_ida"]):
            self.__tela.mensagem_erro("Valor data de ida incorreto")
            return False
        if not self.valida_data(dados["data_volta"]):
            self.__tela.mensagem_erro("Valor data de volta incorreto")
            return False
        
        data_ida = self.valida_data(dados["data_ida"])
        data_volta = self.valida_data(dados["data_volta"])
        if data_ida >= data_volta:
            self.__tela.mensagem_erro("A data de ida deve ser anterior à data de volta")
            return False
        
        if not self.is_float(dados["preco"]):
            self.__tela.mensagem_erro("Preço inválido!")
            return False
        if not dados["qtd_vagas"].isnumeric():
            self.__tela.mensagem_erro("Quantidade de vagas foi preenchida de forma incorreta!")
            return False
        return True
    
    
    def remover(self):
        while True:
            select = self.seleciona()
            tipo = select.tipo
            try:
                if tipo == "NACIONAL":
                    return self.remove_nacional(select)
                elif tipo == "INTERNACIONAL":
                    return self.remove_internacional(select)
                else:
                    return ValueError
            except ValueError:
                self.__tela.mensagem_erro("Viagem nao encontrada")
    
    def remove_nacional(self,viagem):
        if isinstance(viagem, ViagemNacional):
            self.__tela.mostrar_nacional(self.dados_viagem_nacional(viagem))
            confirmar = self.__tela.confirma_exclusao()
            if confirmar == "0":
                for i in range(len(self.__viagens)):
                    if self.__viagens[i] == viagem:
                        self.__viagens.pop(i)
                        self.__tela.mensagem("Exclusão realizada com sucesso")
                        break
            else:
                self.__tela.mensagem("Exclusão cancelada com sucesso")
    
    def remove_internacional(self,viagem):
        if isinstance(viagem, ViagemInternacional):
            self.__tela.mostrar_internacional(self.dados_viagem_internacional(viagem))
            confirmar = self.__tela.confirma_exclusao()
            if confirmar == "0":
                for i in range(len(self.__viagens)):
                    if self.__viagens[i] == viagem:
                        self.__viagens.pop(i)
                        self.__tela.mensagem("Exclusão realizada com sucesso")
                        break
            else:
                self.__tela.mensagem("Exclusão cancelada com sucesso")
        else:
            self.__tela.mensagem_erro("Cliente não encontrado")
    
    def listar(self):
        for viagem in self.__viagens:
            if isinstance (viagem, ViagemInternacional):
                self.__tela.mostrar_internacional(self.dados_viagem_internacional(viagem))
            elif isinstance (viagem, ViagemNacional):
                self.__tela.mostrar_nacional(self.dados_viagem_nacional(viagem))

    @property
    def viagens(self):
        return self.__viagens
