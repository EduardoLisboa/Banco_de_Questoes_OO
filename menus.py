def cabecalho():
    print('-=' * 19, end='-\n')
    print('BANCO DE QUESTÕES'.center(40))
    print('-=' * 19, end='-\n')


def banco_professor():
    # print('O usuário é professor!')
    print('''1  - Adicionar Professor
2  - Listar Alunos
3  - Adicionar Aluno
4  - Remover Aluno
5  - Editar Perfil
6  - Exibir Questões
7  - Adiciona Questão
8  - Remover Questão
9  - Gerar Prova
10 - Sair
11 - Encerrar
--> ''', end='')


def banco_aluno():
    print('O usuário é aluno!')


menus_bancos = [banco_aluno, banco_professor] # 0 pra aluno, 1 pra professor