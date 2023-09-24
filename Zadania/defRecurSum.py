def recur_sum(number):
    if number == 0:
        return 0
    return number + recur_sum(number - 1)


number = 3
print(f"Sum of first {number} numbers is {recur_sum(number)}")
