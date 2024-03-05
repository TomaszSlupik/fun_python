# Tablica ASCII 
print(chr(65))

print('---')
# Cytat
cytat = 'Czesc \'Jan Kowalski\' '
print(cytat)

print('---')

# Nowe linie
print("""Dzisiaj 
testujemy 
sobie""")

print('---')

# różnica Python2 => <class 'int'> i Python3 => tutaj bedzie <class 'float'>
a = 10
b = 7
print(type(a / b))

print('---')

# Dodanie i obejście stringa 
print(2 + int('2'))

print('---')

# lub 
c = 6
c = '6'
print(c)

print('---')

# pomnożenie 
print(10 * 'Hej')

print('---')

# jakie mamy obiekty (zdefiniowa nazwy modułów)
print(dir("ala"))

print('---')

# z dużej litery 
napis = 'ala'
print(napis.capitalize())

print('---')
# Otworzenie Chrome uśpienie na 4 sekundy i zamknięcie 
from selenium import webdriver
from time import sleep
webTest = webdriver.Chrome()
webTest.get("https://www.onet.pl")
sleep(4)

print('---')

# typy bool - od nazwiska matematyka 
final = True
if final == True:
    print("Prawda")
else:
    print("Nie")

print('---')

# Input
age = input("Podaj wiek: ")
if int(age) >= 18:
    print("Możesz kupić piwo")
    if int(age) > 30:
        print("Zaprawszamy")
else:
    print("Musisz okazać dowód")

print('---')

# program który przyjmie pola i ceny dwóch pizz
# i określi ktore z nich bardziej się opłaca 
import math

pizza1_srednica = float(input("Podaj srednicę 1 pizzy: "))
pizza1_cena = float(input("Podaj cenę 1 pizzy: "))
wskaznik_1 = float(pizza1_cena / math.pi * (pizza1_srednica/2 ** 2))

pizza2_srednica = float(input ("Podaj srednicę 2 pizzy: "))
pizza2_cena = float(input("Podaj cenę 2 pizzy: "))
wskaznik_2 = float(pizza2_cena / math.pi * (pizza2_srednica/2 ** 2))

print("Wynik:")
if wskaznik_1 < wskaznik_2:
    print('Bardziej opłaca się pizzę 1')
else:
    print("Wybierz 2 pizzę")

print('---')