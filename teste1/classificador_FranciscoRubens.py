###
# Teste 1 de Programação Avançada
# Nome: Francisco Rubens Karkow do Amaral
# Matrícula: 202010341-90
###

import math

class Classificador:

    def __init__(self, bd):
        self.bd = bd
        self.freq = None

    def calcular_freq(self):
        self.freq = {'N': 0, 'S': 0}
        for p in self.bd:
            if p[2] == 'S':
                self.freq['S'] += 1
            else:
                self.freq['N'] += 1

    def freq_classes(self):
        if self.freq is None:
            self.calcular_freq()
        return self.freq

    def desbalanceamento(self):
        if self.freq is None:
            self.calcular_freq()
        if self.freq['N'] > self.freq['S']:
            freq_majo = self.freq['N']
        else:
            freq_majo = self.freq['S']
        return freq_majo / len(self.bd)

    def classificar(self, novo):
        dist = [math.sqrt((p[0] - novo[0]) ** 2 + (p[1] - novo[1]) ** 2) for p in self.bd]
        min = dist[0]
        for n in dist:
            if min > n:
                min = n
        return self.bd[dist.index(min)][2]

bd_treino = (
    (38, 0, 'N'),
    (41, 30, 'S'),
    (45, 20, 'S'),
    (38, 4, 'N'),
    (29, 20, 'N'),
    (55, 24, 'S'),
    (41, 16, 'N'),
    (47, 4, 'N'),
    (50, 12, 'S')
)

classif = Classificador(bd_treino)
print(classif.bd)
print(classif.freq_classes())
print(classif.desbalanceamento())
novo_paciente1 = (47, 20)
classe = classif.classificar(novo_paciente1)
print('A classe do novo paciente é:', classe)

