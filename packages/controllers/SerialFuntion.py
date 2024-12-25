import json

class BancoDados:
    def __init__(self, arquivo):
        self.__nome_arquivo = "packages/controllers/db" + arquivo
        self.__objetos = []
        self.read()


    def read(self):
        try:
            with open(self.__nome_arquivo, "r", encoding="utf-8") as fjson:
                self.__objetos = json.load(fjson)
        except:
            print(f"Não existe arquivo {self.__nome_arquivo}")
            self.__objetos = []
    
    def write(self, objeto):
        self.__objetos.append(vars(objeto))
        self.save()

    def save(self):
        try:
            with open(self.__nome_arquivo, "w", encoding="utf-8") as fjson:
                json.dump(self.__objetos, fjson, indent = 4, ensure_ascii = False)
                print("Salvo com sucesso!")
        except:
            print("Não foi possível salvar")

    def get_objetos(self):
        return self.__objetos
    
    def atualizar_objeto(self,novo_objeto, index):
        self.__objetos[int(index)] = vars(novo_objeto)
        self.save()






    ## Relacionado a banco de dados de usuários
    def get_objeto(self, matricula):
        for objeto in self.__objetos:
            if matricula == objeto['_matricula']:
                return objeto
        return None
                
    def verificar_matricula(self, matricula): #retorna true se já existe
        for objeto in self.__objetos:
            if matricula == objeto['_matricula']:
                return True
        return False
    
    def login(self, matricula, contato):
        for objeto in self.__objetos:
            if matricula == objeto['_matricula']:
                if contato == objeto['_contato']:
                    return True
        return False