nr = int(input("Enter integer number not equal zero:\n"))
print(f"Multiplication table for your number {nr}:")
for i in range(1, 11):
    i *= nr
    print(i)
