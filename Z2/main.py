import random
import string
from sympy import isprime

# ZADANIE 1
# liczba = input()
# if liczba.isdigit() or (liczba.startswith("-") and liczba[1:].isdigit()):
#     liczba = int(liczba)
#     if liczba >= 0:
#         print("Liczba jest dodatnia")
#     else:
#         print("Liczba jest ujemna")

#ZADANIE 2

# def ocen(ocena: int):
#     if ocena > 90:
#         return 5
#     elif ocena > 75:
#         return 4
#     elif ocena > 50:
#         return 3
#     elif ocena < 50:
#         return 2
#
#
# liczba = input()
# if liczba.isdigit() or (liczba.startswith("-") and liczba[1:].isdigit()):
#     ocena = int(liczba)
#     print(ocen(ocena))
# else:
#     print("To nie jest liczba")

#ZADANIE 3

# liczba = input()
# if liczba.isdigit() or (liczba.startswith("-") and liczba[1:].isdigit()):
#     liczba = int(liczba)
#     if liczba % 2 == 0:
#         print("Liczba parzysta")
#     else:
#         print("Liczba nieparzysta")
# else:
#     print("To nie jest liczba")

#ZADANIE 4
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)

#ZADANIE 5
#
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(i*j)

#Zadanie 6
# zgadl = False
#
# while not zgadl :
#     print("Zgadnij liczbę od 1 do 10")
#     liczba = input()
#     if liczba.isdigit() or (liczba.startswith("-") and liczba[1:].isdigit()):
#         liczba = int(liczba)
#         test = random.randint(1,10)
#         if liczba == test:
#             zgadl = True
#             print("Gratulacje")
#         else:
#             print("Porażka")
#     else:
#         print("To nie jest liczba")

#Zadanie 7

# lista = [1,2,3,4,5,6,7,8,9,10]
# listaP = [2,4,6,8,10]
#
# print(all(i % 2 ==0 for i in lista))
# print(all(i% 2 == 0 for i in listaP))

#Zadanie 8

# listaS = ["ala", "nana", "balon"]
# print(all("a" in i for i in listaS))
# print(any("b" in i for i in listaS))

#Zadanie 9
# for i in range(101):
#     if isprime(i):
#         print(i)

# #Zadanie10
# lista = []
# for i in range(10, 101, 5):
#     lista.append(i)
# print(lista)
#
# #Zadanie 11
# for i, y in enumerate(lista):
#     print("Na indeksie " + str(i) + " Mamy wartość: " + str(y))
#
# #Zadanie 12
#
# listaLiter = ['a','b','c','d','e']
# for i in list(zip(lista,listaLiter)):
#     print(i)
#Zadanie 13
# try:
#     7/0
# except ZeroDivisionError:
#     print("Pamietaj cholero nie dziel przez 0")
#Zadanie 14
# try:
#     print("Podaj liczbe")
#     liczba = input()
#     liczba = float(liczba)
# except ValueError:
#     print("Blad niepoprawna liczba")
#Zadanie 15
# try:
#     open("/niestniejacypli/haha")
# except FileNotFoundError:
#     print("Ale taki plik nie istnieje")

