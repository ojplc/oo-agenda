from packages.Aluno import Aluno
from packages.Professor import Professor
from time import sleep
from packages.Evento import Evento
from datetime import datetime

class Agenda:
    def __init__(self, permissao, nome_usuario):
        self.eventos = []
        self.pessoas = []
        self.canal = None #adicionar canal
        self.__permissao = permissao
        self._nome_usuario = nome_usuario
        self.menu()
    

    def criar_evento(self): #trabalhando aqui
        nome_evento = None
        data_evento = None
        horario_start = None
        horario_finish = None
        quantidade_vagas = None
        
        atributos = {"1": nome_evento, "2" : data_evento, "3" : horario_start, "4" : horario_finish, "5" : quantidade_vagas}

        while nome_evento == None:
            print("\nQual será o nome do evento?")
            sleep(0.5)
            nome_evento = str(input("> "))

        while data_evento == None:
            print("\nQual será a data do evento? (use o formato DD/MM/AAAA)")
            sleep(0.5)
            data_evento = str(input("> "))
            dia,mes,ano = data_evento.split("/")
            try:
                datetime(int(ano), int(mes), int(dia))
            except ValueError:
                print("Data inválida, insira um valor válido")
                sleep(2)
                data_evento = None
        
        while horario_start == None:
            print("\nQue horas começará o evento? (use o formato HH:MM)")
            sleep(0.5)
            horario_start = str(input("> "))
            try:
                hs = datetime.strptime(horario_start, "%H:%M")
            except:
                print("Horário inválido, insira um valor válido")
                sleep(2)
                horario_start = None

        while horario_finish == None:
            print("\nQue horas terminará o evento? (use o formato HH:MM)")
            horario_finish = str(input("> "))
            try:
                hs = datetime.strptime(horario_finish, "%H:%M")
            except:
                print("Horário inválido, insira um valor válido")
                sleep(2)
                horario_finish = None
        
        while quantidade_vagas == None:
            print("\nQuantas vagas estarão disponíveis para o evento?")
            quantidade_vagas = int(input("> "))

        confirmacao = None
        novo_evento = Evento(nome_evento, dia, mes, ano, horario_start, horario_finish, quantidade_vagas)
        while confirmacao == False:
            print(f"\nO evento chamado '{novo_evento.titulo}' será adicionado ao sistema")
            print(f"Ele ocorrerá {novo_evento.dias_da_semana[novo_evento.date.weekday()]} dia {novo_evento.date.day}")
            print(f"Tendo uma duração de {str(novo_evento.duracao)[:-3]}") #remove os segundos
            print("\nConfirma a operação?\n")
            print("1. Adicionar evento")
            print("2. Editar informção\n")
            confirmacao = str(input("> "))
            if confirmacao == "1":
                self.eventos.append(novo_evento)
                print("Evento adicionado com sucesso")
            elif confirmacao == "2":
                alterar = None
                while alterar == None:
                    print("Qual informação você gostaria de alterar?")
                    print("\n1. Nome do evento")
                    print("\n2. Data do evento")
                    print("\n3. Horário de começo")
                    print("\n4. Horário de término")
                    print("\n5. Quantidade de vagas")
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
                    
                    



            

        


    def criar_pessoa(self):
        if self.checar_permissao():
            atribuicao = {"1": Aluno, "2": Professor}
            cargos = {"1": "Aluno", "2": "Professor"}

            atributos = {"cargo" : None, "nome" : None, "matricula" : None, "contato" : None}
            chaves = {"1": "cargo", "2": "nome", "3": "matricula", "4": "contato"}
            
            new_user = None
            while new_user == None:
                while atributos["cargo"] == None:
                    print("\nQual o cargo do usuário?")
                    print("\n1. Aluno")
                    print("2. Professor\n")
                    atributos["cargo"] = input("> ")
                    if atributos["cargo"] != "1" and atributos["cargo"] != "2":
                        print("Selecione uma opção válida")
                        atributos["cargo"] = None

                while atributos["nome"] == None:
                    print("\nQual o nome do usuário?")
                    atributos["nome"] = str(input("> "))

                while atributos["matricula"] == None:
                    print("\nQual a matrícula do usuário?")
                    atributos["matricula"] = str(input("> "))
                
                while atributos["contato"] == None:
                    print("\nQual o contato do usuário?")
                    atributos["contato"] = str(input("> "))
                
                confirmacao = None
                while confirmacao == None:
                    print(f"\nO {cargos[atributos["cargo"]]} chamado {atributos["nome"]}, com matrícula {atributos["matricula"]} e contato {atributos["contato"]} será adicionado ao sistema")
                    print("Confirma a operação?\n")
                    print("1. Adicionar usuário")
                    print("2. Editar informção\n")
                    confirmacao = input("> ")
                    if confirmacao == "1":
                        new_user = atribuicao.get(atributos["cargo"])(atributos["nome"],atributos["matricula"],atributos["contato"])
                        self.pessoas.append(new_user)
                        print("Novo usuário cadastrado com sucesso!\n")
                        sleep(1)
                    elif confirmacao == "2":
                        alterar = None
                        while alterar == None:
                            print("Qual informação você gostaria de editar?")
                            print("\n1. Cargo")
                            print("\n2. Nome")
                            print("\n3. Matricula")
                            print("\n4. Contato")
                            alterar = int(input("> "))
                            if alterar <= len(atributos) and alterar > 0:
                                atributos[chaves[str(alterar)]] = None
                            else:
                                print("\nInsira um valor válido")
                                sleep(1)
                                alterar = None
                        break
                    else:
                        print("Insira um valor válido")
                        confirmacao = None


              
        else:
            print("Usuário não tem as permissões necessárias")
            


    def checar_permissao(self):
        return self.__permissao

    def cadastrar_evento(self):
        pass

    def menu(self):
        escolha = 0
        while escolha == 0:
            print(f"Bem vindo a agenda {self._nome_usuario}, o que você gostaria de fazer?\n")
            print("1. Criar evento") #doing
            print("2. Adicionar usuário") 
            print("3. Cadastrar evento\n") #todo
            escolha = input("> ")
            if escolha == "1":
                self.criar_evento()
                escolha = 0
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