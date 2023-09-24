def sum_of_el(list_of_nr):
    the_sum = 0
    for i in range(len(list_of_nr)):
        the_sum += list_of_nr[i]
    return the_sum


the_list = [1, 2, -8]
print(f"The sum of the list: {the_list} elements is {sum_of_el(the_list)}")
