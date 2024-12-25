from packages.Aluno import Aluno
from packages.Professor import Professor
from time import sleep
from packages.Evento import Evento
from datetime import datetime
from packages.controllers.SerialFuntion import BancoDados


#todo: fazer o comentario em criar_evento done
#colocar area de interesse nos eventos
#conferir se tudo está funcionando
class Agenda:
    def __init__(self, usuario_atual):
        self.__banco_alunos = BancoDados("banco alunos.json")
        self.__banco_professores = BancoDados("banco professores.json")
        self.banco_eventos = BancoDados("banco eventos.json")
        self.canal = None #adicionar canal
        self.__permissao = usuario_atual.permissao()
        self._nome_usuario = usuario_atual.nome
        self._matricula = usuario_atual.matricula
        self.menu()
    


    def criar_evento(self):
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
                try:
                    dia,mes,ano = atributos["2"].split("/")
                    dia = int(dia)
                    mes = int(mes)
                    ano = int(ano)
                    datetime(int(ano), int(mes), int(dia))
                except ValueError:
                    print("Data inválida, insira um valor válido")
                    sleep(2)
                    atributos["2"] = None
            
            #horario start e horario finish
            while atributos["3"] == None:
                print("\nQue horas começará o evento? (use o formato HH:MM)")
                sleep(0.5)
                atributos["3"] = str(input("> "))
                try:
                    hs = datetime.strptime(atributos["3"], "%H:%M")
                    erro = False
                except:
                    print("Horário inválido, insira um valor válido")
                    sleep(2)
                    atributos["3"] = None
                    erro = True


                while atributos["4"] == None:
                    if erro == True:
                        break
                    print("\nQue horas terminará o evento? (use o formato HH:MM)")
                    atributos["4"] = str(input("> "))
                    try:
                        hf = datetime.strptime(atributos["4"], "%H:%M")
                    except:
                        print("Horário inválido, insira um valor válido")
                        sleep(2)
                        atributos["4"] = None
                #horario start precisa ser menor que horario finish
                if not erro and hf < hs:
                    print("\nHorário de término tem que ser depois do horário do começo do evento")
                    atributos["3"] = None
                    atributos["4"] = None
                    sleep(2)
            
            #quantidade de vagas
            while atributos["5"] == None:
                print("\nQuantas vagas estarão disponíveis para o evento?")
                try:
                    atributos["5"] = int(input("> "))
                except:
                    print("Valor inválido")
                    atributos["5"] = None
                    sleep(2)

            confirmacao = None
            novo_evento = Evento(atributos["1"], dia, mes, ano, atributos["3"], atributos["4"], atributos["5"])
            while confirmacao == None:
                print(f"\nO evento chamado '{novo_evento.titulo}' será adicionado ao sistema")
                print(f"Ele ocorrerá {novo_evento.dia_evento()} dia {novo_evento.dia}")
                print(f"Tendo uma duração de {novo_evento.calcular_duracao()} hora(s)")
                print("\nConfirma a operação?\n")
                print("1. Adicionar evento")
                print("2. Editar informção\n")
                confirmacao = str(input("> "))
                #evneto adicionado
                if confirmacao == "1":
                    self.banco_eventos.write(novo_evento)
                    sleep(1)
                #trocar alguma informação
                elif confirmacao == "2":
                    novo_evento = None
                    
                    alterar = None #mantem o loop em menu ate um valor correto ser colocado
                    
                    while alterar == None:
                        print("Qual informação você gostaria de alterar?")
                        print("\n1. Nome do evento")
                        print("\n2. Data do evento")
                        print("\n3. Horário")
                        print("\n4. Quantidade de vagas\n")
                        alterar = int(input("> "))
                        if alterar == 3:
                            atributos["3"] = None
                            atributos["4"] = None
                        elif alterar == 4:
                            atributos["5"] = None
                        elif alterar <= len(atributos) + 1 and alterar > 0:
                            atributos[str(alterar)] = None
                        else:
                            print()
                            print("Insira um valor válido")
                            alterar = None
                    break #break porque confirmação ainda nao tem valor
                else:
                    print("Insira um valor válido")
                    sleep(1)
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
                    if self.__banco_alunos.verificar_matricula(atributos["matricula"]) or self.__banco_professores.verificar_matricula(atributos["matricula"]):
                        print("\nEssa matricula já está cadastrada no sistema!!\n")
                        sleep(2)
                        atributos["matricula"] == None
                
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
            sleep(1)
            


    def checar_permissao(self):
        return self.__permissao

    def cadastrar_evento(self):
        #todo:
        #se nao tiver vaga nao cadastra done
        #se ja tiver cadastrado nao cadastra de novo done 
        cadastrado = False
        while not cadastrado:
            contagem = 1
            ja_cadastrado = {}
            print("\nOs eventos disponíveis são:\n")
            for eventos_criados in self.banco_eventos.get_objetos():
                print(f"{contagem}. {eventos_criados['titulo']}")
                for participantes in eventos_criados["participantes"]:
                    if self._matricula == participantes:
                        print("--> já cadastrado")
                        ja_cadastrado[str(contagem)] = True
                print(f"--> {eventos_criados["numero_vagas"] - len(eventos_criados["participantes"])} vagas disponíveis\n")
                contagem += 1
            print("Escolha uma opção para receber mais detalhes sobre o evento\n(escreva SAIR para voltar ao menu)")
            escolha = input("> ")
            if escolha == "SAIR" or escolha == "sair" or escolha == "Sair":
                cadastrado = True
            elif int(escolha) > 0 and int(escolha) <= len(self.banco_eventos.get_objetos()):
                evento_escolhido = self.banco_eventos.get_objetos()[int(escolha)-1] #index do evento
                evento_escolhido = Evento(evento_escolhido['titulo'],evento_escolhido['dia'],evento_escolhido['mes'],evento_escolhido['ano'], evento_escolhido['start_hour'], evento_escolhido['finish_hour'], evento_escolhido['numero_vagas'], evento_escolhido["participantes"])
                print(f"\n{evento_escolhido}")
                if ja_cadastrado.get(str(escolha)):
                    print("\nVocê já está cadastrado nesse evento\n")
                    print("1. Descadastrar")
                    print("2. Voltar à seleção")
                    escolha2 = input(">")
                    if escolha2 == "1":
                        evento_escolhido.participantes.remove(self._matricula)
                        self.banco_eventos.atualizar_objeto(evento_escolhido, int(escolha)-1)
                        sleep(1)
                elif evento_escolhido.numero_vagas - len(evento_escolhido.participantes) == 0:
                    print("\nEvento não tem mais vagas diponíveis")
                    sleep(2)
                else:

                    print("\nGostaria de se cadastrar?")
                    print("\n1. Sim")
                    print("2. Voltar à seleção\n")
                    escolha2 = input("> ")
                    if escolha2 == "1":
                        evento_escolhido.participantes.append(self._matricula)
                        self.banco_eventos.atualizar_objeto(evento_escolhido, int(escolha)-1)
                        sleep(1)
                        cadastrado = True
            else:
                print("Opção inválida")
                sleep(1)

    def menu(self):
        escolha = 0
        while escolha == 0:
            print(f"\nBem vindo a agenda {self._nome_usuario}, o que você gostaria de fazer?\n")
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
                self.cadastrar_evento()
                escolha = 0

            elif escolha == 4:
                print("Até breve")

                #adicionar area de interesse tambem
            else:
                print("opção inválida\n")
                escolha = 0