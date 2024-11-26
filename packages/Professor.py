from packages.Pessoa import Pessoa


class Professor(Pessoa):
    def __init__(self, nome, matricula, contato):
        self._nome = nome
        self._matricula = matricula
        self._contato = contato
        self._area = []
        self._permissao = True

    @property
    def area(self):
        return (f"suas areas de interesse são {self.area}")

    def adicionar_area(self, interesse):
        self.area.append(interesse)
        print(f"{interesse} foi adicionado a sua lista de interesses")


    def permissao(self):
        return self._permissao