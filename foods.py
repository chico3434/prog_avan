"""
Criado em 07/10/2021 para a aula de programação avançada

@author: Francisco Rubens
"""

# Gerar um gráfico de barras a partir da base "foods.db"

# ----------------------------
# PARTE 1: DATA WRANGLING (transformar os dados)
# ----------------------------

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# conexão com o "foods.db"
conn = sqlite3.connect('C:/Users/chico/PycharmProjects/prog_avan/foods.db')

vSQL = """SELECT t.name, e.season, COUNT(*) AS freq
FROM episodes e 
INNER JOIN foods_episodes fe ON (e.id = fe.episode_id)
INNER JOIN foods f ON (f.id = fe.food_id)
INNER JOIN food_types t ON (t.id = f.type_id)
WHERE e.season IN (8,9)
GROUP BY t.name, e.season
ORDER BY t.name, e.season
"""

c = conn.execute(vSQL)

resultados = c.fetchall()

nomes_colunas = next(zip(*c.description))

resultados.append(('Dip', 8, 0))
resultados.append(('Rice/Pasta', 8, 0))
resultados.sort()

tipos_comida = [t[0] for t in resultados if t[1] == 8]
freq_temp8 = [t[2] for t in resultados if t[1] == 8]
freq_temp9 = [t[2] for t in resultados if t[1] == 9]

df = pd.DataFrame({'t9': freq_temp9, 't8': freq_temp8}, index=tipos_comida)

# ----------------------------
# PARTE 2: ESTATÍSTICA (gerar o gráfico)
# ----------------------------

ax = df.plot.barh()
plt.show()
