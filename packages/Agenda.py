from packages.Aluno import Aluno
from packages.Professor import Professor
from time import sleep
from packages.Evento import Evento
from datetime import datetime
from packages.controllers.SerialFuntion import BancoDados

#começar a ver serialização agora para poder serializar os eventos
#para que exista eventos para cadastrar

#todo: fazer o comentario em criar_evento
class Agenda:
    def __init__(self, permissao, nome_usuario):
        self.__banco_alunos = BancoDados("banco alunos.json")
        self.__banco_professores = BancoDados("banco professores.json")
        self.banco_eventos = BancoDados("banco eventos.json")
        self.eventos = []
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

        novo_evento = None
        while novo_evento == None:
            while atributos["1"] == None:
                print("\nQual será o nome do evento?")
                sleep(0.5)
                atributos["1"] = str(input("> "))

            while atributos["2"] == None:
                print("\nQual será a data do evento? (use o formato DD/MM/AAAA)")
                sleep(0.5)
                atributos["2"] = str(input("> "))
                dia,mes,ano = atributos["2"].split("/")
                dia = int(dia)
                mes = int(mes)
                ano = int(ano)
                try:
                    datetime(int(ano), int(mes), int(dia))
                except ValueError:
                    print("Data inválida, insira um valor válido")
                    sleep(2)
                    atributos["2"] = None
            
            while atributos["3"] == None:
                print("\nQue horas começará o evento? (use o formato HH:MM)")
                sleep(0.5)
                atributos["3"] = str(input("> "))
                try:
                    hs = datetime.strptime(atributos["3"], "%H:%M")
                except:
                    print("Horário inválido, insira um valor válido")
                    sleep(2)
                    atributos["3"] = None
            #ACESCENTAR UM CHECK SE O TEMPO DE COMEÇO É ANTES DO DE TÉRMINO

            while atributos["4"] == None:
                print("\nQue horas terminará o evento? (use o formato HH:MM)")
                atributos["4"] = str(input("> "))
                try:
                    hf = datetime.strptime(atributos["4"], "%H:%M")
                except:
                    print("Horário inválido, insira um valor válido")
                    sleep(2)
                    atributos["4"] = None
            
            while atributos["5"] == None:
                print("\nQuantas vagas estarão disponíveis para o evento?")
                atributos["5"] = int(input("> "))

            confirmacao = None
            novo_evento = Evento(atributos["1"], dia, mes, ano, atributos["3"], atributos["4"], atributos["5"])
            while confirmacao == None:
                print(f"\nO evento chamado '{novo_evento.titulo}' será adicionado ao sistema")
                sleep(0.5)
                print(f"Ele ocorrerá {novo_evento.dias_da_semana[novo_evento.date.weekday()]} dia {novo_evento.date.day}")
                sleep(0.5)
                print(f"Tendo uma duração de {str(novo_evento.duracao)[:-3]}") #remove os segundos
                sleep(0.5)
                print("\nConfirma a operação?\n")
                sleep(0.5)
                print("1. Adicionar evento")
                print("2. Editar informção\n")
                confirmacao = str(input("> "))
                if confirmacao == "1":
                    self.eventos.append(novo_evento)
                    print("Evento adicionado com sucesso!\n")
                    sleep(1)
                elif confirmacao == "2":
                    novo_evento = None
                    
                    alterar = None #mantem o loop em menu ate um valor correto ser colocado
                    
                    while alterar == None:
                        print("Qual informação você gostaria de alterar?")
                        print("\n1. Nome do evento")
                        print("\n2. Data do evento")
                        print("\n3. Horário de começo")
                        print("\n4. Horário de término")
                        print("\n5. Quantidade de vagas\n")
                        alterar = int(input("> "))
                        if alterar <= len(atributos) + 1 and alterar > 0:
                            atributos[str(alterar)] = None
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
                        
                        if atributos["cargo"] == "1":
                            self.__banco_alunos.write(new_user)
                        
                        if atributos["cargo"] == "2":
                            self.__banco_professores.write(new_user)

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
            print("3. Cadastrar-se em um evento\n") #todo
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