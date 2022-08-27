#Importando a Biblioteca
import pandas as pd

# Salvando uma O Caminho do Arquivo em Uma Variável Para Melhor Acesso
plantest_caminho_arqv = 'Pandas/plantest.csv'

# Lendo os Dados de um "csv", e armazenando em um DataFrame.
csv_data = pd.read_csv(plantest_caminho_arqv) 

Testframe = pd.DataFrame(
{
'Coluna1': ['0', '1'], 
'Coluna2': ['1', '0']
},
index=['Linha1', 'Linha2']
)

#Alterando o Valores de uma das Colunas.
csv_data.loc[[0,1],['Valor A','Valor B']] = Testframe

#Imprimindo os Valores Novamente
print("***Print Describe CSV***")
print(Testframe)
print(csv_data)

