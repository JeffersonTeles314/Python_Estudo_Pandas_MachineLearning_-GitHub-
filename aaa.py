import pandas as pd

# Exemplo de DataFrame
data = {
    'Tribunal': ['TJAC', 'TJSP', 'TJAC', 'TJMG'],
    'Caso': ['Caso 1', 'Caso 2', 'Caso 3', 'Caso 4']
}

df = pd.DataFrame(data)

# Filtrando o DataFrame para linhas onde o Tribunal é 'TJAC'
linha_TJAC = df[df['Tribunal'] == 'TJAC']

# Iterando sobre as linhas filtradas corretamente
for index, row in linha_TJAC.iterrows():
    # Acessando os valores das colunas
    tribunal = row['Tribunal']
    caso = row['Caso']
    print(f'Tribunal: {tribunal}, Caso: {caso}')