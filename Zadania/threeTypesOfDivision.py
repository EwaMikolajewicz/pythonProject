a = float(input("Enter the numerator:\n"))
b = float(input("Enter the denominator:\n"))

if b == 0:
    print("The denominator cannot be zero. Division is impossible..")
elif a == int(a) and b == int(b):
    print(f"{int(a)} / {int(b)} = {a / b}")
    print(f"{int(a)} % {int(b)} = {int(a % b)}")
    print(f"{int(a)} // {int(b)} = {int(a // b)}")
else:
    print(f"{a} / {b} = {a/b}")
    print(f"Division remainder and integer division are only possible for integers.")
