from os import system
from random import randint, shuffle
from getpass import getpass
from hashing import hashing
from usuarios import Usuario, Professor, Aluno
from menus import menus_bancos, cabecalho, menus_questoes, menu_alunos
from questoes import Questao
import login

# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# -------------------------------  GERAL  -------------------------------- #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

def limpar_tela():
    system('clear')
    cabecalho()


def sair(prof, id_usuario_online):
    login.login()


def encerrar(prof, id_usuario_online):
    limpar_tela()
    print('\nAté logo!\n')
    input()
    exit()


def retornar(prof, id_usuario_online):
    banco_de_questoes(prof, id_usuario_online)


# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# -------------------------  BANCO DE QUESTÕES  -------------------------- #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

def banco_de_questoes(prof, id_usuario_online):
    limpar_tela()
    menus_bancos[prof]()
    if(prof):
        opcao = int(input())
        funcoes_professor[opcao - 1](prof, id_usuario_online)
    else: # É aluno
        opcao = int(input())
        funcoes_aluno[opcao - 1](prof, id_usuario_online)


# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# -----------------------------  PROFESSOR  ------------------------------ #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

def adicionar_professor(prof, id_usuario_online):
    limpar_tela()
    Professor.adicionar_professor()
    banco_de_questoes(prof, id_usuario_online)


def editar_perfil_professor(prof, id_usuario_online):
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
            login.login()
    elif opc == 7:
        banco_de_questoes(prof, id_usuario_online)
    
    editar_perfil_professor(prof, id_usuario_online)


def listar_usuarios(prof, id_usuario_online):
    limpar_tela()
    Usuario.listar()
    banco_de_questoes(prof, id_usuario_online)


# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# -------------------------------  ALUNOS  ------------------------------- #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

def alunos(prof, id_usuario_online):
    limpar_tela()
    menu_alunos()
    opc = int(input())
    funcoes_prof_aluno[opc - 1](prof, id_usuario_online)


def listar(prof, id_usuario_online):
    limpar_tela()
    Aluno.listar()
    banco_de_questoes(prof, id_usuario_online)


def adicionar_aluno(prof, id_usuario_online):
    limpar_tela()
    Aluno.adicionar_aluno(id_usuario_online)
    banco_de_questoes(prof, id_usuario_online)


def remover_aluno(prof, id_usuario_online):
    limpar_tela()
    print('Remover Aluno')
    tem_aluno = False
    for aluno in Aluno.alunos:
        if aluno.id_professor == id_usuario_online and aluno.ativo:
            tem_aluno = True
            print(f'ID: {aluno.id_usuario}\nNome: {aluno.nome}\n')
    
    if tem_aluno:
        id_aluno = int(input('ID do aluno que deseja remover: '))
        for aluno in Aluno.alunos:
            if aluno.id_usuario == id_aluno:
                aluno.remover()
                print('\nAluno removido com sucesso!')
                break
    else:
        print('\nVocê não possui alunos cadastrados.')
    input()
    banco_de_questoes(prof, id_usuario_online)


def editar_perfil_aluno(prof, id_usuario_online):
    limpar_tela()
    print('Editar Perfil Aluno')
    aluno = Aluno.alunos[id_usuario_online - 1001]
    print(f'1 - Nome: {aluno.nome}')
    print(f'2 - Instituição: {aluno.instituicao}')
    print(f'3 - Idade: {aluno.idade}')
    print(f'4 - Login: {aluno.login}')
    print('5 - Senha')
    print('6 - Retornar')
    opc = int(input('--> '))

    if opc == 1:
        aluno.nome = str(input('Novo Nome: '))
        print('\nNome alterado com sucesso!')
        input()
    elif opc == 2:
        aluno.instituicao = str(input('Nova Instituição: '))
        print('\nInstituição alterada com sucesso!')
        input()
    elif opc == 3:
        aluno.idade = str(input('Nova Idade: '))
        print('\nIdade alterada com sucesso!')
        input()
    elif opc == 4:
        aluno.login = str(input('Novo Login: '))
        print('\nLogin alterado com sucesso!')
        input()
    elif opc == 5:
        senha_atual = hashing(getpass(prompt='Senha atual: '))
        if senha_atual == aluno.senha:
            nova_senha = getpass(prompt='Nova senha: ')
            confirmar = getpass(prompt='Confirmar a nova senha: ')
            if nova_senha == confirmar:
                aluno.senha = hashing(nova_senha)
                print('\nSenha alterada com sucesso!')
                input()
            else:
                print('As senhas estão diferentes!')
                input()
        else:
            print('Senha incorreta!')
            input()
    elif opc == 6:
        banco_de_questoes(prof, id_usuario_online)
    
    editar_perfil_aluno(prof, id_usuario_online)


# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# -----------------------------  QUESTÕES  ------------------------------- #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

def questoes(prof, id_usuario_online):
    limpar_tela()
    menus_questoes[0]()
    opc = int(input())
    funcoes_questoes[opc - 1](prof, id_usuario_online)


def exibir_questoes(prof, id_usuario_online):
    limpar_tela()
    print('Exibir Questões')
    menus_questoes[1]()
    opc = int(input())
    if opc == 1: # Exibir todas as questões
        limpar_tela()
        letras = ['a) ', 'b) ', 'c) ', 'd) ', 'e) ']
        apareceu = []
        for questao in Questao.questoes:
            if questao.ativa:
                num = randint(0, 4)
                apareceu.clear()
                print(f'ID: {questao.id_questao + 1}, Matéria: {questao.materia}, Assunto: {questao.palavra_chave}')
                print(f'{questao.texto}')
                for i in range(0, 5):
                    while num in apareceu: num = randint(0, 4)
                    print(f'{letras[i]}{questao.alternativas[num]}')
                    apareceu.append(num)
                if len(str(id_usuario_online)) < 4: print(f'\nResposta: {questao.resposta}\n')
                else: print()
        input()
    elif opc == 2: # Exibir questões por matéria
        limpar_tela()
        for index, materia in enumerate(Questao.materias, start=1):
            print(f'{index} - {materia}')
        opc = int(input('--> '))
        letras = ['a) ', 'b) ', 'c) ', 'd) ', 'e) ']
        apareceu = []
        for questao in Questao.questoes:
            if questao.materia == Questao.materias[opc - 1] and questao.ativa:
                num = randint(0, 4)
                apareceu.clear()
                print(f'ID: {questao.id_questao + 1}, Matéria: {questao.materia}, Assunto: {questao.palavra_chave}')
                print(f'{questao.texto}')
                for i in range(0, 5):
                    while num in apareceu: num = randint(0, 4)
                    print(f'{letras[i]}{questao.alternativas[num]}')
                    apareceu.append(num)
                if len(str(id_usuario_online)) < 4: print(f'\nResposta: {questao.resposta}\n')
                else: print()
        input()
    else: questoes(prof, id_usuario_online)

    banco_de_questoes(prof, id_usuario_online)


def adicionar_questao(prof, id_usuario_online):
    limpar_tela()
    Questao.adicionar_questao(id_usuario_online)
    banco_de_questoes(prof, id_usuario_online)


