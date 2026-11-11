# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Typ tekstowy (string) służy do przechowywania sekwencji znaków, a funkcja len() pozwala sprawdzić ich liczbę. 
# Uzupełnij program, aby obliczył liczbę znaków w Twoim imieniu, nazwisku oraz pełnym imieniu i nazwisku.

# name = 'Anna' 
# surname = 'Oprun' 

# characters_in_name = len(name)
# characters_in_surname = len(surname)
# full_name = name + ' ' + surname
# characters_in_full_name1 = len(full_name) 
# characters_in_full_name2 = characters_in_name + characters_in_surname

# print(f"Twoje imię ma {characters_in_name} znaków")
# print(f"Twoje nazwisko ma {characters_in_surname} znaków")
# print(f"Twoje pełne imię i nazwisko ma {characters_in_full_name1} znaków - ze spacją")
# print(f"Twoje pełne imię i nazwisko ma {characters_in_full_name2} znaków - bez spacji")

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Znaki w łańcuchu tekstowym są numerowane (indeksowane) począwszy od zera. Oznacza to, że pierwszy znak ma indeks 0, drugi ma indeks 1, trzeci ma indeks 2 itd. 
# Zasada ta jest stosowana w wielu językach programowania.   
# Zmodyfikuj poniższy program, aby wypisywał inicjały Twojego imienia i nazwiska

# name = 'Anna'
# surname = 'Oprun'

# print(name[0])
# print(surname[0])  # Wynik: Wypisuje inicjały

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje skrót nazwy uniwersytetu (tj. KUE).

# uniwersytet = "Krakow University of Economics"
# skrot = uniwersytet[0] + uniwersytet[7] + uniwersytet[21]
# print(skrot)

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# W Pythonie do odczytania zakresu znaków z łańcucha tekstowego można użyć metody wycinków (slicing).   
# Dane pracownika mają postać opisową: "Mr. John May, born on 1998-02-16"   
# Wypisz imię, nazwisko, inicjały oraz datę urodzenia pracownika w osobnych liniach. Uzupełnij kod programu.

# employee = "Mr. John May, born on 1998-02-16"

# print(f"Imię: {employee[4:8]}")
# print(f"Nazwisko: {employee[9:12]}")
# print(f"Data urodzenia: {employee[22:]}") # Wyciągnięcie daty urodzenia od indeksu 22 do końca tekstu
# print(f"Inicjały: {employee[4]}{employee[9]}")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Aby poprawić czytelność, numery telefonów są często prezentowane z myślnikiem lub spacją oddzielającą niektóre cyfry. 
# Napisz program, który wypisuje 9-cyfrowy numer telefonu wprowadzony z klawiatury jako trzy grupy po 3 cyfry każda, rozdzielone znakiem myślnika.

# telefon = input("Podaj numer telefonu: ")
# sformatowany_telefon = telefon[0:3] + "-" + telefon[3:6] + "-" + telefon[6:9]       # Wycięcie poszczególnych części numeru i połącznie ich myślnikami

# print(f"Numer telefonu: {sformatowany_telefon}")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# W informatyce każdy pisany (graficzny) znak języka ludzkiego jest kodowany poprzez przypisanie mu liczby. 
# Do konwersji znaku na jego reprezentację numeryczną służy funkcja ord() w Pythonie. Napisz program wypisujący reprezentację numeryczną dla podanych znaków:
# Program wypisujący reprezentację numeryczną (kody) wybranych znaków za pomocą funkcji ord()

# print(f"a: {ord('a')}")
# print(f"b: {ord('b')}")
# print(f"z: {ord('z')}")
# print(f"A: {ord('A')}")
# print(f"B: {ord('B')}")
# print(f"Z: {ord('Z')}")
# print(f"1: {ord('1')}")
# print(f"=: {ord('=')}")
# print(f"+: {ord('+')}")
# print(f"€: {ord('€')}")

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje reprezentację numeryczną każdej litery Twojego imienia.

# name = 'Anna' 

# print(f"Litera {name[0]} ma kod {ord(name[0])}")
# print(f"Litera {name[1]} ma kod {ord(name[1])}")
# print(f"Litera {name[2]} ma kod {ord(name[2])}")
# print(f"Litera {name[3]} ma kod {ord(name[3])}")

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza, ile liter znajduje się pomiędzy dwiema podanymi literami.
# Następnie, używając programu, oblicz, ile liter znajduje się pomiędzy literami:

# first = input("Podaj pierwszą literę: ")
# last = input("Podaj drugą literę: ")

# first_letter_code = ord(first)
# last_letter_code = ord(last)

# number_of_letters = abs(last_letter_code - first_letter_code) - 1       # Obliczenie liczby liter pomiędzy nimi (różnica kodów minus jeden)

# # --> Kod 'A' to 65, a kod 'D' to 68.Różnica wynosi 68 - 65 = 3.Pomiędzy 'A' a 'D' leżą jednak tylko dwie litery: B i C.

# print(f"Pomiędzy {first} i {last} jest {number_of_letters} liter")

# ZADANIE 9________________________________________________________________________________________________________________________________________________________________________
# Możesz również sprawdzić, jaki znak odpowiada danej wartości kodu, używając dostępnej funkcji chr(). 
# Napisz program, który pozwala sprawdzić, jakie słowo jest ukryte w następujących kodach znaków:

# print(chr(67) + chr(111) + chr(111) + chr(108) + chr(33)) # --> Cool!

# ZADANIE 10________________________________________________________________________________________________________________________________________________________________________
# Każdy język programowania posiada szereg gotowych do użycia funkcji służących do manipulacji ciągami znaków. 
# Uzupełnij program dla filmu "The Lord of the Rings: The Return of the King", wypisując liczbę znaków, tytuł wielkimi i małymi literami, 
# liczbę wystąpień litery "e" oraz pozycję słów "Lord" i "dragon".

# movie = "The Lord of the Rings: The Return of the King"

# print(f"Liczba znaków: {len(movie)}") # Wypisanie liczby znaków w tekście

# print(f"Wielkie litery: {movie.upper()}") # Wypisanie tytułu wielkimi literami

# print(f"Małe litery: {movie.lower()}") # Wypisanie tytułu małymi literami

# print(f"Liczba liter 'e': {movie.count('e')}") # Wypisanie, ile razy litera 'e' pojawia się w tytule

# print(f"Pozycja słowa 'Lord': {movie.find('Lord')}") # Wypisanie pozycji, na której znajduje się słowo 'Lord'

# print(f"Pozycja słowa 'dragon': {movie.find('dragon')}") # Wypisanie pozycji słowa 'dragon' (zwróci -1, jeśli słowo nie występuje w tekście)