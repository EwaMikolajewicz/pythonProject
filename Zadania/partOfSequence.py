str1 = input("Enter sequence of signs:\n")
if len(str1) > 7 and len(str1) % 2 != 0:
    mid = len(str1) // 2
    new_str = str1[mid - 1:mid + 2]
    print(f"The three middle characters of this sequence are: {new_str}")
elif len(str1) < 7:
    print("This sequence is too short.")
else:
    print(f"This sequence has an even ({len(str1)}) number of signs.")
