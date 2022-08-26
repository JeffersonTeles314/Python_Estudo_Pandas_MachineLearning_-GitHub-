
#Parte 1.0 - Importando a Biblioteca
import pandas as pd

# Parte 2.0 - Salvando uma O Caminho do Arquivo em Uma Variável Para Lhor Acesso
plantest_caminho_arqv = 'Pandas/plantest.csv'

# Parte 3.0 - Criando um Dataframe do Zero
Testframe = pd.DataFrame(
{
'Coluna1': ['0', '1'], 
'Coluna2': ['1', '0']
},
index=['Linha1', 'Linha2']
)

# Parte 3.1 - Lendo os Dados de um "csv", e armazenando em um DataFrame.
csv_data = pd.read_csv(plantest_caminho_arqv) 

# Imprimindo um Sumário dos Dados
print("***Print Test Dataframe***")
print(Testframe)

print("***Print Describe CSV***")
print(csv_data)

print("***Print Describe CSV***")
print(csv_data.describe())

