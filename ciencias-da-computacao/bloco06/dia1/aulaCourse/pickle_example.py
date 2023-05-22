import pickle

dict_1 = dict()

dict_1[["felps"]] = "listas não podem ser chaves"

a = pickle.dumps(["felps"])

print(a)

dict_1[a] = "listas não podem ser chaves"

print(dict_1)

for x in dict_1:
    print(x)
    print(pickle.loads(x))
