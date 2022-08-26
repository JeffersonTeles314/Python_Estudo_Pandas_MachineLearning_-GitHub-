
#Parte 1.0 - Importando a Biblioteca
import pandas as pd

# Parte 3.0 - Criando um Dataframe do Zero
Testframe = pd.DataFrame(
{
'Coluna1': ['0', '1'], 
'Coluna2': ['1', '0']
},
index=['Linha1', 'Linha2']
)


# Imprimindo um Sumário dos Dados
print("***Print Test Dataframe***")
print(Testframe)
Testframe.loc['Linha1','Coluna1'] = "Teste"
print("***Print Test Dataframe***")
print(Testframe)

