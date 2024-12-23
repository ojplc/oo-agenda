from datetime import datetime
class Evento:
    def __init__(self, titulo, dia, mes, ano, shoras, fhoras, numero_vagas):
        self.titulo = titulo

        self.ano,self.mes,self.dia = [ano, mes, dia]
        self.start_hour = shoras
        self.finish_hour = fhoras
        self.numero_vagas = numero_vagas
        self.area = []
        self.participantes = []


        
    def calcular_duracao(self):
        return str(datetime.strptime(self.finish_hour, "%H:%M") - datetime.strptime(self.start_hour, "%H:%M"))[:-3] #remove os segundos

    def dia_evento(self):
        dias_da_semana = {
                                0: "segunda-feira",
                                1: "terça-feira",
                                2: "quarta-feira",
                                3: "quinta-feira",
                                4: "sexta-feira",
                                5: "sábado",
                                6: "domingo"
        }
        return dias_da_semana[datetime(self.ano, self.mes, self.dia).weekday()]

    def __str__(self):
        return f"O evento '{self.titulo}' ocorrerá {self.dia_evento()} dia {self.dia},\ne começa às {self.start_hour} terá duração de {str(self.calcular_duracao())[:-3]} "



#self.date = datetime(ano, mes, dia)
#self.start_hour = datetime.strptime(shoras, "%H:%M")
#self.finish_hour = datetime.strptime(fhoras,"%H:%M")
#self.duracao = self.finish_hour - self.start_hour
    
