x = float(input("Enter first number:\n"))
y = float(input("Enter second number:\n"))
try:
    result = x / y
    print(f" {x} / {y} = {result}")

except ZeroDivisionError:
    print("Do not divide by zero!")
