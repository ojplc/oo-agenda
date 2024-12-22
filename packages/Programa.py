from packages.Agenda import Agenda
from packages.Aluno import Aluno
from packages.Professor import Professor
from packages.controllers.SerialFuntion import BancoDados
from time import sleep

class Programa:
    def __init__(self):
        self.__banco_alunos = BancoDados("banco alunos.json")
        self.__banco_professores = BancoDados("banco professores.json")

        self.user_atual = None
        self.login_menu()

        if not isinstance(self.user_atual, (Aluno, Professor)):
            raise ValueError("usuario_atual deve ser uma instância de Aluno ou Professor")
        ## ver se tem algum alarme ou evento pendente antes de abrir a agenda
        self.iniciar_agenda()

    def iniciar_agenda(self):
        self.sessao = Agenda(permissao = self.user_atual.permissao(), nome_usuario = self.user_atual.nome)
        
    def login_menu(self):
        login_matricula = None
        login_contato = None

        print("Bem vindo a agenda")
        while login_matricula == None:
            print("Insira sua matrícula para prosseguir\n")
            login_matricula = str(input("> "))
            print("Agora insira seu contato para prosseguir\n")
            login_contato = str(input("> "))

            if self.__banco_professores.login(login_matricula, login_contato):
                usuario = self.__banco_professores.get_objeto(login_matricula)
                self.user_atual = Professor(usuario['_nome'], usuario['_matricula'], usuario['_contato'])

            elif self.__banco_alunos.login(login_matricula, login_contato):
                usuario = self.__banco_alunos.get_objeto(login_matricula)
                self.user_atual = Aluno(usuario['_nome'], usuario['_matricula'], usuario['_contato'])
            else:
                print("Informações inválidas")
                login_matricula = None
