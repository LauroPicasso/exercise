# A função sum_array recebe um array de números,
# percorre-o e executa a soma de cada um de seus valores (number),
# retornando a soma de todos os números pertencentes ao array.
def sum_array(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum


def squared_array(numbers):
    array_of_squares = []
    for number in numbers:
        array_of_squares.append(number * number)

    return array_of_squares


def multiply_array(numbers):
    result = 1
    for number in numbers:
        result *= number

    return result


# Os arrays têm sempre o mesmo tamanho
def multiply_arrays(array1, array2):
    result = []
    for number1 in array1:
        for number2 in array2:
            result.append(number1 + number2)

    return result
