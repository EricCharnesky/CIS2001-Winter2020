import sys

some_list = []

print(sys.getsizeof(some_list))

for n in range(100):
    print("n: {} - size: {}".format(n, sys.getsizeof(some_list)))
    some_list.append(n)


some_big_number = 1_000_000_000
some_big_list = [None] * some_big_number



