value = 10000
percent = 8
years = 3
result = value*(1+percent/100)**years
print(result-value)

val1 = 'Hello'
val2 = 5
print(val1*val2)
print('Byłam wczoraj na filmie "AAA"')
print('I\'m')
n = 'First line.\nSecond line.'
print(n)
t = '\tTab line.'
print(t)
print('C:\some\name')
print(r'C:\some\name')
x = 36  # x to temperatura
print(x)
y = 48
""" y to wiek """
print(y)
z = 65
'''
z to waga
z to waga
z to waga
z to waga
z to waga
'''
print(z)

word = 'Python'
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
print(word[0:2])

for i in range(0, len(word)):
    print(word[i])

name = 'Adela'
if name[-1] == 'a':
    print('Imie damskie')

print(word[:2])
print(word[2:])
print(word[:2] + word[2:])

word1 = 'Python'
word2 = 'J' + word1[1:]
print(word2)

s = 'jdhgfhkjhoexwbycrbwnxdmozo,omouxfuxgehd   dhngfnlamdz,;'
s_len = len(s)
print(s_len)
print(s[s_len-1])

lata = input()
oprocentowanie = input("wprowadź oprocentowanie: ")
print(lata)
print(oprocentowanie)

imie = input("podaj imie:\n")
wiek = input("podaj wiek:\n")
print('Twoje imię to ' + imie + '. Twój wiek to ' + wiek)

squares = [1, 4, 9, 16, 25]
print(squares)

squares1 = [1, 4, 9, 'a', 25]
print(squares1)
print(squares[0])
print(squares[-1])
print(squares[1:])
print(squares[2:])
print(squares[len(squares)-1])

lista_suma1 = squares + squares1
print(lista_suma1)

lista_suma2 = squares1 + squares
print(lista_suma2)

cubes = [1, 8, 27, 65, 125]
print(cubes)
cubes[3] = 64
print(cubes)
print(len(cubes))
cubes.append(216)
print(cubes)
print(len(cubes))
cubes.append(7**3)
print(cubes)
print(len(cubes))
litery = ['a', 'b', [1, 3]]
liczby = [1, 2, 3]
razem1 = litery + liczby
razem2 = [litery, liczby]
print(razem1)
print(razem2)
print(type(razem1))
print(type(razem2))
