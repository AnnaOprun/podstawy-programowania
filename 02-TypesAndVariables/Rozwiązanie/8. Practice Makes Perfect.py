# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Algorytm to procedura krok po kroku lub zestaw reguł zaprojektowanych w celu rozwiązania problemu. 
# Poniższy kod programu wyszczególnia kroki potrzebne do obliczenia pola powierzchni oraz obwodu koła. Uzupełnij program, a następnie sprawdź go dla podanych danych.

# r = float(input("Podaj promień: "))
# pi = 3.14

# area = pi * (r ** 2) # Obliczenie pola powierzchni
# circumference = 2 * pi * r # Obliczenie obwodu

# print(f"Obwód: {circumference}")
# print(f"Pole powierzchni: {area}")

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Napisz program (konwerter temperatur), który odczytuje temperaturę w stopniach Celsjusza z klawiatury. 
# Następnie program oblicza i wypisuje temperaturę w kelwinach i stopniach Fahrenheita.

# celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
# kelvin = celsius + 273.15
# fahrenheit = celsius * 9 / 5 + 32

# print(f"Temperatura w Kelwinach: {kelvin}")
# print(f"Temperatura w Fahrenhaitach: {fahrenheit}")

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Napisz program – konwerter jednostek – który wypisuje Twój wzrost zarówno w centymetrach, jak i w stopach oraz calach. 
# Użyj operatora dzielenia bez reszty oraz operatora obliczającego resztę z dzielenia.

# cm = 170

# feet = int(cm // 30.48)     # 1 stopa = 30.48 cm, 1 cal = 2.54 cm --> Obliczamy liczbę stóp za pomocą dzielenia bez reszty (//)
# remaining_cm = cm % 30.48   # Obliczamy pozostałe centymetry za pomocą operatora reszty z dzielenia (%)
# inches = int(remaining_cm / 2.54)   # Przeliczamy resztę centymetrów na cale i zaokrąglamy do liczby całkowitej

# print(f"Mam {cm} cm wzrostu, tj. {feet} stóp i {inches} cali")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Kod SWIFT (znany również jako BIC – Bank Identifier Code) to unikalny kod identyfikacyjny używany do globalnej identyfikacji konkretnego banku lub instytucji finansowej. 
# Jest on używany przede wszystkim do międzynarodowych przelewów i komunikacji między bankami. 
# Kod SWIFT ma zazwyczaj 8 lub 11 znaków i składa się z kodu banku (4 znaki), kodu kraju (2 znaki), kodu lokalizacji (2 znaki) oraz opcjonalnego kodu oddziału (3 znaki). 
# Napisz program, który odczytuje kod SWIFT z klawiatury i wypisuje kod banku oraz kod kraju.

# swift = input("Podaj kod SWIFT: ")

# bank_code = swift[0:4]   # Kod banku to pierwsze 4 znaki (indekse od 0 do 3)
# country_code = swift[4:6]   # Kod kraju to kolejne 2 znaki (indeksy od 4 do 5)

# print(f"Bank Code: {bank_code}")
# print(f"Country Code: {country_code}")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Firma transportowa potrzebuje programu do obliczania kosztu transportu towarów. 
# Program oblicza koszt transportu na podstawie podanej odległości w km, ceny paliwa za 1 litr oraz zużycia paliwa w litrach na 100 km.

# distance = int(input("Podaj odległość w km: "))
# fuel_price = float(input("Podaj cenę paliwa za litr: "))
# fuel_consumption = float(input("Podaj zużycie paliwa w litrach na 100 km: "))

# total_fuel_consumption = (distance / 100) * fuel_consumption # Obliczenie całkowitego zużycia paliwa (zużycie na 100 km razy przebyty dystans podzielony przez 100)

# total_cost = total_fuel_consumption * fuel_price # Obliczenie całkowitego kosztu (całkowite zużycie paliwa razy cena za litr)

# print(f"Całkowite zużycie paliwa: {total_fuel_consumption} litrów")
# print(f"Całkowity koszt transportu: {total_cost} zł")

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# System binarny (dwójkowy) to pozycyjny system liczbowy wymagający tylko dwóch cyfr: 0 i 1, 
# natomiast system szesnastkowy (heksadecymalny) używa szesnastu symboli (od 0 do 9 oraz od A do F). 
# Napisz program, który odczytuje liczbę całkowitą z klawiatury i wypisuje ją w systemie binarnym oraz szesnastkowym, korzystając z wbudowanych funkcji Pythona.

# number = int(input("Enter number: "))

# binary_number = bin(number)
# hex_number = hex(number)

# print(f"Binary number: {binary_number}")
# print(f"Hexadecimal number: {hex_number}")


