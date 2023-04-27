# from Cronometro import Cronometro
#
# with Cronometro("algoritmo"):
#    algoritmo(...)

# Exercício 1 Dado um array com os seguintes elementos
# ["zebra", "macaco", "elefante", "arara", "javali"],
# após duas iterações utilizando bubble sort, como estaria este array?

array = ["zebra", "macaco", "elefante", "arara", "javali"]


def bubble_sort(array):
    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False
        for i in range(len(array) - num_of_iterations - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True
        num_of_iterations += 1

    return array


if __name__ == "__main__":
    print(bubble_sort(array))
