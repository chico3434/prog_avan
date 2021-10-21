#----- Exercício 1
num_criancas = [2, 0, 2, 3, 5, 3, 4, 0, 2, 7, 2, 1, 3, 1, 1, 4, 3, 0, 0, 1]

import pandas as pd
import matplotlib.pyplot as plt


df = pd.DataFrame(num_criancas, columns=['Número de crianças'])
df.boxplot()
plt.show()