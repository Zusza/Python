# Generator tablicy:
import random

liczby = 40
L = []
for i in range(liczby):
  L.append(random.randint(10, 100))

# Zad.1
# # Iteracyjnie:
# max = 0
# for i in L:
#   if i > max:
#     max = i
# print(max)
# # Funkcja:
# print(max(L))

# Zad.2
# # Iteracyjnie:
# mini = 100
# for i in L:
#   if i < mini:
#     mini = i
# print(mini)
# # Funkcja:
# print(min(L))

# Zad.3
# # Iteracyjnie:
# mini = 100
# max = 0
# for i in L:
#   if i > max:
#     max = i
# for i in L:
#   if i < mini:
#     mini = i
# x=max-mini
# print(x)
# # Funkcja:
# print(len(L))

# Zad.4
# # Iteracyjnie:
# max = 0
# vmax = L[0]
# for i in L:
#     if i > vmax and i < max:
#         vmax = i
# print(vmax)
# # Funkcja:
# S = (list(set(L))
# print(S(len(S)-2)) <- Nie działa

# Zad.5
# # Iteracyjnie:
# mini = 0
# vmini = L[0]
# for i in L:
#   if i < vmini and i > mini:
#     vmini = i
# print(vmini)
# # Funkcja:

# Zad.6
# # Iteracyjnie:
# max=0
# l=0
# for i in L:
#   if i > max:
#     max = i
# for j in L:
#   if j == max:
#     l += 1
# print(l)
# # Funkcja:
# print(L.count(max(L)))

# Zad.7
# # Iteracyjnie:
# l = 0
# mn = 100
# for i in L:
#   if i < mn:
#     mn = i
# for j in L:
#   if j == mn:
#     l += 1
# print(l)
# # Funkcja:
# print(L.count(min(L)))

# Zad.8
# # Iteracyjnie:
# n = int(input("Liczba: "))
# l = 0
# for i in L:
#   if i == n:
#     l += 1
# print(l)
# # Funkcja:

# Zad.9
# # Iteracyjnie:
# sum = 0
# for i in L:
#   sum += i
# sum = sum/40
# print(round(sum,1))
# # Funkcja:

# Zad.10
# # Iteracyjnie:
# sum = 0
# for i in range(0, len(L) ,2):
#   sum += L[i]
# print(sum)
# # Funkcja:

# Zad.11
# # Iteracyjnie:
# sum = 0
# for i in range(1,len(L),2):
#   sum += L[i]
# sum = sum // 40
# print(sum)
# # Funkcja:

# Zad.12
# # Iteracyjnie:
# n = 0
# l = 0
# for i in range(len(L)):
#   n = i
#   for j in range(len(L)):
#     if L[j] == n:
#       l += 1
#   if l == 1:
#     print(L[i], end=" ")
# # Funkcja:

# Zad.13
# # Iteracyjnie:
# n = 1
# for i in range(10,100):
#   for j in L:
#     if i == j:
#       n = 0
#   if n == 1:
#     print(i)
# # Funkcja:
