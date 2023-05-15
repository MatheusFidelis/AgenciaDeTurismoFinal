from tela.tela_abstrata import TelaAbstrata

class TelaAgencia(TelaAbstrata):
    def __init__(self):
        pass
    
    def opcoes(self):   
        print(" --- AGÊNCIA DE VIAGEM --- ")
        print("Escolha uma das opções")
        print("1 - Cliente (cadastre-se) ")
        print("2 - Funcionario (cadastre-se)") 
        print("3 - Acessar")
        print("0 - Finalizar Sistema")
        opcao = input("Escolha uma opção: ")
        print("\n")
        return opcao
    
    def acessar(self):
        print(" --- AGÊNCIA DE VIAGEM --- ")
        print("Escolha uma das opções")
        print("1 - Sou Cliente")
        print("2 - Sou Funcionario")
        print("0 - voltar")
        opcao = input("Escolha uma opção: ")
        print("\n")
        return opcao
    
    def tela_agencia_cliente(self):
        print(" --- AGÊNCIA DE VIAGEM - CLIENTE --- ")
        print("Escolha uma das opções")
        print("1 - Listar viagens disponíveis")
        print("2 - Reservar")
        print("3 - Listar Reservas")
        print("0 - Voltar")
        opcao = input("Escolha uma opção: ")
        print("\n")
        return opcao
    
    def total_vendas(self,total):
        print(f"TOTAL DE VENDAS:  R$ {total}")
    
    def tela_agencia_funcionario(self):
        print(" --- AGÊNCIA DE VIAGEM - FUNCIONARIO --- ")
        print("Escolha uma das opções")
        print("1 - Cadastrar Viagem")
        print("2 - Listar reservas")
        print("3 - Total de vendas")
        print("0 - Voltar")
        opcao = input("Escolha uma opcao: ")
        print("\n")
        return opcao
    
    
