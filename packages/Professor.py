from packages.Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, matricula, contato):
        self.nome = nome
        self.matricula = matricula
        self._contato = contato
        self.__permissao = True

    def permissao(self):
        return self.__permissao