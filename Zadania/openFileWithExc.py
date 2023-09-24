try:
    f = open("plik.txt")
    s = f.readline()
    i = int(s.strip())
    print(i)
except FileNotFoundError:
    print("File not found.")
