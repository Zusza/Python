# Przykładowe zadania NWD (można używać gcd, lcm)

# 1. Dodaj dwa ułamki
# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
# c = int(input("Podaj c: "))
# d = int(input("Podaj d: "))

# x = b
# y = d
# iloczyn = x * y
# while y > 0:
#   x, y = y, x % y
# nww = iloczyn // x

# e = (nww // b) * a
# f = (nww // d) * c
# g = e + f

# print(f"{a}/{b} + {c}/{d} = {e}/{nww} + {f}/{nww} = {g}/{nww}")

# 2. Dodaj trzy ułamki
# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
# c = int(input("Podaj c: "))
# d = int(input("Podaj d: "))
# e = int(input("Podaj e: "))
# f = int(input("Podaj f: "))

# x = b
# y = d
# z = f
# iloczyn = x * y * z
# while y > 0:
#   x, y = y, x % y
# nww = iloczyn // x

# t = (nww // b) * a
# w = (nww // d) * c
# q = (nww // f) * e
# g = t + w + q

# print(f"{a}/{b} + {c}/{d} + {e}/{f} = {t}/{nww} + {w}/{nww} + {q}/{nww} = {g}/{nww}")

# 3. Skróć ułamek
# import math
# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
# c = math.gcd(a,b)
# d = a//c
# e = b//c
# print(f"Skrócony ułamek: {d}/{e}")

# 4. Zamień ułamek niewłaściwy na liczbę mieszaną i skróć o ile się da
# import math
# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
# c = a//b
# d = a%b
# e = math.gcd(d,b)
# a = d//e
# b = b//e
# print(f"Całości {c}, Ułamek: {a}/{b}")

# 5. Ułamki szwajcarskie - mianowniki to liczby dwucyfrowe, liczniki to sumy cyfr mianowików. Ułamek jest szwajcarski gdy można go skrócić do formy 1/minownik. Wypisać je wszystkie: 3/12, 9/18 itd....
# import math
# L = []
# for i in range(10,100):
#   a = i//10 + i%10
#   nwd = math.gcd(a, i)
#   a = a//nwd
#   b = i//nwd
#   if a == 1 and b%10 == b:
#     if str(a)+"/"+str(b) not in L:
#       L.append(str(a)+"/"+str(b))
# print(L)

# 6. Ułamki austriackie - rozważamy wszystkie liczby dwucyfrowe. Liczniki to iloczyny, a mianowniki różnice kolejnych liczb dwucyfrowych. Pewne liczby nie dadzą ułmków austrickich, np. 10, 33 (w liczniku lub mianowniku byłoby zero). Ułamek jest austriacki gdy jest niewłaściwy i da się go jakkolwiek skrócić, np 19/8, 24/2 ... Wypisz wszystkie ułamki austriackie
# import math
# L = []
# F = []
# for i in range(2,10):
#   for j in range(1,i):
#     L.append(str(i) + str(j))
# for l in L:
#   i = int(l)
#   a = i//10
#   b = i%10
#   c = a*b
#   d = a-b
#   nwd = math.gcd(c,d)
#   c = c//nwd
#   d = d//nwd
#   if str(c) + "/" + str(d) not in F:
#     F.append(str(c) + "/" + str(d))
# print(F)

# Ułamki egipskie:
# li, mi = int(input()), int(input())
# a, b = li, mi
# from math import ceil, gcd
# L = []
# while li > 0:
#     x = ceil(mi/li)
#     L.append(x)
#     nww = mi * x // gcd(mi, x)
#     # li/mi - 1/x
#     li = (nww // mi) * li
#     mi = nww
#     y = nww // x
#     li = li - y

# print(f"{a}/{b}", end= " = ")
# for x in L:
#     print(f"1/{x}", end= " + ")

# Zadania do rozwiązania na kartce
# 1. Napisz algorytm nwd odejmowanie / modulo i przeprowaź symulacje kroków dla a = 24 i b = 64
# a = int(input())
# b = int(input())
# while a != b:
#   if a > b : a = a - b
#   elif b > a : b = b - a
# print(a)

# Symulacja:
# 64 | 24
# 24 | 40
#  8 | 16
#  8 | 8
#  8 |


# MOJE - wspólny mianownik
# a = int(input("Podaj ułamek1: "))
# b = int(input("Podaj ułamek1: "))

# c = int(input("Podaj ułamek2: "))
# d = int(input("Podaj ułamek2: "))

# e = int(input("Podaj ułamek3: "))
# f = int(input("Podaj ułamek3: "))

# x = b
# y = d
# ilo = x * y
# while y > 0:
#   x, y = y, x % y
# nww = ilo // x
# w = (nww // b) * a
# q = (nww // d) * c
# h = (nww // f) * e
# if nww < 100:
#   print("Wspólny mianownik ma wartość poniżej 100")
# else:
#   print("Wspólny mianownik nie ma wartości poniżej 100")
