# Import necessary libraries
import pandas as pd
import numpy as np

# Senha Aula 2: 

#cria um dataframe
df_temperatura = pd.DataFrame(
    {
        'dia_semana' : ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"],
        'temperatura' : [np.nan, np.nan, np.nan, 21.5, 20.0]
    }
)
# calcula a média e mediana das temperaturas, substituindo NaN por esses valores
df_temperatura['temperatura_media'] = df_temperatura['temperatura'].fillna(df_temperatura['temperatura'].mean().round(2))
df_temperatura['preenchido_ffill'] = df_temperatura['temperatura'].ffill()
df_temperatura['preenchido_bfill'] = df_temperatura['temperatura'].bfill()

print(df_temperatura)