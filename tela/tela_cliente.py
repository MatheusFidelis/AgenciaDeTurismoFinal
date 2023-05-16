from tela.tela_abstrata import TelaAbstrata


class TelaCliente(TelaAbstrata):
    def __init__(self):
        pass
    
    def opcoes(self):
        print(" --- CLIENTE --- ")
        print("1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Remover")
        print("4 - Listar")
        print("0 - Voltar")
    
        opcao = input("Escolha uma das opções: ")
        print("\n")
        return opcao
    
    def dados_cliente(self):
        print("------- CADASTRAR CLIENTE -------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        contato = input("Contato: ")
        visto = self.tem_visto(input("Tem visto? (sim ou nao): "))
        print("\n")
        return {"nome": nome,"cpf":cpf, "contato": contato, "visto":visto}
    
    def tem_visto(self, dados_visto: str = "") -> bool:
        # sourcery skip: merge-comparisons, merge-duplicate-blocks
        possui_visto = dados_visto.strip().lower()
        if possui_visto == "s" or possui_visto == "sim":
            return True
        elif possui_visto == "n" or possui_visto == "nao" or possui_visto == "não":
            return False
        else:
            return None
            
    
    def dados_alterar(self):
        print("------- ALTERAR CLIENTE -------")
        nome = input("Nome: ")
        contato = input("Contato: ")
        visto = self.tem_visto(input("Tem visto? (sim ou nao): "))
        print("\n")
        return {"nome": nome, "contato": contato, "visto":visto}
    
    
    def seleciona(self):
        print("------- SELECIONAR CLIENTE -------")
        cpf = input("Cpf: ")
        print("\n")
        return cpf
    
    def confirma_exclusao(self):
        print(" --- CONFIRMAR EXCLUSÃO --- ")
        print("0 - Confirmar")
        print("1 - Cancelar")
        
        opcao = input("Escolha uma das opções: ")
        print("\n")
        return opcao
        
    
    def mostra_cliente(self, dados_cliente):
        print("------- {} -------".format(dados_cliente["nome"]))
        print("NOME: ", dados_cliente["nome"])
        print("CPF: ", dados_cliente["cpf"])
        print("CONTATO: ", dados_cliente["contato"])
        print("VISTO: ", self.mostrar_visto(dados_cliente["visto"]))
        print("\n")
        
    def mostrar_visto(self, dados):
        convert = dados
        if convert is True:
            return 'Sim'
        else:
            return 'Não'
        
