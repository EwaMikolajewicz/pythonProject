print("Creating a new string by adding string s2: 'Python' inside s1: 'FullStack'")

s1 = "FullStack"
s2 = "Python"
mid = len(s1) // 2
new_s = s1[:mid] + s2 + s1[mid:]
print(new_s)
