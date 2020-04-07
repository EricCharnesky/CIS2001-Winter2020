def merge(left_side, right_side, list):
    left_index = 0
    right_index = 0
    while left_index + right_index < len(list):
        if right_index == len(right_side) or \
            ( left_index < len(left_side) and left_side[left_index] < right_side[right_index]):
            list[left_index+right_index] = left_side[left_index]
            left_index += 1
        else:
            list[left_index + right_index] = right_side[right_index]
            right_index += 1

def merge_sort(list):

    number_of_items = len(list)

    if number_of_items < 2:
        return

    middle_index = number_of_items // 2
    left_side = list[:middle_index]
    right_side = list[middle_index:]

    merge_sort(left_side)
    merge_sort(right_side)

    merge(left_side, right_side, list)

some_list = [41, 17, 11, 42, 0, 7, 24, 19]

print(some_list)
merge_sort(some_list)
print(some_list)






