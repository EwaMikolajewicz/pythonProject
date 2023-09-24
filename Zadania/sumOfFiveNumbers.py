print("Enter 5 numbers, and get their sum.")
list_of_numbers = []
for i in range(5):
    the_sum = 0
    x = float(input(f"podaj {i+1} liczbę:\n"))
    list_of_numbers.append(x)
    for nr in list_of_numbers:
        the_sum += nr
print(f"The sum of the given numbers is: {the_sum}")
