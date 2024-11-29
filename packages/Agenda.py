from packages.Aluno import Aluno
from packages.Professor import Professor
from time import sleep
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
            atribuicao = {"1": Aluno, "2": Professor}
            cargos = {"1": "Aluno", "2": "Professor"}
            cargo = None
            nome = None
            matricula = None
            contato = None
            atributos = {"1": cargo, "2": nome, "3": matricula, "4": contato}
            new_user = None
            while new_user == None:
                while cargo == None:
                    print("\nQual o cargo do usuário?")
                    print("\n1. Aluno")
                    print("2. Professor\n")
                    cargo = input("> ")
                    if cargo != "1" and cargo != "2":
                        print("Selecione uma opção válida")
                        cargo = None

                while nome == None:
                    print("\nQual o nome do usuário?")
                    nome = str(input("> "))

                while matricula == None:
                    print("\nQual a matrícula do usuário?")
                    matricula = str(input("> "))
                
                while contato == None:
                    print("\nQual o contato do usuário?")
                    contato = str(input("> "))
                
                confirmacao = None
                while confirmacao == None:
                    print(f"\nO {cargos[str(cargo)]} chamado {nome}, com matrícula {matricula} e contato {contato} será adicionado ao sistema")
                    print("Confirma a operação?\n")
                    print("1. Adicionar usuário")
                    print("2. Editar informção\n")
                    confirmacao = input("> ")
                    if confirmacao == "1":
                        new_user = atribuicao.get(str(cargo))(nome, matricula, contato)
                        self.pessoas.append(new_user)
                        print("Novo usuário cadastrado com sucesso")
                    elif confirmacao == "2":
                        alterar = None
                        while alterar == None:
                            print("Qual informação você gostaria de editar?")
                            print()
                            print("1. Cargo")
                            print()
                            print("2. Nome")
                            print()
                            print("3. Matricula")
                            print()
                            print("4. Contato")
                            alterar = int(input("> "))
                            if alterar <= len(atributos) + 1 and alterar > 0:
                                atributos[alterar] = None
                            else:
                                print()
                                print("Insira um valor válido")
                                alterar = None
                        break
                    else:
                        print("Insira um valor válido")
                        confirmacao = None


              
        else:
            print("Usuário não tem as permissões necessárias")
            


    def checar_permissao(self):
        return self._usuario.permissao()

    def cadastrar_evento(self):
        pass

    def menu(self):
        escolha = 0
        while escolha == 0:
            print(f"Bem vindo a agenda {self._usuario.nome}, o que você gostaria de fazer?\n")
            print("1. Criar evento")
            print("2. Adicionar usuário")
            print("3. Cadastrar evento\n")
            escolha = input("> ")
            if escolha == "1":
                pass
            elif escolha == "2":
                self.criar_pessoa()
                escolha = 0
            elif escolha == "3":
                pass
            elif escolha == 4:
                print("Até breve")
            else:
                print("opção inválida\n")
                escolha = 0