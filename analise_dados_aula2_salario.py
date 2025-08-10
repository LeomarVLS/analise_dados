# Import necessary libraries
import pandas as pd
import numpy as np

# Senha Aula 2: 

#cria um dataframe
df_salarios = pd.DataFrame(
    {
    'nome': ["Leomar", "Carol", "Michele", "Vando", "Fatima"],
    'salario': [4000, np.nan, 5000, np.nan, 100000],
    }
)

# calcula a média e mediana dos salários, substituindo NaN por esses valores
df_salarios['salario_media'] = df_salarios['salario'].fillna(df_salarios['salario'].mean().round(2))
df_salarios['salario_mediana'] = df_salarios['salario'].fillna(df_salarios['salario'].median())

print(df_salarios)