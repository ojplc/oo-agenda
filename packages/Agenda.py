from packages.Aluno import Aluno
from packages.Professor import Professor
class Agenda:
    def __init__(self, usuario_atual):
        if not isinstance(usuario_atual, (Aluno, Professor)):
            raise ValueError("usuario_atual deve ser uma instância de Aluno ou Professor")
        self.eventos = []
        self.pessoas = []
        self.canal = None #adicionar canal
        self._usuario = usuario_atual
        self.menu()
    

    def criar_evento(self):
        pass


    def criar_pessoa(self): #comecarei pelo desenvolvimento de pessoa
        if self.checar_permissao():
            atribuicao = None
            nome = None
            matricula = None
            contato = None
            while atribuicao == None:
                print("Qual a atribuição do usuário?")
                print("")
                print("1. Aluno")
                print("")
                print("2. Professor")
                print('')
                atribuicao = int(input())
                if atribuicao != 1 and atribuicao != 2:
                    print("Selecione uma opção válida")
                    atribuicao = None

            while nome == None:
                print("Qual o nome do usuário?")
                print("")
                nome = str(input())

            while matricula == None:
                print("Qual a matrícula do usuário?")
                print("")
                matricula = str(input())
            
            while contato == None:
                print("Qual o contato do usuário?")
                print("")
                contato = str(input())
            
            print(f"O {atribuicao} chamado {nome}, com matrícula {matricula} e contato {contato} será adicionado ao sistema")
            #atribuição ta imprimindo numero
            #quero adicionar a opção de mudar algum atributo quando chegar aqui
        else:
            print("Usuário não tem as permissões necessárias")
            


    def checar_permissao(self):
        return self._usuario.permissao()

    def cadastrar_evento(self):
        pass

    def menu(self):
        print("Bem vindo a agenda, o que você gostaria de fazer?")
        print('')
        print("1. Criar evento")
        print("")
        print("2. Adicionar usuário")
        print("")
        print("3. Cadastrar evento")
        print("")
        escolha = int(input())
        if escolha == 1:
            pass
        elif escolha == 2:
            self.criar_pessoa()
        elif escolha == 3:
            pass