def remover_questao(prof, id_usuario_online):
    limpar_tela()
    print('Remover Questão')
    menus_questoes[1]()
    opc = int(input())
    if opc == 1: # Exibir todas as questões
        limpar_tela()
        letras = ['a) ', 'b) ', 'c) ', 'd) ', 'e) ']
        apareceu = []
        for questao in Questao.questoes:
            if questao.ativa:
                num = randint(0, 4)
                apareceu.clear()
                print(f'ID: {questao.id_questao + 1}, Matéria: {questao.materia}, Assunto: {questao.palavra_chave}')
                print(f'{questao.texto}')
                for i in range(0, 5):
                    while num in apareceu: num = randint(0, 4)
                    print(f'{letras[i]}{questao.alternativas[num]}')
                    apareceu.append(num)
                if len(str(id_usuario_online)) < 4: print(f'\nResposta: {questao.resposta}\n')
                else: print()
    elif opc == 2: # Exibir questões por matéria
        limpar_tela()
        for index, materia in enumerate(Questao.materias, start=1):
            print(f'{index} - {materia}')
        opc = int(input('--> '))
        letras = ['a) ', 'b) ', 'c) ', 'd) ', 'e) ']
        apareceu = []
        for questao in Questao.questoes:
            if questao.materia == Questao.materias[opc - 1] and questao.ativa:
                num = randint(0, 4)
                apareceu.clear()
                print(f'\nID: {questao.id_questao + 1}, Matéria: {questao.materia}, Assunto: {questao.palavra_chave}')
                print(f'{questao.texto}')
                for i in range(0, 5):
                    while num in apareceu: num = randint(0, 4)
                    print(f'{letras[i]}{questao.alternativas[num]}')
                    apareceu.append(num)
                if len(str(id_usuario_online)) < 4: print(f'\nResposta: {questao.resposta}\n')
                else: print()
    else:
        questoes(prof, id_usuario_online)

    id_remover = int(input('\nID da questão que deseja remover: '))
    Questao.questoes[id_remover - 1].ativa = False
    print('\nQuestão removida com sucesso!\n')
    input()
    remover_questao(prof, id_usuario_online)


# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# -------------------------  PROVAS E SIMULADOS  ------------------------- #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #

def gerar_prova(prof, id_usuario_online):
    limpar_tela()
    print('Gerar Prova')
    print('Quais matérias colocar na prova?')
    print('(Separe com um espaço simples. Ex.: 1 2 4)')
    for index, materia in enumerate(Questao.materias, start=1):
        print(f'{index} - {materia}')
    opcoes = str(input('--> '))
    opcoes = opcoes.split(' ')
    print('\nMatérias escolhidas:')
    qtd_questoes = []
    materias_escolhidas = []
    for index, opcao in enumerate(opcoes, start=1):
        print(f'{index} - {Questao.materias[int(opcao) - 1]}')
        materias_escolhidas.append(Questao.materias[int(opcao) - 1])
        maximo = 0
        for questao in Questao.questoes:
            if Questao.materias[int(opcao) - 1] == questao.materia: maximo += 1
        qtd_questoes.append(int(input(f'Quantidade de questões: (Max = {maximo}) ')))
        print()
    print(f'Total de questões: {sum(qtd_questoes)}')

    questoes_materias_escolhidas = []
    for questao in Questao.questoes:
        if questao.materia in materias_escolhidas:
            questoes_materias_escolhidas.append(questao)

    escolhidas = []
    indice = randint(0, len(questoes_materias_escolhidas) - 1)
    for index, qtd in enumerate(qtd_questoes):
        while qtd > 0:
            if questoes_materias_escolhidas[indice] not in escolhidas and questoes_materias_escolhidas[indice].materia == materias_escolhidas[index]:
                escolhidas.append(questoes_materias_escolhidas[indice])
                qtd -= 1
            else:
                indice = randint(0, len(questoes_materias_escolhidas) - 1)

    shuffle(escolhidas)
    letras = ['a) ', 'b) ', 'c) ', 'd) ', 'e) ']
    prova = open('prova.txt', 'w', encoding='utf-8')
    gabarito = open('gabarito.txt', 'w', encoding='utf-8')
    for index, questao in enumerate(escolhidas, start=1):
        prova.write(f'{index} {questao.texto}\n')
        gabarito.write(f'{index} {questao.resposta}\n')
        shuffle(questao.alternativas)
        for index2, alternativa in enumerate(questao.alternativas):
            prova.write(f'{letras[index2]}{alternativa}\n')
        prova.write('\n')
    prova.close()
    gabarito.close()

    print('\nProva e gabaritos gerados com sucesso!\n')
    input()
    banco_de_questoes(prof, id_usuario_online)


