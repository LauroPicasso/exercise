dict_1 = dict()
dict_2 = {}

dict_1["string como chave"] = "qualquer coisa pode ser valor"
dict_1[1] = "inteiros podem ser chaves"
dict_1[(1, 2)] = "tuplas também podem ser chaves"

dict_2[["listas não"]] = 1
dict_2[{"conjuntos também não"}] = 2

print(dict_1.get(1))
print(dict_1.keys())
print(dict_1.values())
print(dict_1.items())
