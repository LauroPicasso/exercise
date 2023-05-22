import pandas as pd

data_dict = {
    "Grande Região": ["Norte", "Nordeste", "Sudeste", "Sul", "Centro-Oeste"],
    "Número de Municípios": [450, 1794, 1668, 1191, 467],
    "População em situação de rua": [4399, 22864, 49792, 16021, 8777],
    "Total de Municípios (%)": [8.10, 32.20, 29.90, 21.40, 8.40],
    "Total em situação de rua (%)": [4.32, 22.45, 48.89, 15.73, 8.62],
}

df = pd.DataFrame(data_dict)

# Quantas linhas e quantas colunas possui o nosso conjunto de dados?
df.shape

# Há valores nulos no DataFrame?
df.info()

# Qual o número médio de pessoas em situação de rua por região do Brasil
# # em nosso DataFrame?
df.describe()

# Qual região tem proporcionalmente
# a maior quantidade de pessoas nessa situação? E qual tem menos?
df.describe()
