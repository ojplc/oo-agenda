from datetime import datetime
class Evento:
    def __init__(self, titulo, dia, mes, ano, shoras, fhoras, numero_vagas):
        self.titulo = titulo

        self.date = datetime(ano, mes, dia)
        self.start_hour = datetime.strptime(shoras, "%H:%M")
        self.finish_hour = datetime.strptime(fhoras,"%H:%M")
        self.duracao = self.finish_hour - self.start_hour
        self.dias_da_semana = {
                                0: "segunda-feira",
                                1: "terça-feira",
                                2: "quarta-feira",
                                3: "quinta-feira",
                                4: "sexta-feira",
                                5: "sábado",
                                6: "domingo"
        }
        self.area = []
        self.participantes = []
        self.numero_vagas = numero_vagas
        
    
    def __str__(self):
        return f"O evento '{self.titulo}' ocorrerá {self.dias_da_semana[self.date.weekday()]} dia {self.date.day}, terá duração de {str(self.duracao)[:-3]} "
    
