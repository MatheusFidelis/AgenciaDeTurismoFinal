from tela.tela_abstrata import TelaAbstrata
import datetime

class TelaReserva(TelaAbstrata):
    def __init__(self):
        pass
    
    def mostrar_reserva(self,dados):
        print(" --- RESERVAS --- ")
        print("Codigo: ", dados["codigo"])
        print("Cliente: ", dados["nome_cliente"])
        print("País: ", dados["pais"])
        print("Origem: ", dados["origem"])
        print("Destino: ", dados["destino"])
        print("Descrição: ", dados["descricao"])
        print("Ida: ", dados["ida"])
        print("Volta: ",dados["volta"])
        print("Data da Reserva: ",dados["data_reserva"])
        print("Número de Vagas Restante: ",dados["qtd_vagas"])
        print("Número de Vagas Preenchidas: ",dados["n_pessoas"])
        print("Preço Unitario: ",dados["preco_unitario"])
        print("Total: ",dados["valor_final"])
        print("\n")
    
        
    
    def dados_reserva(self):
        print(" --- RESERVA --- ")
        codigo = input("codigo da viagem: ")
        cliente = input("cpf do cliente: ")
        nome_cliente = str
        viagem = None
        pais = str
        origem = str
        destino = str
        descricao = str
        ida = datetime
        volta = datetime
        data_reserva = datetime
        qtd_vagas = None
        n_pessoas = int(input("Reserva para quantas pessoas: "))
        preco_unitario = float
        tipo = str
        visto = False
        valor_final = float
        print("\n")
        return {"codigo": codigo, "cliente": cliente,"nome_cliente":nome_cliente, "viagem": viagem,"pais":pais, "origem":origem, "destino":destino ,"descricao":descricao, "ida":ida, "volta":volta,"data_reserva": data_reserva, "qtd_vagas":qtd_vagas,"n_pessoas": n_pessoas,"preco_unitario":preco_unitario,"tipo":tipo,"visto":visto,"valor_final": valor_final }
    
    def seleciona(self):
        print("------- SELECIONAR RESERVA -------")
        codigo = input("codigo: ")
        print("\n")
        return codigo
