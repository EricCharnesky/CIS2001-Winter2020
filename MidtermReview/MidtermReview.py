#7
def sum_of_even_columns(some_list):
    sum = 0
    for column_index in range(len(some_list[0])):
        column_sum = 0
        for row in some_list:
            column_sum += row[column_index]
        if column_sum % 2 == 0:
            sum += column_sum
    return sum

#8 - encapsulation - interact with public methods,
 # hide private details
  # work with the abstract public interface

#9
def _recursive_product(some_list, current_index, current_product):
    if current_index == 0:
        return some_list[0] * current_product
    return _recursive_product(some_list, current_index-1, current_product*some_list[current_index])

def recursive_product(some_list):
    return _recursive_product(some_list, len(some_list)-2, some_list[-1])

def better_recursive_product(some_list):
    if len(some_list) > 1:
        return some_list[0] * better_recursive_product(some_list[1:])
    return some_list[0]

print(recursive_product([1,2,3,4,5]))
print(better_recursive_product([1,2,3,4,5]))



# 10 - how to design a solution

# classes are objects - nouns in the problem definition
# class attributes are properties of the noun
# class methods are verbs of the noun


# 11 non recursive product
def iterative_product_of_list(some_list):
    product = some_list[0]
    for index in range(1, len(some_list)):
        product *= some_list[index]
    return product


#12 - three reasons inheritance is useful

# don't have to repeat work - rewrite functions
# cleaner solutions
# override parent class behavior or specialize child class behavior
# combine class behaviors in python


#13 - shallow copies are bad
# two variables pointed to the same list in memory

#14 - false- many base cases are allowed

#15 - O(1) - constant lookup time by index because we can read the memory address
