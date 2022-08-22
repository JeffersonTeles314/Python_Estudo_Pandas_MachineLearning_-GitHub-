import pandas as pd

# Salvando uma O Caminho do Arquivo em Uma Variável Para Lhor Acesso
melbourne_file_path = '../input/melbourne-housing-snapshot/melb_data.csv'
# Lendo os Dados e armazenando os Dados em um DataFrame Chamado melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path) 
# Imprimindo um Sumário dos Dados
melbourne_data.describe()
