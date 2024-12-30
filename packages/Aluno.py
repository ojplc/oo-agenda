from packages.Pessoa import Pessoa


class Aluno(Pessoa):
    def __init__(self, nome, matricula, contato):
        self.nome = nome
        self.matricula = matricula
        self._contato = contato
        self.__permissao = False

    def permissao(self):
        return self.__permissao