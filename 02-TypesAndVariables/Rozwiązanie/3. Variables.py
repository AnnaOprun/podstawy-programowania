# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# W programowaniu zmienna to symboliczna nazwa lub identyfikator, który przechowuje wartość. 
# Działa jak pojemnik na dane, a jej wartość może się zmieniać w trakcie wykonywania programu.

# 1) company
#    - Wartość: "ABC Data"
#    - Typ: str (tekst)

# 2) phone
#    - Wartość: "555-123-009"
#    - Typ: str (tekst)

# 3) employees
#    - Wartość: 25
#    - Typ: int (liczba całkowita)

# 4) remote_work
#    - Wartość: True
#    - Typ: bool (wartość logiczna)

# 5) big_company
#    - Wartość: False (wynik porównania 25 > 100)
#    - Typ: bool (wartość logiczna)

# 6) income
#    - Wartość: 4500000
#    - Typ: int (liczba całkowita)

# 7) income_per_person
#    - Wartość: 180000.0 (wynik dzielenia 4500000 / 25)
#    - Typ: float (liczba zmiennoprzecinkowa)

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Poniżej znajduje się program, który oblicza sumę dwóch liczb. 
# Zadanie polega na zmodyfikowaniu tego programu tak, aby obliczał sumę trzech liczb.

# number1 = 71
# number2 = 14
# number3 = 17

# wynik = number1 + number2 + number3

# print('Liczba 1: ', number1)
# print('Liczba 2: ', number2)
# print('Liczba 3: ', number3)
# print('Suma: ', wynik)

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Dwie zmienne x i y mają wartości odpowiednio 7 i 34. 
# Napisz program, który zamienia wartości tych zmiennych miejscami (po zamianie x powinno wynosić 34, a y powinno wynosić 7). 
# Użyj do tego dodatkowej, pomocniczej zmiennej.

# x = 7
# y = 34
# i = 0  # dodatkowa zmienna pomocnicza

# print("Przed zamianą: x =", x, "| y =", y)

# # zamiana wartości za pomocą zmiennej pomocniczej
# i = x
# x = y
# y = i

# print("Po zamianie: x =", x, "| y =", y)

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który dla podanej prędkości w km/h wypisuje tę prędkość w m/s.

# speed_kmh = 70
# # Aby zamienić km/h na m/s, należy podzielić prędkość przez 3.6
# speed_ms = speed_kmh / 3.6

# print(speed_kmh, "km/h = ", speed_ms, "m/s")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza długość przekątnej prostokąta o bokach a=5 i b=8. 
# Do obliczenia pierwiastka kwadratowego użyj funkcji sqrt, która jest dostępna w module o nazwie math 
# — musisz go zaimportować do swojego programu.

# import math
# a = 5
# b = 8
# przekatna = math.sqrt(a**2 + b**2)

# print("Długość przekątnej prostokąta wynosi:", przekatna)

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Odległość do horyzontu zależy od wysokości obserwatora nad ziemią. Im wyżej się znajdujesz, tym dalej znajduje się horyzont.
# W większości sytuacji można skorzystać ze wzoru: [d = 3.57 × √h], gdzie d - to odległość do horyzontu w kilometrach | h - to wysokość obserwatora w metrach.
# Napisz program, który oblicza odległość do horyzontu na podstawie wysokości podanej w metrach z klawiatury. 
# Następnie za pomocą programu oblicz odległość do horyzontu w km, gdy: 

# import math
# h = float(input("Podaj wysokość w metrach: ")) 
# d = 3.57 * math.sqrt(h) # Obliczenie odległości do horyzontu ze wzoru

# print("Odległość do horyzontu wynosi:", round(d, 2), "km")

# 1) Stojąc na plaży (np. wysokość oczu ok. 1.7 metra):
# h = 1.7
# d_beach = 3.57 * math.sqrt(1.7) --> 4.65 km

# 2) Okno hotelu na wysokości 20 metrów:
# h = 20
# d_hotel = 3.57 * math.sqrt(20) --> 15.97 km

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# W 2022 roku populacja świata wynosiła około 8 miliardów, a na półkuli północnej żyło 7,2 miliarda ludzi. Napisz program, który oblicza i wypisuje:
# 1) Liczbę osób oraz procent populacji ogółem żyjących na półkuli północnej
# 2) Liczbę osób oraz procent populacji ogółem żyjących na półkuli południowej

# total = 8000000000
# polnoc = 7200000000
# poludnie = total - polnoc

# print("Populacja świata: ", total)
# print("Półkula północna: ", polnoc)
# print("Półkula północna w %: ", polnoc / total * 100)
# print("Półkula południowa: ", poludnie)
# print("Półkula południowa w %: ", poludnie / total * 100)

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Poniższy program oblicza i wypisuje średnią ocenę ucznia, ale zawiera kilka błędów. Popraw program, aby działał poprawnie.

# math = 5
# art = 4
# music = 5
# history = 3     # Usunięto cudzysłów, aby ocena była liczbą całkowitą (int)

# average = (math + art + music + history) / 4    # Poprawiono nazwy zmiennych, znaki dodawania oraz dodano nawias obejmujący całą sumę ocen

# print("Średnia ocena wynosi:", average)     # Poprawiono cudzysłowy oraz literówkę w nazwie zmiennej 'average'