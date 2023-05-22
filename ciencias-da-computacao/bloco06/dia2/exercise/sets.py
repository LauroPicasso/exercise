set_1 = set()
set_2 = {1, 2, 3, 4, 5, 6}
set_3 = {value for value in range(1, 10)}

dir(set_1)

set_1.add(5)
set_1.add(6)
set_1.add(7)
set_1.add(8)

print(dir(set_1))

print(set_1.union(set_2))
print(set_1.intersection(set_2))
print(set_1.difference(set_2))
print(set_2.difference(set_1))
