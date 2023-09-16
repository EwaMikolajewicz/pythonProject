# a = 2>1
# print(a)
# print(type(a))

# x = 1
# y = 2.5
# print(x + y)

# str1 = "Datatypes"
# mid_str1 = len(str1)//2
# print(str1[mid_str1-1:mid_str1+2])

# s1 = "FullStack"
# s2 = "Python"
# mid_s = len(s1) // 2
# s = s1[:mid_s] + s2 + s1[mid_s:]
# # s = s1[:4] + s2 + s1[4:]
# print(s)

# zbior1 = {"ala","zosia",3,3,3,3,3,3}
# zbior2 = {2, "ala"}
# print(zbior2 | zbior1)
# print(len(zbior1))

# age = 20
# print(f"Masz {age} lat")

# print(3 == "3")
# print (3 == 3)
#
# def silnia(x):
#     if x == 0:
#         return 1
#     else:
#         return x*silnia(x-1)
#
#
# x = int(input("podaj liczbę całkowitą nieujemną: "))
# print(f"Silnia z {x} wynosi {silnia(x)}")

# x = int(input("Podaj swój wynik egzaminu: "))
# if x>= 90:
#     ocena = '5'
# elif x>= 75:
#     ocena = '4'
# elif x>= 60:
#     ocena = '3'
# else:
#     ocena = '2'
# print(f"Twój wynik to: {x}. Twoja ocena to: {ocena}")

# is_driver_licence = False
# age = 20
# if age >= 18 and is_driver_licence is False:
#     print("ok")
# else:
#     print("nie ok")

# string = "Python"
# for li in string:
#     print("litera:",li)

# lista = [1,2,3,45]
# for element in lista:
#     print(element)
# print("koniec")

# for i in [1,2,3]:
#     print("zewnątrz:",i)
#     for j in [4,5,6]:
#         print("wewnątrz:",j)
#     print("koniec pętli wewnętrznej")
# print("koniec pętli zewnętrznej")

# str = "Python ,gfd , iy ,"
# strbez = ""
# for sign in str:
#     if sign != ',':
#         strbez += sign
# print(strbez)

# x = 5
# while x >=0:
#     print(x)
#     x = x - 1

# x = 8
# y = 15
# if x > 3 or y % 2 == 0:
#     print("Co najmniej jeden warunek jest spełniony")
# else:
#     print("Żaden warunek nie jest spełniony")

# Ćwiczenie nr:
# Napisz program, w którym:
# * Utwórz listę zawierającą imiona: prowadzącego oraz lilku osób uczestniczacych w kursie
# * Następnie ją posortuj alfabetycznie, oraz
# * Policz ile z osób na liście jest imion żeńskich
#     * W tym celu możesz sprawdzić czy imię kończy się na „`a`”
# names = ['Kamil', 'Wojciech', 'Małgorzata', 'Mateusz', 'Grzegorz', 'Bogdan', 'Katarzyna', 'Damian', 'Anatolii', 'Anna', 'Paweł', 'Marta', 'Justyna', 'Ilona', 'Daniel']
# names.sort()
# len(names)
# count = 0
# for name in names:
#     if name[-1] == 'a':
#         count += 1
# print(f"Liczba imion żeńskich na liście: {count}")

# list = []
# for dig in range(2000,2701):
#     if dig % 5 == 0 and dig % 7 == 0:
#         list.append(dig)
# print(list)


# x = int(input("Podaj liczbę:"))
# sum = 0
# for i in range(1, x+1):
#     sum += i
# print(f"Suma liczb od 1 do {x} to: {sum}")

# num = int(input("Podaj liczbę: "))
# for i in range(1,11):
#     i *= num
#     print(i)

# def print_hello(i):
#     print("Hello"*i)


# print_hello(5)

def power(x,y=2):
    return x ** y

# x = int(input("podaj liczbę1:"))
# y = int(input("podaj liczbę2:"))
result = power(2)
print(result)
result = power(2,5)
print(result)
