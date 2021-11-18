class Robot:

    def __init__(self, nome, ano_fabr=None):
        self.__nome = nome
        if (ano_fabr is None) or (type(ano_fabr) != int or (ano_fabr > 2020)):
            self.__ano_fabricacao = 2020
        else:
            self.__ano_fabricacao = ano_fabr

    def falar_oi(self):
        print("Oi, eu sou {} de {}.".format(self.__nome, self.__ano_fabricacao))


robo = Robot('Jhon', 2011)
robo.falar_oi()
robo._Robot__ano_fabricacao = 'aaa'
robo.falar_oi()
