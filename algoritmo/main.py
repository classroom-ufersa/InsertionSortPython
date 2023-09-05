from listafuncionario import *
def main():
    arquivo = "funcionarios.txt" 
    lista_funcionarios = ListaFuncionario(arquivo)

    while True:
        print("1. Adicionar funcionário")
        print("2. Listar funcionários")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")

        lista_funcionarios.ler_arquivo()

        if escolha == "1":
            nome = input("Digite o nome do funcionário: ")
            cargo = input("Digite o cargo do funcionário: ")
            doc = int(input("Digite o documento do funcionário: "))
            lista_funcionarios.adiciona_funcionario(nome, cargo, doc)
            print("Funcionário adicionado com sucesso.")

        elif escolha == "2":
            print("\nLista de Funcionários:")
            print('NOME\tCARGO\tDOCUMENTO\n')
            for funcionario in lista_funcionarios.lista_funcionarios:
                print(f"{funcionario.nome}\t{funcionario.cargo}\t{funcionario.doc}")

        elif escolha == "3":
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
