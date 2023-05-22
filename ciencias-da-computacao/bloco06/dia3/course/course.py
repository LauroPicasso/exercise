import pandas as pd


def calcula_situacao(media):
    return "Aprovado" if media >= 7 else "Reprovado"


dicionario_de_notas = {
    "nome": ["Maria", "João", "Fernanda", "Túlio"],
    "primeira_nota": [9, 8, 7, 8],
    "segunda_nota": [8, 7, 9, 3],
}


dataframe = pd.DataFrame(dicionario_de_notas)

dataframe["media"] = (dataframe["primeira_nota"] + dataframe["segunda_nota"])/2

dataframe["situação"] = dataframe["media"].apply(calcula_situacao)

print(dataframe)
