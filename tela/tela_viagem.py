from tela.tela_abstrata import TelaAbstrata

class TelaViagem(TelaAbstrata):
    def __init__(self):
        pass
    
    def opcoes(self):
        print(" --- VIAGEM --- ")
        print("1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Remover")
        print("4 - Listar")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")
        print("\n")
        return opcao
    
    def seleciona_viagem(self):
        print(" --- SELECIONAR VIAGEM --- ")
        codigo = input("Codigo: ")
        print("\n")
        return codigo
    
    def tipo_da_viagem(self):
        print(" --- TIPO DE VIAGEM --- ")
        print("1 - Nacional")
        print("2 - Intercional")
        print("0 - Voltar")
        
        opcao = input("Escolha uma opção: ")
        print("\n")
        return opcao
        
    def dados_internacional(self):
        print(" --- CADASTRAR VIAGEM INTERNACIONAL --- ")
        codigo = input("Código: ")
        pais_origem = input("País de Origem: ").capitalize()
        pais_destino = input("País de Destino: ").capitalize()
        descricao = input("Descricao: ")
        data_ida = input("Insira a data de ida no formato DD-MM-YYYY: ")
        data_volta = input("Insira a data de volta no formato DD-MM-YYYY: ")
        preco = float(input("Preço do pacote: "))
        qtd_vagas = input("Quantidade de Vagas: ")
        tipo = "INTERNACIONAL"
        visto = True
        return {"codigo":codigo,"origem": pais_origem,"destino": pais_destino, "descricao": descricao,"data_ida":data_ida, "data_volta":data_volta, "preco":preco, "qtd_vagas":qtd_vagas, "tipo":tipo, "visto":visto}
    
    
        
    def alterar_internacional(self):
        print(" --- ALTERAR VIAGEM INTERNACIONAL --- ")

        pais_origem = input("País de Origem: ").capitalize()
        pais_destino = input("País de Destino: ").capitalize()
        descricao = input("Descricao: ")
        data_ida = input("Insira a data de ida no formato DD-MM-YYYY: ")
        data_volta = input("Insira a data de volta no formato DD-MM-YYYY: ")
        preco = input("Preço do pacote: ")
        qtd_vagas = input("Quantidade de Vagas: ")
        visto = True
        print("\n")
        
        return {"origem": pais_origem,"destino": pais_destino, "descricao": descricao,"data_ida":data_ida, "data_volta":data_volta, "preco":preco, "qtd_vagas":qtd_vagas, "visto":visto}
    
    
    
    def dados_nacional(self):
        print(" --- CADASTRAR VIAGEM NACIONAL --- ")
        codigo = input("Código: ")
        pais_origem = input("País de Origem: ").capitalize()
        pais_destino = input("País de Destino: ").capitalize()
        descricao = input("Descricao: ")
        data_ida = input("Insira a data de ida no formato DD-MM-YYYY: ")
        data_volta = input("Insira a data de volta no formato DD-MM-YYYY: ")
        preco = input("Preço do pacote: ")
        qtd_vagas = input("Quantidade de Vagas: ")
        tipo = "NACIONAL"
        estado_origem = input("Estado de Origem: ")
        estado_destino = input("Estado de Destino: ")
        print("\n")        
        
        return {"codigo":codigo,"origem": pais_origem,"destino": pais_destino, "descricao": descricao,"data_ida":data_ida, "data_volta":data_volta, "preco":preco, "qtd_vagas":qtd_vagas, "tipo":tipo,"estado_origem": estado_origem, "estado_destino": estado_destino}
    
    def alterar_nacional(self):
        print(" --- ALTERAR VIAGEM NACIONAL --- ")

        pais_origem = input("País de Origem: ").capitalize()
        pais_destino = input("País de Destino: ").capitalize()
        descricao = input("Descricao: ")
        data_ida = input("Insira a data de ida no formato DD-MM-YYYY: ")
        data_volta = input("Insira a data de volta no formato DD-MM-YYYY: ")
        preco = input("Preço do pacote: ")
        qtd_vagas = input("Quantidade de Vagas: ")
        estado_origem = input("Estado de Origem: ")
        estado_destino = input("Estado de Destino: ")
        print("\n")
        
        return {"origem": pais_origem,"destino": pais_destino, "descricao": descricao,"data_ida":data_ida, "data_volta":data_volta, "preco":preco, "qtd_vagas":qtd_vagas, "estado_origem": estado_origem, "estado_destino": estado_destino}
    
    def confirma_exclusao(self):
        print(" --- CONFIRMAR EXCLUSÃO --- ")
        print("0 - CONFIRMAR")
        print("1 - Cancelar")
        opcao = input("Escolha uma opção: ")
        print("\n")
        return opcao
    

    def mostrar_internacional(self,dados_viagem):          
        print(" --- VIAGEM ", dados_viagem["tipo"]," --- ")
        print("CÓDIGO: ", dados_viagem["codigo"])
        print("ORIGEM: ", dados_viagem["origem"])
        print("DESTINO: ", dados_viagem["destino"])
        print("DESCRIÇÃO: ", dados_viagem["descricao"])
        print("IDA: ", dados_viagem["data_ida"])
        print("VOLTA: ", dados_viagem["data_volta"])
        print("PREÇO: ", dados_viagem["preco"])
        print("QUANTIDADE DE VAGAS: ", dados_viagem["qtd_vagas"])
        print("TIPO: ", dados_viagem["tipo"])            
        print("\n")
        
    def mostrar_nacional(self,dados_viagem):
        print(" --- VIAGEM ", dados_viagem["tipo"]," --- ")
        print("CÓDIGO: ", dados_viagem["codigo"])
        print("PAÍS: ", dados_viagem["origem"])
        print("DESCRIÇÃO: ", dados_viagem["descricao"])
        print("IDA: ", dados_viagem["data_ida"])
        print("VOLTA: ", dados_viagem["data_volta"])
        print("PREÇO: ", dados_viagem["preco"])
        print("QUANTIDADE DE VAGAS: ", dados_viagem["qtd_vagas"])
        print("TIPO: ", dados_viagem["tipo"])
        print("ESTADO DE ORIGEM: ", dados_viagem["estado_origem"])
        print("ESTADO DE DESTINO: ", dados_viagem["estado_destino"])                        
        print("\n")
    
    
