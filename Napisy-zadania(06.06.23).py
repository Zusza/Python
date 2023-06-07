# # Zad.1 - Wczytaj dowolny napis i wypisz z niego pierwszą i ostatnią literę
# n = input("Podaj napis: ")
# # Sposób #1:
# print(n[0], n[-1])
# # Sposób #2:
# print(n[0], n[len(n)-1])

# # Zad.2 - Wczytaj dowolny napis i wypisz z niego literki bez pierwszej i ostatniej
# m = input("Podaj napis: ")
# # Sposób #1:
# print(m[1:-1])
# # Sposób #2:
# print(m[1:len(m)-1])
# # Sposób #3:
# for i in range(1, len(m)-1):
#   print(m[i],end=" ")

# # Zad.3 - Wypisz 4 ostatnie litery z wpisanego napisu w kolejności od końca
# c = input("Podaj napis: ")
# # Sposób #1:
# print(c[-1:-5:-1])
# # Sposób #2:
# print(c[:-5:-1])
# # Sposób #3:
# for i in range(len(c)-1, len(c)-5, len(c)-1):
#   print(c[i])
# # Sposób #4:
# C = list(c)
# C.reverse();
# c = "".join(C)
# print(C[:4])

# # Zad.4 - Waga napisu to suma kodów ASCII jego liter. Zważ wpisany napis
# d = input("Podaj napis: ")
# s = 0
# # Sposób #1:
# for i in d:
#   s+= ord(i)
# print(s)

# # Zad.5 - Policz ile we wpisanym napisie jest liter "A"
# e = input("Podaj napis: ")
# ilosc = 0
# # Sposób #1:
# for i in e:
#   if i == "A":
#     ilosc += 1
# print(ilosc)

# # Zad.6 - Podaj dominującą liter we wpisanym napisie. (Niech to będzie tylko jedna literka)
# f = input("Podaj napis: ")
# m = 0
# for x in f:
#   if f.count(x) > m:
#     m = f.count(x)
#     liter = x
# print(liter, m)

# # Zad.7 - Znajdź literę-dominantę w napisie (może być ich kilka, lub żaden)
# def CzyJestMniej(L): # <-- Funkcja
#   for x in L:
#     if 0 < L.count(x) < max(L):
#       return True
#   return False

# g = input("Podaj napis: ")
# K = [0] * 100
# for x in g:
#   K[ord(x)] += 1
# domi = max(K)
# if sum(K) == max(K):
#   print("Dominanta: ", chr(K.index(max(K))))
# elif not CzyJestMniej(K):
#   print("Brak dominanty")
# else:
#   D = []
#   for i in range(len(K)):
#     if K[i] == max(K):
#       D.append(chr(i))
#   print("Dominanty:", ", ".join(D))

# # Zad.8 - Sprawdź czy w napisie występują 3 podciągi "LA"
# h = input("Podaj napis: ")
# T = list(h)
# ilo = 0
# for i in range(len(h)-1):
#   j = i+1
#   if (T[(i]=="L" and T[j]=="A") or (T[i]=="l" and T[j]=="a") or (T[i]=="L" and T[j]=="a") or (T[i]=="l" and T[j]=="A"):
#      ilo += 1
# if ilo >= 3:
#   print("Tak, ", ilo)
# else:
#   print("Nie")

# # Zad.9 - Znajdź "średnią literę" w napisie. (Przejdź na kod ASCII i jeśli wynik będzie ułamkowy to zaokrąglij średnią dół)
# x = input("Podaj napis: ")
# x = x.lower()
# dl = len(x)
# srindex = dl // 2
# if dl % 2 == 0:
#     srlitera = x[srindex - 1]
# else:
#     srlitera = x[srindex]
# print("Średnia litera:", srlitera)

# # Zad.10 - Wypisz literki, których nie ma w napisie.
# # Sposób #1:
# def znajbraku(x):
#     x = x.lower()
#     alpf = 'abcdefghijklmnopqrstuvwxyz'
#     brakulite = ''
#     for litera in alpf:
#         if litera not in x:
#             brakulite += litera
#     return brakulite
# text = input("Podaj napis: ")
# brakulite = znajbraku(text)
# if brakulite:
#     print("Brakujące litery:", brakulite)
# else:
#     print("Nie ma brakujących liter w tekście.")

# # Sposób #2:
# x = input("Podaj napis: ")
# x = x.lower() # <-- zmienia wszystkie litery na małe
# alpf = "abcdefghijklmnopqrstuvwxyz"
# brakuli = ""
# for litera in alpf:
#     if litera not in x:
#         brakuli += litera
# if brakuli:
#     print("Brakujące litery:", brakuli)
# else:
#     print("Nie ma brakujących liter w tekście.")

# # Zad.11 - Znajdź ilość trzyznakowych palindromów w napisie (3 litery obok siebie)
# x = input("Podaj napis: ")
# x = x.lower()
# y = 0
# for i in range(len(x) - 2):
#     if x[i] == x[i + 2]:
#         y += 1
# print("Ilość trzyznakowych palindromów w napisie:", y)

# Zad.1-Gr.1-Rozważamy wszystkie słowa, które posiadają dokładnie dwa takie same znaki oraz pozostałe znaki inne niż wspomniana para. Np baza, matka, barszcz.Wypisz wszystkie znaki ze słowa, które znajdują się między parą takich samych znaków.

# Zad.2-Przekształć podane słowo do postaci paro-tylnej. Dzielimy słowo na pary znaków od końca. Każdą parę wypisujemy w kolejności odwrotnej i w ten sposób tworzymy nowe słowo
# n = input("Podaj napis: ")
# s = ""
# dl = len(n)
# for i in range(dl - 1, 0, -2):
#   s += n[i]
#   s += n[i - 1]
# if dl % 2 != 0:
#   s += n[0]
# print(s)

# Zad.3-Sprawdź czy podane przez usera słowo jest niemalejące alfabetycznie, czyli czy każda kolejna literka w nim jest alfabetycznie nie mniejsza niż poprzednia. Np: adek, ery, deep
# n = input("Podaj napis: ")
# a = True
# for i in range(len(n) - 1):
#   if ord(n[i]) < ord(n[i + 1]):
#     a = False
# if a:
#   print("Napis jest nierosnący alfabetycznie")
# else:
#   print("Napis nie jest nierosnący alfabetycznie")

# Zad.1-Gr.2-Użytkownik wprowadza dwa słowa. Sprawdź czy pierwsze z nich jest zawarte w drugim
# n = input("Podaj napis: ")
# m = input("Podaj napis: ")
# if n in m or m in n:
#   print("Jedno słowo jest zawarte w drugim słowie")
# else:
#   print("Jedno słowo nie jest zawarte w drugim słowie")

# Zad.2-Sprawdź czy z podzbioru liter wpisanego przez usera słowa da się utworzyć słowo "baza"
# n = input("Podaj napis: ").lower()
# b = "baza"
# zn = set(n)
# d = True
# for i in b:
#   if i not in zn:
#     d = False
#     break
# if d:
#   print("Da się utworzyć słowo 'baza'")
# else:
#   print("Nie da sie utworzyć słowa 'baza'")

# Zad.3-Wypisz wszystkie wyrazy, które powstają z podanego przez usera słowa poprzez usunięcie duplikatów liter
# Wypisuje KAŻDĄ możliwą opcję
# import itertools
# n = input("Podaj napis: ").lower()
# w = set()
# for i in n:
#   if i not in w:
#     w.add(i)
# for i in range(1, len(w)+1):
#   for j in itertools.permutations(w,i):
#     w2 = ''.join(j)
#     if w2 != n:
#       print(w2)
