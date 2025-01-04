from datetime import datetime
class Evento:
    def __init__(self, titulo, dia, mes, ano, shoras, fhoras, numero_vagas, participantes = [], area = []):
        self.titulo = titulo

        self.ano,self.mes,self.dia = [ano, mes, dia]
        self.start_hour = shoras
        self.finish_hour = fhoras
        self.numero_vagas = numero_vagas
        self.area = area
        self.participantes = participantes


        
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

    def mes_evento(self):
        meses_do_ano = {
                        1: "janeiro",
                        2: "fevereiro",
                        3: "março",
                        4: "abril",
                        5: "maio",
                        6: "junho",
                        7: "julho",
                        8: "agosto",
                        9: "setembro",
                        10: "outubro",
                        11: "novembro",
                        12: "dezembro"
        }
        return meses_do_ano[self.mes]

    def retornar_datetime(self):
        return datetime(self.ano, self.mes, self.dia)

    def __str__(self):
        return f'O evento "{self.titulo}" ocorrerá {self.dia_evento()} dia {self.dia} de {self.mes_evento()},\ncomeça às {self.start_hour} \ntermina às {self.finish_hour} \ntendo duração de {str(self.calcular_duracao())}'



#self.date = datetime(ano, mes, dia)
#self.start_hour = datetime.strptime(shoras, "%H:%M")
#self.finish_hour = datetime.strptime(fhoras,"%H:%M")
#self.duracao = self.finish_hour - self.start_hour
    
