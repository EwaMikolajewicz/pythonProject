x = int(input("Enter the first integer:\n"))
y = int(input("Enter the second integer:\n"))

a = max(x, y)
b = min(x, y)

while a > b:
    a = a - b
print(f"NWD of {x} and {y} is: {a}")
