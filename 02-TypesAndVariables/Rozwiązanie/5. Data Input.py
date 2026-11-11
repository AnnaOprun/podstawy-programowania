# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# W każdym języku programowania istnieje funkcja do pobierania danych od użytkownika. Pozwala ona programowi wstrzymać działanie i czekać, aż użytkownik wpisze coś z klawiatury. 
# Wszystko, co wpisze użytkownik, jest traktowane jako tekst (string).
# Zadanie polega na uzupełnieniu kodu, który wczytuje imię i nazwisko, zapisuje je w osobnych zmiennych, łączy w pełne imię i nazwisko oraz wypisuje wyniki.

# imie = input("Podaj swoje imię: ")
# nazwisko = input("Podaj swoje nazwisko: ")
# pelne_imie = imie + " " + nazwisko

# print(f"Twoje imię to {imie}, a Twoje nazwisko to {nazwisko}.")
# print(f"A Twoje pełne imię i nazwisko to {pelne_imie}.")

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Pamiętaj, że wszystko, co użytkownik wpisze z klawiatury, jest traktowane jako tekst (string). Jeśli potrzebujesz liczby do obliczeń arytmetycznych, 
# musisz przekonwertować tekst na liczbę za pomocą funkcji int() dla liczb całkowitych lub float() dla liczb rzeczywistych.   
# Zadanie polega na uzupełnieniu kodu programu, który oblicza objętość i pole powierzchni sześcianu na podstawie podanego boku.

# cube_side_string = input('Podaj bok sześcianu: ')
# cube_side = int(cube_side_string)

# cube_volume = cube_side ** 3     # Obliczenie objętości sześcianu (wzór: a³)
# cube_surface_area = 6 * (cube_side ** 2)     # Obliczenie pola powierzchni sześcianu (wzór: 6 * a²)

# print(f'Objętość sześcianu o boku {cube_side} wynosi {cube_volume}')
# print(f'Pole powierzchni sześcianu o boku {cube_side} wynosi {cube_surface_area}')

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza objętość i pole powierzchni prostopadłościanu o bokach a, b i c. 

# a = float(input("Podaj długość boku a: "))
# b = float(input("Podaj długość boku b: "))
# c = float(input("Podaj długość boku c: "))

# objetosc = a * b * c     # Obliczenie objętości (wzór: a * b * c)
# pole_powierzchni = 2 * (a * b + b * c + a * c)      # Obliczenie pola powierzchni

# print(f"Objętość prostopadłościanu wynosi {objetosc}")
# print(f"Pole powierzchni prostopadłościanu wynosi {pole_powierzchni}")

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Od kwoty zapłacono 23% VAT. Napisano program, który wczytuje kwotę z klawiatury. 
# Następnie oblicza i wypisuje zarówno kwotę, jak i jej podatek VAT. Zastosuj formatowanie do dwóch miejsc po przecinku.

# kwota = float(input("Podaj kwotę: "))

# vat = kwota * 0.23   # Obliczenie podatku VAT (23%)

# print(f"Amount   : {kwota:.2f}") # Zapis (:.2f) w f-stringu służy do formatowania liczb zmiennecinkowych (ułamków) w taki sposób, aby były wyświetlane dokładnie z dwoma miejscami po przecinku.
# print(f"VAT 23%  : {vat:.2f}")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Cena produktu na etykiecie jest podawana przed i po uwzględnieniu rabatu. Napisz program, który umożliwia wprowadzenie ceny produktu i rabatu. 
# Wypisz cenę produktu, rabat, cenę produktu po rabacie oraz różnicę między ceną produktu przed i po rabacie. Wszystkie ceny wydrukuj z dwoma miejscami po przecinku.

# cena = float(input("Podaj cenę: "))
# rabat = float(input("Podaj rabat w %: "))

# redukcja = cena * (rabat / 100)     # Obliczenie kwoty obniżki (redukcji)
# cena_po_rabacie = cena - redukcja

# print(f"Cena: {cena:.2f}")
# print(f"Rabat %: {rabat:.0f}")
# print(f"Cena po rabacie: {cena_po_rabacie:.2f}")
# print(f"Obniżka: {redukcja:.2f}")



