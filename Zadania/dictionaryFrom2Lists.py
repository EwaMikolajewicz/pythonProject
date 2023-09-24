key_list = ['Dziesieć', 'Dwadzieścia', 'Trzydzieści']
value_list = [10,20,30]
if len(key_list) != len(value_list):
    print("Lengths of lists are not equal. Mission impossible.")
else:
    my_dict = {}
    for i in range(len(key_list)):
        my_dict.update({key_list[i]:value_list[i]})
    print(f"My dictionary from two lists:\nlist1: {key_list}\nlist2: {value_list}:\nDictionary: {my_dict}")