from funcionario import Funcionario
from ordenacao import insertion_sort
class ListaFuncionario:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.lista_funcionarios = []

    def ler_arquivo(self):
        self.lista_funcionarios = []  # Limpa a lista antes de ler novamente
        with open(self.arquivo, 'r') as arquivo:
            for linha in arquivo:
                # Verifica se a linha contém pelo menos três valores separados por tabulação
                valores = linha.strip().split('\t')
                if len(valores) == 3:
                    nome, cargo, doc = valores
                    self.adiciona_funcionario(nome, cargo, int(doc))

    def reescreve_arquivo(self):
        with open(self.arquivo, 'w', newline="") as arquivo:
            for funcionario in self.lista_funcionarios:
                arquivo.write(f'{funcionario.nome}\t{funcionario.cargo}\t{funcionario.doc}\n')

    def adiciona_funcionario(self, nome, cargo, doc):
        funcionario = Funcionario(nome, cargo, doc)
        self.lista_funcionarios.append(funcionario)
        insertion_sort(self.lista_funcionarios)
        self.reescreve_arquivo()
