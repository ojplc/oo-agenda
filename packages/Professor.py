from packages.Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, matricula, contato):
        self.nome = nome
        self.matricula = matricula
        self._contato = contato
        self.area = []
        self.__permissao = True

    @property
    def areas(self):
        return (f"suas areas de interesse são {self.area}")

    def adicionar_area(self, interesse):
        self.area.append(interesse)
        print(f"{interesse} foi adicionado a sua lista de interesses")


    def permissao(self):
        return self.__permissao