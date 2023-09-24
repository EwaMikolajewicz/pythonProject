kp = float(input("Enter initial capital:\n"))
years = int(input("Enter number of years:\n"))
ir = float(input("Enter interest rate:\n"))
kk = kp * (1 + ir / 100) ** years
profit = round(kk - kp, 2)
print(f"Your profit from initial capital {kp} PLN "
      f"after {years} years is {profit} PLN")
