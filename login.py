from getpass import getpass
from os import system
from hashing import hashing
from usuarios import Usuario
from banco_de_questoes import banco_de_questoes, limpar_tela

usuarios_dict = dict()
def ler_usuarios():
    usuarios_dict.clear()
    for usuario in Usuario.usuarios:
        if usuario.ativo:
            usuarios_dict[usuario.login] = [usuario.senha, usuario.is_prof, usuario.id_usuario]


def login():
    while(True):
        limpar_tela()
        ler_usuarios()
        try:
            login = str(input('Login: '))
            senha = getpass(prompt='Senha: ')

            if usuarios_dict[login][0] == hashing(senha):
                print('\nLogin realizado com sucesso!\n')
                input()
                banco_de_questoes(usuarios_dict[login][1], usuarios_dict[login][2])
                exit()
            else:
                print('\nSenha incorreta!\n')
                input()
                system('clear')
        except KeyError:
            print('\nUsuário não cadastrado!\n')
            exit()