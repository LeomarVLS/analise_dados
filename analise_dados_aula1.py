import pandas as pd

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
    'work_year': 'Ano',
    'experience_level': 'Senioridade',
    'employment_type': 'Contrato',
    'job_title': 'Cargo',
    'salary': 'Salario',
    'salary_currency': 'Moeda',
    'salary_in_usd': 'USD',
    'employee_residence': 'Residencia',
    'remote_ratio': 'Remoto',
    'company_location': 'Empresa',
    'company_size': 'Tamanho_empresa'
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
    'CT': 'Contrato',
    'FL': 'Freela'
}

valor_remoto = {
    0: 'Presencial',
    50: 'Híbrido',
    100: 'Remoto'
}

valor_tamanho_empresa = {
    'L': 'Grande',
    'M': 'Média',
    'S': 'Pequena'
}

df.rename(columns=colunas_renomeadas, inplace=True)

# print(df["Senioridade"].value_counts(), df["Contrato"].value_counts(), df["Remoto"].value_counts(), df["Tamanho_empresa"].value_counts())

df["Senioridade"] = df["Senioridade"].replace(valor_senioridade)
df["Contrato"] = df["Contrato"].replace(valor_contrato)
df["Remoto"] = df["Remoto"].replace(valor_remoto)
df["Tamanho_empresa"] = df["Tamanho_empresa"].replace(valor_tamanho_empresa)

# print(df["Senioridade"].value_counts(), df["Contrato"].value_counts(), df["Remoto"].value_counts(), df["Tamanho_empresa"].value_counts())

print(df.describe(include='object'))

print(df.describe())