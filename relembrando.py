class Programa:
    def __init__(self,nome, ano):
        self.__nome = nome
        self.__ano = ano


class Filme:
    def __init__(self,nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao


class Serie:
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.__temporadas = temporadas


filme1= Filme('poderoso chefao', 1970, 180)
filme2= Filme('vingadores', 2012, 120)
serie1 = Serie('round 6', 2021, 1)
serie1 = Serie('evil dead', 2015, 3)

print('hrlo')