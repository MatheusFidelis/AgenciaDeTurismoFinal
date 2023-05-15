from tela.tela_abstrata import TelaAbstrata


class TelaFuncionario(TelaAbstrata):
    def __init__(self):
        pass

    def opcoes(self):
        print(" --- FUNCIONARIO --- ")
        print("1 - Cadastrar")
        print("2 - Alterar")
        print("3 - Remover")
        print("4 - Listar")
        print("0 - Voltar")

        opcao = input("Escolha uma das opções: ")
        print("\n")
        return opcao

    def dados_funcionario(self):
        print("------- CADASTRAR FUNCIONARIO -------")
        nome = input("Nome: ")
        matricula = input("MATRICULA: ")
        contato = input("Contato: ")
        print("\n")
        return {"nome": nome, "matricula": matricula, "contato": contato}

    def dados_alterar(self):
        print("------- ALTERAR FUNCIONARIO -------")
        nome = input("Nome: ")
        contato = input("Contato: ")
        print("\n")
        return {"nome": nome, "contato": contato}

    def seleciona(self):
        print("------- SELECIONAR FUNCIONARIO -------")
        matricula = input("Matricula: ")
        print("\n")
        return matricula

    def confirma_exclusao(self):
        print(" --- CONFIRMAR EXCLUSÃO --- ")
        print("0 - Confirmar")
        print("1 - Cancelar")

        opcao = input("Escolha uma das opções: ")
        print("\n")
        return opcao

    def mostra_funcionario(self, dados_funcionario):
        print("------- {} -------".format(dados_funcionario["nome"]))
        print("NOME: ", dados_funcionario["nome"])
        print("MATRICULA: ", dados_funcionario["matricula"])
        print("CONTATO: ", dados_funcionario["contato"])
        print("\n")

