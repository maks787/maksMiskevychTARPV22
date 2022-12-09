from math import * #perepisal import
import math
print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #konvertiroval vo float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2)) 
print()
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #konvertiroval vo float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #konvertiroval vo float
S=b*c
print("Ristküliku pindala, S") #dobavil kovichki
P=2*(b+c) #dobavil umnozheniye 
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b*2+c*2) 
print("Ristküliku diagonaal" , round(di,2)) #dobavil okruglenije 
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #konvertiroval vo float
d=2*r
print(f"Ringi läbimõõt, {d}") 
S=pi*r**2 #ispravil formulu
print("Ringi pindala", round(S,2)) #postavil zna4enie okrugleniya
C=2*pi*r
print("Ringjoone pikkus", round(C,2)) #postavil zna4enie okrugleniya

