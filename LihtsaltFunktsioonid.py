from math import * # звезда показывает что используются все функции


# 08/12/2022

#print("Hello world!") # Выводит информацию на экран.
#name=input("What is your name? ") # Функция выдает информацию в формате "str".
#print() # Пустая строка
#print(f"{name}, i like your name! ")
#print(name,", i like your name! ") # ,->пробел
#print(name+", i like your name! ") # str+str
#age=int(input("How old are you? ")) # int(str)
#print(name,"you are", age, "years old")
#age+=10
#print(name+", 10 aasta parast sa oled"+str(age)+"years old")

from base64 import b16decode, b16encode


print()
print("Vordse pindalaga riskulik ja ring")
a=float(input("Anna laius: "))
b=float(input("Anna korgus: "))
S=a*b # -,*,/,**,+,//,%
P=2*a+2*b
d=round(sqrt(a**2+b**2),2)
print(f"Pindala = {S}\nPerimetr = {P}\nDiagonaal = {d}")
r=round(sqrt(S/pi),2)
print(f"Ringi raadius = {r} ")
