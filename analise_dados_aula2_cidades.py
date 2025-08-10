# Import necessary libraries
import pandas as pd
import numpy as np

# Senha Aula 2: 

#cria um dataframe
df_cidades = pd.DataFrame(
    {
        'nome' : ["leomar", "carol", "michele", "vando", "fatima"],
        'cidade' : ["sao paulo", np.nan, "curitiba", np.nan, "florianopolis"],
    }
)

df_cidades["cidade_preenchida"] = df_cidades['cidade'].fillna('Não Informado')

df_limpo = df_cidades.dropna().isnull().sum().head()

# print(df_cidades)
print(df_limpo.head().info())