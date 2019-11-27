from hashing import hashing

class Usuario():
    usuarios = []
    quantidade_usuarios = 0

    def __init__(self, is_prof, nome, instituicao, login, senha, id_usuario, ativo):
        self.is_prof = is_prof
        self.nome = nome
        self.instituicao = instituicao
        self.login = login
        self.senha = hashing(senha)
        self.id_usuario = id_usuario
        self.ativo = ativo


class Professor(Usuario):
    professores = []
    indice_atual_professores = 0

    def __init__(self, is_prof, nome, instituicao, materia, login, senha, id_usuario, ativo):
        super().__init__(is_prof, nome, instituicao, login, senha, id_usuario, ativo)
        self.materia = materia


class Aluno(Usuario):
    alunos = []
    indice_atual_alunos = 0

    def __init__(self, is_prof, nome, instituicao, idade, login, senha, id_usuario, id_professor, ativo):
        super().__init__(is_prof, nome, instituicao, login, senha, id_usuario, ativo)
        self.idade = idade
        self.id_professor = id_professor


admin = Professor(1, 'admin', 'admin', 'todas', 'admin', 'admin', Professor.indice_atual_professores + 1, True)
Usuario.quantidade_usuarios += 1
Usuario.usuarios.append(admin)
Professor.indice_atual_professores += 1
Professor.professores.append(admin)


aluno = Aluno(0, 'Eduardo', 'UFAL', 15, 'eduardo', '123', Aluno.indice_atual_alunos + 1001, admin.id_usuario, True)
Usuario.quantidade_usuarios += 1
Usuario.usuarios.append(aluno)
Aluno.indice_atual_alunos += 1
Aluno.alunos.append(aluno)

