print("Creating a new string by adding first, middle and last character from string s1: 'America' and s2: 'Japan'")
s1 = "America"
s2 = "Japan"
mid1 = len(s1) // 2
mid2 = len(s2) // 2
new_s = s1[0] + s2[0] + s1[mid1] + s2[mid2] + s1[-1] + s2[-1]
print(new_s)