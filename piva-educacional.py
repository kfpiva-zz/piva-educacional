import random

materias = ('Português', 'Inglês', 'Matemática', 'Biologia', 'Física', 'Filosofia', 'Espanhol', 'Química', 'Redação')
series = {'Primeira serie':1, 'Segunda serie':2,'Terceira serie':1,'Quarta serie':4,'Quinta serie':5, 'Sexta serie':6,'Sética serie':7,'Oitava serie':8,'Nona serie':9 }


class Aluno(object):
    """docstring for [object Object]."""
    def __init__(self, nome):
        super([object Object], self).__init__()
        self.nome = nome

class Professor(object):
    """docstring for [object Object]."""
    def __init__(self, nome):
        super([object Object], self).__init__()
        self.nome = nome
        self.ensina = {}
        for materia in materias:
            self.ensina[materia] = input(f'Você ensina {materia} (sim/não)?')

    def disponibilidade():
        pass

class aula(object):
    """docstring for [object Object]."""
    def __init__(self, duracao, materia, professor, aluno):
        super([object Object], self).__init__()
        self.duracao = duracao
        self.materia = materia

    def extender():
        while True:
            try:
                duracao = duracao + int(input('Quantos minutos de aula você gostaria de adiconar?'))
            except:
                print("Isso não é um número")
                continue
            else:
                break

    def __str__():
        return "Aula de %s , duraçao %s, com aluno %s e professor %s" %(materia,duracao,aluno,professor)
