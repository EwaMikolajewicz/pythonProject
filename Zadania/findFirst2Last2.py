def find_first2_last2(the_list):
    if len(the_list) < 2:
        return ""
    else:
        return the_list[:2] + the_list[-2:]


list1 = "CodeBrainers"
print(find_first2_last2(list1))
list2 = "CB"
print(find_first2_last2(list2))
list3 = "C"
print(find_first2_last2(list3))

