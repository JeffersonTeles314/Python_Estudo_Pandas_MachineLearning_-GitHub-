import pandas as pd

# Salvando uma O Caminho do Arquivo em Uma Variável Para Lhor Acesso
plantest_caminho_arqv = 'Pandas/plantest.csv'
# Lendo os Dados e armazenando os Dados em um DataFrame Chamado melbourne_data
plantest_data = pd.read_csv(plantest_caminho_arqv) 
# Imprimindo um Sumário dos Dados
print(plantest_data.describe())