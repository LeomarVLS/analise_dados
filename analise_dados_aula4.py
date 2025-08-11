import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pycountry as pycountry

# Senha Aula: PANDAS

# Importa CSV e Define o DataFrame
df = pd.read_csv('https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv')

# Printa constudo do CSV, tipos de como trazer as Infos do CSV
# print(df.head())
# print(df.info())
# print(df.describe())

# Modo de Printa as Linhas  e Colunas

lines, columns = df.shape[0], df.shape[1]

print('Linhas:', lines)
print('Colunas:', columns)

# print(df.columns)

# Dicionario para renomear as colunas e valores
colunas_renomeadas = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}

valor_senioridade = {
    'SE': 'Senior',
    'MI': 'Pleno',
    'EN': 'Junior',
    'EX': 'Executivo'
}

valor_contrato = {
    'FT': 'Tempo Integral',
    'PT': 'Tempo Parcial',
    'CT': 'contrato',
    'FL': 'Freela'
}

valor_remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'remoto'
}

valor_tamanho_empresa = {
    'L': 'Grande',
    'M': 'Média',
    'S': 'Pequena'
}

df.rename(columns=colunas_renomeadas, inplace=True)

# print(df["senioridade"].value_counts(), df["contrato"].value_counts(), df["remoto"].value_counts(), df["tamanho_empresa"].value_counts())

df["senioridade"] = df["senioridade"].replace(valor_senioridade)
df["contrato"] = df["contrato"].replace(valor_contrato)
df["remoto"] = df["remoto"].replace(valor_remoto)
df["tamanho_empresa"] = df["tamanho_empresa"].replace(valor_tamanho_empresa)

# print(df.head())

# Senha Aula 2: PRINT

# print(df.isnull().sum())

# print(df[df.isnull().any(axis=1)])

df_limpo = df.dropna().isnull().sum().head()

df_limpo = df.assign(ano = df_limpo['ano'].astype('int64'))

print(df_limpo.head())

# Senha Aula 3:

# agrupa os dados por senioridade e calculo a média do salário em usd
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index
ordem_senioridade = ['Junior', 'Pleno', 'Senior', 'Executivo']
media_salarial_senioridade_reset = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()
media_salarial_senioridade = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).index
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

# Configuração do gráfico Salario por Senioridade
plt.figure(figsize=(8, 5))
plt.title('Salário por médio Senioridade')
plt.xlabel('Nível de Senioridade')
plt.ylabel('Salário em usd Anual')
# df_limpo['senioridade'].value_counts().plot(kind='bar', title='Distribuição por Senioridade')
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem)

# Configuração do gráfico distribuição do salário Anuais
plt.figure(figsize=(8, 4))
plt.title('distribuição do salário Anuais')
plt.xlabel('Salário em usd')
plt.ylabel('Frequência')
sns.histplot(df_limpo['usd'], bins=50, kde=True)

# Configuração do gráfico salario Anual em Boxplot
plt.figure(figsize=(8, 5))
plt.title('Distribuição do Salárial por Senioridade')
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade')
plt.xlabel('Senioridade')
plt.ylabel('Salario em usd')

# Configuração do gráfico salario Anual em Boxplot
plt.figure(figsize=(8, 5))
plt.title('Distribuição do Salárial por Senioridade')
sns.barplot(x='senioridade', y='usd', data=df_limpo, order=media_salarial_senioridade)
plt.xlabel('Senioridade')
plt.ylabel('Salario Anual')

# Configuração do gráfico salario Anual em Boxplot iterativo, funcionando somente no colab
# fig = px.bar(media_salarial_senioridade,
#         x='senioridade',
#         y='usd', color='senioridade',
#         title='Distribuição do Salárial por Senioridade',
#         labels={'senioridade': 'nivel de Senioridade', 'usd': 'Salário em usd'}
# )

# Configuração do gráfico quandidade remoto por quantidade, em grafico de pizza
# plt.figure(figsize=(8, 5))
# plt.title('Proporção de Trabalho Remoto')
# plt.pie(remoto_contagem['quantidade'], labels=remoto_contagem['tipo_trabalho'], autopct='%1.1f%%', startangle=90)


# Configuração do gráfico quandidade remoto por quantidade, em grafico de pizza, funcionando somente no colab
fig = px.pie(remoto_contagem,
        names='tipo_trabalho',
        values='quantidade',
        title='Proporção de Trabalho Remoto',
        hole=0.5,
)

df_limpo.head()

#cria função
def iso2_to_iso3(code):
  try:
    return pycountry.countries.get(alpha_2=code).alpha_3
  except:
    return None

# cria nova coluna Codigo ISO 3
df_limpo['residencia_iso3'] = df_limpo['residencia'].apply(iso2_to_iso3)

# calcula media salarial por país (ISO 3)
df_ds = df_limpo[df_limpo['cargo'] == 'Data Scientist']
media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()

# Gera grafico em Mapa, funcionando somente no colab
# fig_maps = px.choropleth(media_ds_pais,
#                     locations='residencia_iso3',
#                     color='usd',
#                     color_continuous_scale='rdylgn',
#                     title='Média Salarial por País',
#                     labels={'usd': 'Salário em usd', 'residencia_iso3': 'País'}
#                     )

# Exibe o gráfico importando a biblioteca matplotlib
plt.show()
# fig.show()
# fig_maps.show()