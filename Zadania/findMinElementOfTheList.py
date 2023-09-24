def min_nr_in_list(lista):
    m = lista[0]
    for i in range(len(lista)):
        if lista[i] < m:
            m = lista[i]
    return m


myList = [1, 5, -14, 2100, -34, 2]
print(f"Min element of list: {myList} is {min_nr_in_list(myList)}")
