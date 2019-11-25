from os import system
from getpass import getpass
from hashing import hashing
from usuarios import Usuario, Professor, Aluno
from menus import menus_bancos, cabecalho
import login

def limpar_tela():
    system('clear')
    cabecalho()


def banco_de_questoes(prof, id_usuario_online):
    limpar_tela()
    menus_bancos[prof]()
    if(prof):
        opcao = int(input())
        funcoes_professor[opcao - 1](id_usuario_online)
    else:
        pass


def adicionar_professor(id_usuario_online):
    limpar_tela()
    # print('Adicionar Professor')
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
    banco_de_questoes(1, id_usuario_online)


def listar_alunos(id_usuario_online):
    limpar_tela()
    for aluno in Aluno.alunos:
        if aluno.ativo:
            print(f'ID: {aluno.id_usuario}')
            print(f'Nome: {aluno.nome.title()}')
            print(f'Instituição: {aluno.instituicao.title()}')
            print(f'Idade: {aluno.idade}')
            print(f'ID Professor Resposável: {aluno.id_professor}\n')
    input()
    banco_de_questoes(1, id_usuario_online)


def adicionar_aluno(id_usuario_online):
    limpar_tela()
    # print('Adicionar Aluno')
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

    banco_de_questoes(1, id_usuario_online)


def remover_aluno(id_usuario_online):
    limpar_tela()
    # print('Remover Aluno')
    tem_aluno = False
    for aluno in Aluno.alunos:
        if aluno.id_professor == id_usuario_online and aluno.ativo:
            tem_aluno = True
            print(f'ID: {aluno.id_usuario}\nNome: {aluno.nome}\n')
    
    if tem_aluno:
        id_aluno = str(input('ID do aluno que deseja remover: '))
        for aluno in Aluno.alunos:
            if aluno.id_usuario == id_aluno:
                aluno.ativo = False
                break
        print('\nAluno removido com sucesso!')
    else:
        print('\nVocê não possui alunos cadastrados.')
    input()
    banco_de_questoes(1, id_usuario_online)


def editar_perfil_professor(id_usuario_online):
    limpar_tela()
    # print('Editar Perfil')
    professor = Professor.professores[id_usuario_online - 1]
    print(f'1 - Nome: {professor.nome}')
    print(f'2 - Instituição: {professor.instituicao}')
    print(f'3 - Matéria que leciona: {professor.materia}')
    print(f'4 - Login: {professor.login}')
    print('5 - Senha')
    print('6 - Desativar conta')
    print('7 - Retornar')
    opc = int(input('--> '))

    if opc == 1:
        professor.nome = str(input('Novo Nome: '))
        print('\nNome alterado com sucesso!')
        input()
    elif opc == 2:
        professor.instituicao = str(input('Nova Instituição: '))
        print('\nInstituição alterada com sucesso!')
        input()
    elif opc == 3:
        professor.materia = str(input('Nova Matéria: '))
        print('\nMatéria alterada com sucesso!')
        input()
    elif opc == 4:
        professor.login = str(input('Novo Login: '))
        print('\nLogin alterado com sucesso!')
        input()
    elif opc == 5:
        senha_atual = hashing(getpass(prompt='Senha atual: '))
        if senha_atual == professor.senha:
            nova_senha = getpass(prompt='Nova senha: ')
            confirmar = getpass(prompt='Confirmar a nova senha: ')
            if nova_senha == confirmar:
                professor.senha = hashing(nova_senha)
                print('\nSenha alterada com sucesso!')
                input()
            else:
                print('As senhas estão diferentes!')
                input()
        else:
            print('Senha incorreta!')
            input()
    elif opc == 6:
        confirmar = str(input('\nConfirmar exclusão da conta? (s/n)\n--> ')).lower()
        if confirmar == 's':
            professor.ativo = False
            print('\nConta excluída com sucesso!')
            input()
    elif opc == 7:
        banco_de_questoes(1, id_usuario_online)
    
    editar_perfil_professor(id_usuario_online)


def exibir_questoes(id_usuario_online):
    limpar_tela()
    print('Exibir Questões')
    input()


def adicionar_questao(id_usuario_online):
    limpar_tela()
    print('Adicionar Questão')
    input()


def remover_questao(id_usuario_online):
    limpar_tela()
    print('Remover Questão')
    input()


def gerar_prova(id_usuario_online):
    limpar_tela()
    print('Gerar Prova')
    input()


def sair(id_usuario_online):
    login.login()
    exit()


def encerrar(id_usuario_online):
    limpar_tela()
    print('\nAté logo!\n')
    input()
    exit()


funcoes_professor = [adicionar_professor, listar_alunos, adicionar_aluno, remover_aluno, editar_perfil_professor,
                    exibir_questoes, adicionar_questao, remover_questao, gerar_prova, sair, encerrar]