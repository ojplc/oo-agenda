from packages.Agenda import Agenda
from packages.Aluno import Aluno
from packages.Professor import Professor

class Programa:
    def __init__(self, user_atual):
        self.user_atual = user_atual
        if not isinstance(user_atual, (Aluno, Professor)):
            raise ValueError("usuario_atual deve ser uma instância de Aluno ou Professor")
        ## ver se tem algum alarme ou evento pendente antes de abrir a agenda
        self.iniciar_agenda()

    def iniciar_agenda(self):
        self.sessao = Agenda(permissao = self.user_atual.permissao(), nome_usuario = self.user_atual.nome)
        