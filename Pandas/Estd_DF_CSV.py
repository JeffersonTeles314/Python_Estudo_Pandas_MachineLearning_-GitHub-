#Importando a Biblioteca
import pandas as pd

# Salvando uma O Caminho do Arquivo em Uma Variável Para Melhor Acesso
plantest_caminho_arqv = 'Pandas/plantest.csv'

# Lendo os Dados de um "csv", e armazenando em um DataFrame.
csv_data = pd.read_csv(plantest_caminho_arqv) 

#Imprimindo os Valores
print("***Print Describe CSV***")
print(csv_data)

#Alterando o Valores de uma das Colunas.
csv_data['Valor A'] = range(len(csv_data), 0, -1)

#Imprimindo os Valores Novamente
print("***Print Describe CSV***")
print(csv_data)

