names = ['Kamil', 'Wojciech', 'Małgorzata', 'Mateusz', 'Grzegorz',
         'Bogdan', 'Katarzyna', 'Damian', 'Anatolii', 'Anna',
         'Paweł', 'Marta', 'Justyna', 'Ilona', 'Daniel']
sorted(names)
count = 0
for el in names:
    if el[-1] == "a":
        count += 1
print(f"Sorted list: {sorted(names)}")
print(f"Number of females names in list: {count}")
