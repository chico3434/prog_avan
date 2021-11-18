class Robot:

    def __init__(self, nome, ano_fabr=None):
        self.nome = nome
        if(ano_fabr is None) or (type(ano_fabr) != int or (ano_fabr > 2020)):
            self.ano_fabr = 2020
        else:
            self.ano_fabr = ano_fabr

    def falar_oi(self):
        print("Oi, eu sou {} de {}.".format(self.nome, self.ano_fabr))


robo = Robot('Cleyton', 2009)
robo.falar_oi()
robo.ano_fabr = 'Teste'
robo.falar_oi()
