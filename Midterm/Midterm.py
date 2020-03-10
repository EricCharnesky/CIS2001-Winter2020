


def sum_of_values_in_even_product_of_indexes( some_2d_list ):
    sum = 0
    for row_index in range(len(some_2d_list)):
        for column_index in range(len(some_2d_list[row_index])):
            if row_index * column_index % 2 == 0 and row_index != 0 and column_index != 0:
                sum += some_2d_list[row_index][column_index]
    return sum

some_list = [
[ 1, 2, 3, 4 ],
[ 5, 6, 7, 8 ],
[ 1, 2, 1, 2 ] ]

print(sum_of_values_in_even_product_of_indexes(some_list))


def sum_of_ordinal_values_in_string( some_string ):
    if len(some_string) == 1:
        return ord(some_string[0])
    return ord(some_string[0]) + sum_of_ordinal_values_in_string(some_string[1:])

print(sum_of_ordinal_values_in_string('Eric'))
for letter in "Eric":
    print(ord(letter))