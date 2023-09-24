def count_pal(the_list):
    count = 0
    for el in the_list:
        if len(el) >= 2 and el[0] == el[-1]:
            count = count + 1
    return count


list1 = ['abc', 'xyz', 'aba', '1221', 'aa', '2a2s2d2a2']
print(f"The number of elements in list {list1} with first and last sign the same is {count_pal(list1)}")
