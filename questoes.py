class Questao():
    questoes = []
    quantidade_questoes = 0

    def __init__(self, materia, palavra_chave, texto, resposta, alternativas, id_professor):
        self.materia = materia
        self.palavra_chave = palavra_chave
        self.texto = texto
        self.resposta = resposta
        self.alternativas = alternativas
        self.id_professor = id_professor

'''
nova_questao = Questao('biologia', 'Células', 'Qual a fonte de energia das células?', 'Mitocôndria', ['Mitocôndria', 'Ribossomos', 'Lisossomos', 'Queratina', 'Lombriga'], 1)
Questao.quantidade_questoes += 1
Questao.questoes.append(nova_questao)

nova_questao = Questao('Inglês', 'Verbo to be', 'Como falar "Eu sou" em inglês?', 'I am', ['I am', 'You are', 'He is', 'I is', 'We am'], 1)
Questao.quantidade_questoes += 1
Questao.questoes.append(nova_questao)
'''

def atualizar_questoes():
    pass