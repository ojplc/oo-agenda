from abc import ABC, abstractmethod

class Pessoa(ABC):
    # classe abstrata não tem init pois não terá instância
    


    @property
    def nome(self):
        return self._nome
    
    @property
    def matricula(self):
        return self._matricula    
    
    @property
    def contato(self):
        return self._contato
    
    @property
    @abstractmethod
    def areas(self):
        pass

   

    @nome.setter
    def nome(self,nome):
        self._nome = nome

    @matricula.setter
    def matricula(self,matricula):
        self._matricula = matricula

    @contato.setter
    def contato(self,contato):
        self._contato = contato



    @abstractmethod
    def adicionar_area(self):
        pass

    @abstractmethod
    def permissao(self):
        pass