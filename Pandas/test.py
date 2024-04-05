import pandas as pd

reviews = pd.read_csv("Pandas/plantest.csv")
print(reviews.Valor_A)


# pd.set_option("display.max_rows", 5)

#print(pd.DataFrame(reviews.groupby('Valor_A')).Valor_A)
#pd.to_string(reviews.groupby('Valor_A').Valor_B)