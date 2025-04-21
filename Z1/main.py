#Z1
# print("Hello PJATK")
#
# #Z2
# wrt = 1
# wra = "Ala"
# wrb = True
# wrc = 2.532
#
# #Z3
# a = "a"
# b=3
# c=5.5
# print(a+b) #Error
# print(b+c)

#Z4
# wrd, wre, wrf = 1.13, 2, "kot"
# print(wre)

#Z5
# name = input()
# print((name + " ") *20)

#Z6
# multilinestr = """ala
# ma
# kota"""
# print(multilinestr)

#Z7
# name = "Mike"
# age = 35
# def przedstaw(x,y):
#     print("My name is " + x + " and I'm " + str(y) + " years old")
#
#
# przedstaw(name, age)

#Z8
# print(f"Ala ma {4} koty")
# print("Czesc jestem {imie} i lubie obliczac pi {pi:.2f}".format(imie="Przemek", pi=3.12511))

#Z9
# print("Podaj wartosc a")
# a = input()
# print("Podaj wartosc b")
# b = input()
# print(f"Suma = {int(a) + int(b)}")

#Z10
# tekst = input()
# print(tekst.upper())
# print(tekst.lower())
# print(tekst.replace("a", "b"))

#Z11
# alat = True
# alaf = False
# if (alaf):
#     print("Ojej")
# elif(alat):
#     print("No wlasnie")

#Z12
# lista = ["ala", 2, True]
# for i in range(len(lista)):
#     print(lista[i])

#Z13
tuple1 = ("ala", 2, True)
# for i in range(len(tuple1)):
#     print(tuple1[i])

#Z14
lista = ["ala", 2, True, "Misia", "Basia", "Ola"]
#A
# for i in range(len(lista)-1):
#     print(lista[i])
#B
# for i in range(len(lista)):
#     if i % 2 == 0:
#         print(lista[i])
#C
# for i in range(int(len(lista) - len(lista)/2)):
#     if i % 2 == 0:
#         print(lista[i])
#D
# wrt = "Misia"
# print(wrt in lista)
#E
# tuple1[1] = "Kot" #Error
# lista[1] = "Kakao"
#F
# lista.append("Kaktus")
# print(lista[len(lista)-1])
# lista.insert(2, "Pies")
# print(lista[2])
#G i H
# del lista[len(lista)-1]
# print(lista[len(lista)-1])
# del lista[3]
# print(lista[3])
#I
lista2 = ["Kasztan", "Jablko", "Cytryna"]

# lista += lista2
# for i in range(len(lista)):
#     print(lista[i])
#
# #J
# print(lista.count("X"))
# print(lista.count("Ola"))

#Z15 i Z16
# lista2d = [[1, 2, 3],
#            [1, 2, 3],
#            [1, 2, 3]]
# del lista2d

#Z17
# slownik = {"klucz1": "Wartosc1", "klucz2": 2, "klucz3": True}
# print(slownik.keys())
# del slownik["klucz1"]
# print(slownik.values())
# slownik["klucz4"] = "Nowa wartosc"
# print(slownik.values())
