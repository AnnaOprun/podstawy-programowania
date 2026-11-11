# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Osoby do 26 roku życia włącznie są zwolnione z płacenia podatków w Polsce. 
# Napisz program, który na podstawie wieku osoby wprowadzonego z klawiatury wypisuje True, jeśli osoba jest zwolniona z podatku, a w przeciwnym razie wypisuje False.

# wiek = int(input("Podaj wiek: "))
# brak_podatku = wiek <= 26

# print(f"Zwolnienie z płacenia podatków: {brak_podatku}")

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Hasło jest poprawne, jeśli ma co najmniej 8 znaków długości. Napisz program, który sprawdza, czy długość hasła odczytanego z klawiatury jest poprawna.

# haslo = input("Podaj hasło: ")
# haslo_ok = len(haslo) >= 8

# print(f"Długość hasła jest poprawna: {haslo_ok}")

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który sprawdza, czy liczba wprowadzona z klawiatury jest parzysta. Wypisz True, gdy liczba jest parzysta, oraz False, gdy liczba jest nieparzysta. 

# number = int(input("Podaj liczbę: "))
# even = number % 2 == 0

# print(f"Liczba jest parzysta: {even}")

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Drzewo może zostać ścięte, jeśli jego średnica wynosi co najmniej 50 cm.
# Napisz program, który na podstawie obwodu drzewa wprowadzonego z klawiatury oblicza i wypisuje wartość True, jeśli drzewo może zostać ścięte, lub False w przeciwnym razie.

# import math

# obwod = float(input("Podaj obwód drzewa w cm: "))
# srednica = obwod / math.pi
# mozna_sciac = srednica >= 50

# print(f"Drzewo może być ścięte: {mozna_sciac}")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Numery rejestracyjne pojazdów w Krakowie zaczynają się od liter KR lub KK. 
# Napisz program, który sprawdza, czy numer rejestracyjny pojazdu wprowadzony z klawiatury oznacza pojazd z Krakowa. 
# Wypisz True, jeśli samochód jest z Krakowa, lub False w przeciwnym razie.

# car_number = input("Podaj numer rejestracyjny pojazdu: ")
# is_krakow = car_number[0:2] == "KR" or car_number[0:2] == "KK"

# print(f"Samochód jest z Krakowa: {is_krakow}")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Prędkość pojazdów na autostradzie w Polsce musi mieścić się w zakresie od 40 do 140 km/h. 
# Napisz program, który sprawdza, czy prędkość pojazdu wprowadzona z klawiatury jest poprawna.

# predkosc = int(input("Podaj prędkość pojazdu: "))
# poprawna_predkosc = 40 <= predkosc <= 140

# print(f"Prędkość jest poprawna: {poprawna_predkosc}")

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Każdy język programowania udostępnia zestaw funkcji, których możesz używać w swoich programach. Jedną z nich jest funkcja randint(a,b), 
# która zwraca losową liczbę całkowitą z zakresu [a,b]. Funkcja ta jest dostępna w module o nazwie random, który należy zaimportować do programu. 

# import random

# random_number = random.randint(5, 10) # Program generujący losową liczbę CAŁKOWITĄ z zakresu od 5 do 10 (włącznie)
# print(random_number)

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje wyniki trzech rzutów kością oraz sumę wyrzuconych oczek, stosując generator liczb losowych.
# Program symulujący trzy rzuty kostką do gry i sumujący wyrzucone oczka

# import random

# dice_roll_1 = random.randint(1, 6)
# dice_roll_2 = random.randint(1, 6)
# dice_roll_3 = random.randint(1, 6)

# total = dice_roll_1 + dice_roll_2 + dice_roll_3

# print(f"Wyniki rzutów: {dice_roll_1}, {dice_roll_2}, {dice_roll_3}")
# print(f"Suma oczek: {total}")

# ZADANIE 9________________________________________________________________________________________________________________________________________________________________________
# W wielu grach liczby jeden i sześć na kości mają specjalne znaczenie. 
# Napisz program, który wypisuje liczbę wyrzuconą na kości oraz wartość True, jeśli wyrzucona liczba to 1 lub 6.

# import random

# dice_rolled = random.randint(1, 6)
# special_number = dice_rolled == 1 or dice_rolled == 6

# print(f"Liczba wyrzuconą na kości: {dice_rolled}")
# print(f"specjalne numer (1 or 6): {special_number}")

# ZADANIE 10_______________________________________________________________________________________________________________________________________________________________________
# Napisz program, który umożliwia użytkownikowi rzucenie wyzwania komputerowi. Komputer rzuca kością. 
# Następnie użytkownik próbuje odgadnąć liczbę z kości, wpisując z klawiatury liczbę od 1 do 6. 
# Jeśli użytkownik odgadł liczbę z kości, komputer wypisuje True, w przeciwnym razie komputer wypisuje False.

# import random
# computer = random.randint(1, 6)

# you = int(input("Zgadnij liczbę (1-6): "))
# won = you == computer

# print(f"You won: {won}")


