from packages.Agenda import Agenda
from packages.Aluno import Aluno
from packages.Professor import Professor

Aluno1 = Aluno("Divo", 333, 99961)

print(Aluno1.permissao())

Professor1 = Professor("alan",334,1192)

print(Professor1.permissao())


agenda0 = Agenda(Professor1)