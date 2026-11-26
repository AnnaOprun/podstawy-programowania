# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________

# Plik to nazwane miejsce na dysku służące do trwałego przechowywania danych. Wykorzystuje się go do zapisywania informacji w formacie, który może zostać odczytany przez Pythona, 
# inne programy, a nawet człowieka. Python udostępnia wbudowane funkcje i biblioteki do pracy z plikami, pozwalając tworzyć je, odczytywać, zapisywać oraz modyfikować.
# Zauważ, że pliki mogą występować w różnych postaciach, ale najpopularniejsze z nich to:   
# Pliki tekstowe (np. .txt, .csv, .py): przechowują zwykłe dane tekstowe czytelne dla człowieka.
# Pliki binarne (np. obrazy, filmy, pliki wykonywalne): zawierają dane w formacie binarnym, który nie jest bezpośrednio czytelny dla człowieka.

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
#   ...

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Zwróć uwagę na poniższy program, który otwiera i odczytuje zawartość pliku tekstowego. 
# Zaleca się otwieranie pliku w instrukcji with. Otwarty plik jest wtedy zamykany automatycznie po wykonaniu wszystkich instrukcji znajdujących się w bloku instrukcji with.
# Parametr 'r' (odczyt) w funkcji open() oznacza otwarcie pliku wyłącznie do odczytu. Jest to ustawienie domyślne.

# with open('example.txt', 'r') as file:
#     content = file.read() #pobiera całą zawartość pliku do zmiennej
# # Plik jest automatycznie zamykany po wyjściu z bloku 

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Aby odczytać zawartość pliku, musisz go najpierw otworzyć. Zawartość pliku tekstowego możesz czytać linia po linii albo odczytać całą zawartość pliku od razu.
# Program print_countries.py otwiera plik tekstowy, odczytuje jego zawartość linia po linii i wypisuje zawartość każdej linii. 
# Przeanalizuj kod programu, a następnie uruchom program.   Jeśli program nie może otworzyć pliku countries.txt, sprawdź w terminalu VS Code, jaki jest bieżący folder. 
# Jeśli jest to ClassMaterials, zmień bieżący folder na ten, który zawiera zarówno program, jak i plik countries.txt (08-FileHandling), wykonując poniższe polecenie. 
# Następnie uruchom program ponownie

# with open('countries.txt', 'r') as file:
#     for line in file:
#         print(line, end="")

# Plik 'countries.txt' 

# Poland, Warsaw, 38265000
# Germany, Berlin, 83240000
# France, Paris, 67850000
# Japan, Tokyo, 125800000
# Canada, Ottawa, 38250000

# Zwróć uwagę na użycie instrukcji `print()` z parametrem `end=""`. Jego zastosowanie wynika z obecności znaków końca linii na końcu wierszy w pliku tekstowym.

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Zmodyfikuj program print_countries.py tak, aby wypisywana lista krajów była ponumerowana.

# with open('countries.txt', 'r') as file:
#     counter=1
#     for line in file:
#         print(f"{counter}. {line}", end="")
#         counter+=1

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Poniższy program wypisuje listę krajów z pliku countries.txt. Zmodyfikuj program tak, aby wypisywał listę krajów posortowaną alfabetycznie.
# Wskazówka: przed wypisaniem zawartości tablicy posortuj ją alfabetycznie za pomocą wbudowanej funkcji sorted().

# def read_from_file(name):
#     with open(name, "r", encoding="utf-8") as file:  # otwieramy plik w trybie odczytu z kodowaniem UTF-8
#         content = file.read()  # pobieramy całą treść pliku jako jeden napis
#     return content  # zwracamy wczytaną treść

# file_content = read_from_file("countries.txt")  # Odczytujemy całą zawartość pliku countries.txt

# file_lines = file_content.splitlines()  # Dzielimy wczytany tekst na osobne linie bez znaków końca linii

# sorted_lines = sorted(file_lines)   # Sortujemy alfabetycznie listę wierszy za pomocą wbudowanej funkcji sorted()

# print("Posortowana alfabetycznie lista krajów:")
# for line in sorted_lines: 
#     print(line)

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Plik car_park.txt zawiera dane o liczbie zaparkowanych samochodów z ostatnich pięciu dni. Uzupełnij poniższy program tak, aby obliczał łączną liczbę zaparkowanych samochodów.

# def read_from_file(name):
#     with open(name, "r", encoding="utf-8") as file:  # otwieramy plik z kodowaniem UTF-8 do odczytu
#         content = file.read()  # pobieramy całą treść pliku jako pojedynczy napis
#     return content  # zwracamy odczytaną zawartość

# # Odczytujemy cały plik i dzielimy go na listę pojedynczych linii
# file_content = read_from_file("car_park.txt")
# file_lines = file_content.splitlines()

# # Sumujemy liczby zaparkowanych samochodów z każdego wiersza pliku
# total = 0  # akumulator przechowujący łączną liczbę samochodów
# for line in file_lines:  # przechodzimy przez każdy wiersz w liście file_lines
#     total += int(line)  # konwertujemy tekst z linii na liczbę całkowitą i dodajemy do sumy

# print("Łączna liczba zaparkowanych samochodów:", total)

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Plik pets.txt zawiera zabawny tekst o zwierzętach. Napisz program, który wypisuje ten tekst oraz zlicza liczbę słów w tekście.
# Aby obliczyć liczbę słów w wierszu, użyj metody split(), która dzieli napis na listę, gdzie każde słowo jest elementem listy. 
# Następnie odczytaj długość tej listy. Użyj funkcji len(). Na koniec zsumuj liczbę słów w każdym wierszu.

# word_count = 0  # licznik wszystkich słów odnalezionych w pliku

# with open("pets.txt", "r", encoding="utf-8") as file:  # otwieramy plik z kodowaniem UTF-8 do odczytu
#     print("Zawartość pliku pets.txt:")
#     for line in file:  # przechodzimy przez kolejne wiersze pliku
#         print(line, end="")  # wypisujemy wiersz bez dodatkowej pustej linii
#         words = line.split()  # dzielimy bieżący wiersz na listę pojedynczych słów
#         word_count += len(words)  # dodajemy liczbę słów z bieżącego wiersza do łącznego licznika

# print(f"\nLiczba słów w tekście: {word_count}")

# ZADANIE 9________________________________________________________________________________________________________________________________________________________________________
# Plik it_company.csv zawiera listę pracowników. Napisz program, który wyświetla wyłącznie pracowników na stanowisku Software Engineer. Ponumeruj pozycje na wypisywanej liście.
# Wskazówka: możesz sprawdzić, czy dany napis zawiera się wewnątrz innego napisu, używając operatora in.

# file_name = "it_company.csv"  # nazwa pliku CSV z listą pracowników
# job_title = "Software Engineer"  # poszukiwane stanowisko pracy

# with open(file_name, "r", encoding="utf-8") as file:  # otwieramy plik z kodowaniem UTF-8 do odczytu
#     print("Pracownicy na stanowisku Software Engineer:")
#     counter = 1
#     for line in file:  # czytamy plik linia po linii
#         if job_title in line:  # sprawdzamy, czy w bieżącym wierszu występuje poszukiwane stanowisko
#             print(f"{counter}. {line}", end="")  # wypisujemy numer i wiersz bez dodatkowej pustej linii
#             counter += 1  # zwiększamy licznik o 1 dla kolejnego pasującego pracownika