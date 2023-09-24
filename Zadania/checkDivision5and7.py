list_of_numbers = []
for i in range(2000, 2701):
    if i % 7 == 0 and i % 5 == 0:
        list_of_numbers.append(i)
print(list_of_numbers)
