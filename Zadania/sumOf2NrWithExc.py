while True:
    try:
        x = float(input("Enter first number:\n"))
        y = float(input("Enter second number:\n"))
        result = x + y
        print(f" {x} + {y} = {result}")
        break
    except ValueError as er:
        print(f"You should enter numbers,", er)
