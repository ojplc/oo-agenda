# Projeto agenda
Atividade desenvolvida na disciplina orientação à objetos com o objetivo de criar uma agenda de eventos universitários.

# Sobre o programa
Para iniciar a agenda basta rodar o arquivo run_agenda.py, ele abrirá o login da agenda, as credenciais padrões para administrador são:
- matrícula: 01
- contato: admin

Na agenda, qualquer professor tem permissões de administrador, assim qualquer credencial em
- Agenda/packages/controllers/db/dbbanco_professores.json
será tratada como um administrador.

Ao efetuar o login o usuário será apresentado com um menu, o qual contém as funções da agenda.

## Criar evento
Qualquer usuário pode criar um evento, que poderá ser visualizado por todos que fizerem login na plataforma.
Ao criar um evento o usuário receberá perguntar direcionadas para montar um objeto da classe Evento, que após a confirmação do usuário será serializado no seguinte arquivo:
- Agenda/packages/controllers/db/dbbanco_eventos.json



## Adicionar usuário
Apenas adiministradores podem acrescentar usuários na agenda. Assim, é necessário que o usuário esteja logado como um professor para que seja possível adicionar uma nova credencial
As credenciais são salvas no arquivo
- Agenda/packages/controllers/db/dbbanco_alunos.json


## Cadastrar-se em um evento
Qualquer usuário pode se cadastrar em um evento, essa função apresentará ao usuário com os eventos disponíveis e suas respectivas vagas restantes, não sendo possível se cadastrar em um evento sem vagas
Se o usuário escolher um evento que ele já está cadastrado, ele será apresentado com a opção de se descadastrar.

# Sugestão de testes

## Descadastro em eventos
Se o usuário selecionar um evento o qual ele já está cadastrado ele receberá a opção de se descadastrar

## Colisão de horários
Fazendo o login como:
- matrícula: 241011170
- contato: 241011170@aluno.unb.br

Ao tentar se cadastrar no evento "Aulão de C2" o sistema avisará o usuário que ele já está cadastrado em outros dois eventos nesse mesmo dia. Cabe ao usuário decidir se se cadastrará mesmo assim ou se retornará a seleção de eventos.

## Eventos cheios
O evento "Debate eleitoral" não possui mais vagas e por isso o usuário não conseguirá se cadastrar

