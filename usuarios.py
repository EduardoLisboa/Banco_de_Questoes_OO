from getpass import getpass
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
    
    def remover(self):
        self.ativo = False


class Professor(Usuario):
    professores = []
    indice_atual_professores = 0

    def __init__(self, is_prof, nome, instituicao, materia, login, senha, id_usuario, ativo):
        super().__init__(is_prof, nome, instituicao, login, senha, id_usuario, ativo)
        self.materia = materia


    @staticmethod
    def adicionar_professor():
        print('Adicionar Professor')
        nome = str(input('Nome: '))
        instituicao = str(input('Instituição: '))
        materia = str(input('Matéria que leciona: '))
        login = str(input('Login: '))
        senha = getpass(prompt='Senha: ')
        novo_prof = Professor(1, nome, instituicao, materia, login, senha, Professor.indice_atual_professores + 1, True)

        Professor.indice_atual_professores += 1
        Professor.professores.append(novo_prof)
        Usuario.quantidade_usuarios += 1
        Usuario.usuarios.append(novo_prof)

        print('\nProfessor cadastrado com sucesso!\n')
        input()


class Aluno(Usuario):
    alunos = []
    indice_atual_alunos = 0

    def __init__(self, is_prof, nome, instituicao, idade, login, senha, id_usuario, id_professor, ativo):
        super().__init__(is_prof, nome, instituicao, login, senha, id_usuario, ativo)
        self.idade = idade
        self.id_professor = id_professor


    @staticmethod
    def listar_alunos():
        print('Listar Alunos')
        for aluno in Aluno.alunos:
            if aluno.ativo:
                print(f'ID: {aluno.id_usuario}')
                print(f'Nome: {aluno.nome.title()}')
                print(f'Instituição: {aluno.instituicao.title()}')
                print(f'Idade: {aluno.idade}')
                print(f'ID Professor Resposável: {aluno.id_professor}\n')
        input()
    

    @staticmethod
    def adicionar_aluno(id_usuario_online):
        print('Adicionar Aluno')
        nome = str(input('Nome: '))
        instituicao = str(input('Instituição: '))
        idade = int(input('Idade: '))
        login = str(input('Login: '))
        senha = getpass(prompt='Senha: ')
        novo_aluno = Aluno(0, nome, instituicao, idade, login, senha, Aluno.indice_atual_alunos + 1001, id_usuario_online, True)
        
        Aluno.indice_atual_alunos += 1
        Aluno.alunos.append(novo_aluno)
        Usuario.quantidade_usuarios += 1
        Usuario.usuarios.append(novo_aluno)

        print('\nAluno cadastrado com sucesso!\n')
        input()


admin = Professor(1, 'admin', 'admin', 'todas', 'admin', 'admin', Professor.indice_atual_professores + 1, True)
Usuario.quantidade_usuarios += 1
Usuario.usuarios.append(admin)
Professor.indice_atual_professores += 1
Professor.professores.append(admin)

aluno = Aluno(0, 'Eduardo Lisboa', 'UFAL', 24, 'eduardo', '123', Aluno.indice_atual_alunos + 1001, admin.id_usuario, True)
Usuario.quantidade_usuarios += 1
Usuario.usuarios.append(aluno)
Aluno.indice_atual_alunos += 1
Aluno.alunos.append(aluno)
