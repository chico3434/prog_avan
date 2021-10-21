
num_criancas = [2, 0, 2, 3, 5, 3, 4, 0, 2, 7, 2, 1, 3, 1, 1, 4, 3, 0, 0, 1]

import statistics as st

print('Média:',st.mean(num_criancas))
print('Mediana:', st.median(num_criancas))
print('Moda:', st.mode(num_criancas))
print('Variância:', st.variance(num_criancas))
print('Desvio Padrão:', st.stdev(num_criancas))
print('Quartis:', st.quantiles(num_criancas))
print('Decis:', st.quantiles(num_criancas, n=10))