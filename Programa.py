class Programa:
    def __init__(self,nome, ano):
        self._nome = nome
        self._ano = ano
    
    def __str__(self):
        return f'nome: {self._nome}, ano: {self._ano}'

class Filme(Programa):
    def __init__(self,nome, ano, duracao):
        super().__init__(nome, ano)
        self._duracao = duracao
    
    def __str__(self):
        return f'nome: {self._nome}, ano {self._ano}, duração: {self._duracao} minutos'


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self._temporadas = temporadas

    def __str__(self):
        return f'nome: {self._nome}, ano {self._ano}, temporadas: {self._temporadas} temporadas'


filme1= Filme('poderoso chefao', 1970, 180)
filme2= Filme('vingadores', 2012, 120)
serie1 = Serie('round 6', 2021, 1)
serie2 = Serie('evil dead', 2015, 3)

lista = [filme1,filme2,serie1,serie2]

for item in lista:
    print(item)