def gerar_simulado(prof, id_usuario_online):
    limpar_tela()
    print('Gerar Simulado')
    print('Quais matérias colocar no simulado?')
    print('(Separe com um espaço simples. Ex.: 1 2 4)')
    for index, materia in enumerate(Questao.materias, start=1):
        print(f'{index} - {materia}')
    opcoes = str(input('--> '))
    opcoes = opcoes.split(' ')
    print('\nMatérias escolhidas:')
    qtd_questoes = []
    materias_escolhidas = []
    for index, opcao in enumerate(opcoes, start=1):
        print(f'{index} - {Questao.materias[int(opcao) - 1]}')
        materias_escolhidas.append(Questao.materias[int(opcao) - 1])
        maximo = 0
        for questao in Questao.questoes:
            if Questao.materias[int(opcao) - 1] == questao.materia: maximo += 1
        qtd_questoes.append(int(input(f'Quantidade de questões: (Max = {maximo}) ')))
        print()
    print(f'Total de questões: {sum(qtd_questoes)}')
    input()

    questoes_materias_escolhidas = []
    for questao in Questao.questoes:
        if questao.materia in materias_escolhidas:
            questoes_materias_escolhidas.append(questao)

    escolhidas = []
    indice = randint(0, len(questoes_materias_escolhidas) - 1)
    for index, qtd in enumerate(qtd_questoes):
        while qtd > 0:
            if questoes_materias_escolhidas[indice] not in escolhidas and questoes_materias_escolhidas[indice].materia == materias_escolhidas[index]:
                escolhidas.append(questoes_materias_escolhidas[indice])
                qtd -= 1
            else:
                indice = randint(0, len(questoes_materias_escolhidas) - 1)
    shuffle(escolhidas)
    gabarito = []
    for escolhida in escolhidas:
        gabarito.append(escolhida.resposta)

    limpar_tela()
    letras = ['a) ', 'b) ', 'c) ', 'd) ', 'e) ']
    dict_resposta = {'a' : 0, 'b' : 1, 'c' : 2, 'd' : 3, 'e' : 4}
    respostas = []
    for index, questao in enumerate(escolhidas, start=1):
        print(f'{index} {questao.texto}')
        shuffle(questao.alternativas)
        for index2, alternativa in enumerate(questao.alternativas):
            print(f'{letras[index2]}{alternativa}')
        resp = str(input('\nResposta (letra): ')).lower()
        if questao.alternativas[dict_resposta[resp]] == questao.resposta:
            respostas.append(1)
        else:
            respostas.append(0)
        print()
    
    print('\n-=-=-=-=-=- RESULTADOS -=-=-=-=-=-\n')
    nota = (10 * sum(respostas)) / len(escolhidas)
    acertos = respostas.count(1)
    print(f'\nVocê acertou {acertos} questão de {len(escolhidas)}' if acertos == 1 else f'\nVocê acertou {acertos} questões de {len(escolhidas)}')
    print(f'Sua nota foi: {nota:.2f} de 10')

    print('\nRespostas:\n')
    for index, questao in enumerate(escolhidas, start=1):
        print(f'{index} {questao.resposta}')

    input()
    banco_de_questoes(prof, id_usuario_online)


# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #
# -------------------------  LISTAS DE FUNÇÕES  -------------------------- #
# ------------------------------------------------------------------------ #
# ------------------------------------------------------------------------ #


funcoes_professor = [adicionar_professor, alunos, listar_usuarios, editar_perfil_professor,
                    questoes, gerar_prova, sair, encerrar]

funcoes_aluno = [editar_perfil_aluno, exibir_questoes, gerar_simulado, sair, encerrar]

funcoes_questoes = [exibir_questoes, adicionar_questao, remover_questao, retornar]

funcoes_prof_aluno = [listar, adicionar_aluno, remover_aluno, retornar]
