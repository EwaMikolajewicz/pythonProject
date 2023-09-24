def max_nr_in_list(lista):
    m = lista[0]
    for i in range(len(lista)):
        if lista[i] > m:
            m = lista[i]
    return m


myList = [1, 5, -14, 21, 17, 2]
print(f"Max element of list: {myList} is {max_nr_in_list(myList)}")
