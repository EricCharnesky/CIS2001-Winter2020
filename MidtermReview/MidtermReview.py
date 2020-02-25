#1.	Eric Charnesky says do not cheat!

#2.	Because the position has the Node behind the scenes ( is a wrapper class around Node), you can add/remove around a node in a linked list in O(1)

#3.	Class Course:

class Course:
def __init__(self):
	self.Name = “”
	self.Number = “”
	self.Credits = 0
	self.Cost_per_credit = 0

def get_total_cost(self):
	return self.Credits * self._cost_pre_credit

#4 – 
# AAA
#Arrange
Expected_credits = 4
Cost_per_credit =500
Expected_cost_for_course = 2000

#act
Cis2001 = Course()
Cis2001.Credits = expected_credits
Cis2001.cost_per_credit = cost_per_credit
Actual_cost = cis2001.get_total_cost()

#assert
Self.assertEqual(expected_cost_for_course, actual_cost)

#5.	Exhaustive enough to ensure every line of code is run when the tests are run.
#Because we don’t trust the code we right to be accurate

#6.	O(N) – because you have to fill the blank space by shifting everything after the index back


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
