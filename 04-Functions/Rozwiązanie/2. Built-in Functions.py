# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Istnieje wiele funkcji wbudowanych, gotowych do użycia, np. len(), print(), input() czy type().   
# Używając wbudowanych funkcji Pythona, napisz program, który oblicza i wypisuje:   

# Największa liczba z podanych
max_number = max(7, 5, 6, 3, 8, 2)
print("Największa liczba z 7,5,6,3,8,2 to:", max_number)

# Najmniejsza liczba z podanych
min_number = min(4, 7, 2, 3, 9, 8)
print("Najmniejsza liczba z 4,7,2,3,9,8 to:", min_number)

# Długość frazy "computer science" (liczba znaków, wliczając spację)
str_length = len("computer science")
print('Liczba znaków w "computer science" wynosi:', str_length)

# Wczytanie litery z klawiatury
letter = input("Wprowadź literę: ")
print("Wczytana litera to:", letter)

# Konwersja tekstu "20303" na liczbę całkowitą
number_from_str = int("20303")
print('Liczba reprezentująca ciąg "20303" to:', number_from_str)

# Reprezentacja binarna liczby 304 (zwraca napis z przedrostkiem '0b')
binary_str = bin(304)
print("Postać binarna liczby 304 to:", binary_str)

# Reprezentacja szesnastkowa liczby 304 (zwraca napis z przedrostkiem '0x')
hex_str = hex(304)
print("Postać szesnastkowa liczby 304 to:", hex_str)

# Kod Unicode dla znaku euro (€)
euro_unicode = ord("€")
print("Kod Unicode znaku € to:", euro_unicode)

# Wartość bezwzględna z -17 (usuwa minus)
abs_value = abs(-17)
print("Wartość bezwzględna z -17 to:", abs_value)