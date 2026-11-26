# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
#   ...

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Zwróć uwagę, że niektóre operacje na plikach mogą spowodować zatrzymanie działania programu (np. gdy na dysku nie ma pliku o podanej nazwie). 
# Aby temu zapobiec, możesz użyć bloku try-except do obsługi wyjątków, czyli błędów, które mogą wystąpić podczas wykonywania programu. 
# Wyjątki mogą pojawić się na przykład przy próbie dzielenia przez zero, odwołaniu się do nieistniejącego pliku lub przetwarzaniu danych w złym formacie.
# dea stojąca za try-except polega na tym, że umieszczasz kod, który może wywołać błąd, wewnątrz bloku try, a jeśli wystąpi błąd, blok except obsługuje go bez awaryjnego 
# przerywania działania programu.  

# try:
#    # kod, który może zgłosić wyjątek
# except TypWyjątku:
#    # kod obsługujący wyjątek

# Program read_file.py próbuje wypisać zawartość pliku, którego nie ma na dysku. 
# Przeczytaj treść programu, a następnie uruchom go i zobacz, co się stanie. Jak widać, program zatrzymuje się, gdy napotka błąd (próbę otwarcia nieistniejącego pliku).   
# Następnie zapoznaj się z treścią programu read_file_try_except.py, który otwiera i odczytuje zawartość pliku wewnątrz bloku try-except. Na koniec uruchom program. 
# Jak widać, nawet gdy wystąpi błąd (próba otwarcia nieistniejącego pliku), program działa dalej.   

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wyświetla pierwsze pięć wierszy z pliku it_company.csv, a następnie w kolejnym wierszu wypisuje komunikat o naciśnięciu klawisza Enter 
# i czeka na naciśnięcie klawisza Enter. Program powtarza wyświetlanie kolejnych pięciu wierszy z pliku, za każdym razem czekając na naciśnięcie klawisza Enter.

# file_name = "it_company.csv"  # nazwa pliku CSV z danymi pracowników

# # Otwieramy plik w trybie odczytu ('r') z kodowaniem UTF-8 i wypisujemy go porcjami po 5 linii
# with open(file_name, "r", encoding="utf-8") as file:
#     count = 0  # licznik wierszy wypisanych w bieżącej paczce
#     for line in file:  # czytamy plik linia po linii
#         print(line, end="")  # wypisujemy wiersz bez dodatkowej pustej linii
#         count += 1  # zwiększamy licznik wierszy w aktualnej grupie
#         if count == 5:  # po wyświetleniu pięciu wierszy robimy przerwę
#             print("Naciśnij klawisz Enter...")  # wypisujemy zachętę w kolejnym wierszu
#             input()  # czekamy, aż użytkownik naciśnie klawisz Enter
#             count = 0  # zerujemy licznik przed kolejną paczką pięciu wierszy

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Plik email.txt zawiera surową wiadomość e-mail.
# Napisz program, który używa wyrażeń regularnych do pobrania i wypisania:
# adresu e-mail 
# nadawcyadresu e-mail 
# odbiorcytematu wiadomości e-mail
# treści wiadomości e-mail
# Dla każdego z powyższych poleceń zdefiniuj osobną funkcję, która zwraca wartość odczytaną z wiadomości e-mail. 

# Plik 'emails.py'

# import emails  # importujemy utworzony moduł emails

# sender = emails.email_sender()  # pobieramy adres e-mail nadawcy
# recipient = emails.email_recipient()  # pobieramy adres e-mail odbiorcy
# subject = emails.email_subject()  # pobieramy temat wiadomości
# body = emails.email_body()  # pobieramy treść wiadomości

# print(f"Nadawca: {sender}")
# print(f"Odbiorca: {recipient}")
# print(f"Temat: {subject}")
# print("Treść wiadomości:")
# print(body)

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza liczbę wierszy, znaków oraz słów dla dowolnego pliku tekstowego. 
# Użytkownik podaje nazwę pliku z klawiatury. Użyj bloku try-except, aby uniknąć przerwania działania programu, gdy użytkownik wpisze nazwę pliku, który nie istnieje. 
# Wypisz wynik obliczeń. Aby sprawdzić, czy program działa poprawnie, znajdź w internecie 3 pliki tekstowe i użyj ich do przetestowania programu.
# Program obliczający liczbę wierszy, znaków oraz słów we wskazanym pliku tekstowym

# file_name = input("Podaj nazwę pliku tekstowego: ")  # pobieramy nazwę pliku od użytkownika z klawiatury

# try:
#     with open(file_name, "r", encoding="utf-8") as file:  # otwieramy plik w trybie odczytu z kodowaniem UTF-8
#         content = file.read()  # wczytujemy całą treść pliku jako pojedynczy napis

#     lines = content.splitlines()  # dzielimy treść pliku na listę pojedynczych wierszy
#     line_count = len(lines)  # liczba wierszy w pliku
#     char_count = len(content)  # łączna liczba znaków w odczytanej zawartości pliku
#     word_count = len(content.split())  # łączna liczba słów oddzielonych białymi znakami

#     print(f"Nazwa pliku: {file_name}")
#     print(f"Liczba wierszy: {line_count}")
#     print(f"Liczba znaków: {char_count}")
#     print(f"Liczba słów: {word_count}")
# except FileNotFoundError:  # obsługujemy sytuację, gdy podany plik nie istnieje na dysku
#     print(f"Błąd: plik '{file_name}' nie istnieje.")

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza liczbę samogłosek w tekście wprowadzonym z klawiatury. Użyj wyrażeń regularnych.

# import re  # moduł do obsługi wyrażeń regularnych

# text = input("Wpisz dowolny tekst: ")  # pobieramy tekst od użytkownika z klawiatury

# pattern = r"[aeiouyAEIOUĄĘÓąęó]"  # wzorzec dopasowujący samogłoski (łacińskie i polskie, małe oraz wielkie)
# vowels = re.findall(pattern, text)  # zwraca listę wszystkich samogłosek odnalezionych w tekście

# print(f"Liczba samogłosek w podanym tekście: {len(vowels)}")

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Plik files.txt zawiera listę nazw plików. Napisz program, który wypisuje wyłącznie te nazwy plików, których rozszerzenia składają się z dokładnie czterech znaków (np. .html).

# import re  # moduł wyrażeń regularnych

# file_name = "files.txt"  # nazwa pliku wejściowego z listą nazw plików

# pattern = r"\.[^.\s]{4}$"   # Wzorzec sprawdza, czy na końcu nazwy pliku znajduje się kropka oraz dokładnie cztery znaki rozszerzenia

# with open(file_name, "r", encoding="utf-8") as file:  # otwieramy plik w trybie odczytu z kodowaniem UTF-8
#     print("Pliki z rozszerzeniem składającym się z dokładnie czterech znaków:")
#     for line in file:  # przeglądamy kolejne wiersze pliku
#         entry = line.strip()  # usuwamy białe znaki z początku i końca wiersza, w tym znak nowej linii
#         if re.search(pattern, entry):  # sprawdzamy, czy nazwa pliku pasuje do wzorca rozszerzenia
#             print(entry)  # wypisujemy pasującą nazwę pliku

# ZADANIE 9________________________________________________________________________________________________________________________________________________________________________
# Wygodne przetwarzanie dokumentów CSV jest możliwe dzięki modułowi csv. Znajdź w internecie, jak używać tego modułu. 
# Następnie napisz program, który na podstawie pliku it_company.csv wypisuje imię, nazwisko oraz adres e-mail (w podanej kolejności, bez stanowiska) 
# osób zatrudnionych na stanowisku Graphic Designer.

# import csv  # wbudowany moduł do wygodnego odczytu i przetwarzania plików CSV

# file_name = "it_company.csv"  # nazwa pliku CSV z listą pracowników
# target_position = "Graphic Designer"  # poszukiwane stanowisko pracy

# # Otwieramy plik w trybie odczytu ('r') z kodowaniem UTF-8 oraz parametrem newline="" zalecanym przez moduł csv
# with open(file_name, "r", encoding="utf-8", newline="") as file:
#     reader = csv.DictReader(file)  # czytamy wiersze jako słowniki na podstawie nagłówka pierwszej linii pliku
#     print("GRAPHIC DESIGNERS")
#     print("=================")
#     for row in reader:  # przechodzimy przez kolejne rekordy pracowników
#         if row.get("Job Title") == target_position:  # sprawdzamy, czy stanowisko pracownika to Graphic Designer
#             first_name = row.get("First Name", "")  # pobieramy imię pracownika
#             last_name = row.get("Last Name", "")  # pobieramy nazwisko pracownika
#             email = row.get("Email", "")  # pobieramy adres e-mail pracownika
#             print(f"{first_name} {last_name}, {email}")  # wypisujemy imię, nazwisko oraz e-mail w żądanym formacie

# ZADANIE 10________________________________________________________________________________________________________________________________________________________________________
# Plik clothing.csv zawiera listę odzieży na stanie magazynowym. Napisz program, który wypisuje te produkty, 
# których cena jest mniejsza niż 60 oraz których stan magazynowy jest mniejszy niż 40.

# import csv  # moduł do wygodnego wczytywania plików CSV

# file_name = "clothing.csv"  # nazwa pliku CSV z listą odzieży

# # Otwieramy plik w trybie odczytu ('r') z kodowaniem UTF-8 oraz parametrem newline=""
# with open(file_name, "r", encoding="utf-8", newline="") as file:
#     reader = csv.DictReader(file)  # wczytujemy wiersze jako słowniki na podstawie nagłówków kolumn
#     print("Produkty z ceną poniżej 60 oraz stanem magazynowym poniżej 40:")
#     for row in reader:  # przeglądamy kolejne rekordy produktów
#         # Dopasowujemy nazwy kolumn (np. Price/price oraz Stock/stock) i bezpiecznie konwertujemy na liczby
#         raw_price = row.get("Price") if row.get("Price") is not None else row.get("price", "0")
#         raw_stock = row.get("Stock") if row.get("Stock") is not None else row.get("stock", "0")
#         price = float(raw_price.replace(",", ".").strip())  # zamieniamy cenę na liczbę zmiennoprzecinkową
#         stock = int(float(raw_stock.strip()))  # zamieniamy stan magazynowy na liczbę całkowitą
#         if price < 60 and stock < 40:  # sprawdzamy oba warunki jednocześnie
#             print(row)  # wypisujemy pasujący produkt

# ZADANIE 11________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza, wypisuje oraz zapisuje do pliku tekstowego liczby całkowite od 1 do 100 oraz ich drugą i trzecią potęgę.

# file_name = "powers.txt"  # nazwa pliku tekstowego, do którego zapiszemy wyniki

# # Otwieramy plik w trybie zapisu ('w') z kodowaniem UTF-8 i jednocześnie wypisujemy wiersze na ekranie
# with open(file_name, "w", encoding="utf-8") as file:
#     for number in range(1, 101):  # iterujemy po liczbach całkowitych od 1 do 100 włącznie
#         second_power = number ** 2  # obliczamy drugą potęgę liczby
#         third_power = number ** 3  # obliczamy trzecią potęgę liczby
#         row = f"{number},{second_power},{third_power}"  # formatujemy wiersz dokładnie jak w przykładzie
#         print(row)  # wypisujemy wiersz w terminalu
#         file.write(f"{row}\n")  # zapisujemy wiersz wraz ze znakiem nowej linii do pliku

# print(f"Wyniki zostały zapisane do pliku {file_name}.")

# ZADANIE 12________________________________________________________________________________________________________________________________________________________________________
# Plik books.csv zawiera listę książek. Napisz program, który kopiuje dane książek z podanego gatunku do odpowiadającego mu pliku. 
# Użyj funkcji, aby podzielić program na logiczne części.

# import csv  # moduł do wygodnego wczytywania plików CSV

# SOURCE_FILE = "books.csv"  # nazwa pliku wejściowego z listą książek

# # Mapowanie gatunków literackich na odpowiednie nazwy plików docelowych
# GENRE_FILES = {
#     "Fantasy": "books_fantasy.txt",
#     "Historical": "books_historical.txt",
#     "Romance": "books_romance.txt",
#     "Classic": "books_classic.txt",
# }

# # Funkcja przygotowująca puste pliki docelowe z kodowaniem UTF-8 przed rozpoczęciem kopiowania
# def initialize_genre_files(genre_files):
#     for filename in genre_files.values():  # przechodzimy przez wszystkie nazwy plików gatunków
#         with open(filename, "w", encoding="utf-8"):  # tworzymy lub czyścimy plik docelowy na starcie
#             pass  # samo otwarcie w trybie 'w' wystarcza do przygotowania pliku

# # Funkcja dopisująca pojedynczy rekord książki do wskazanego pliku tekstowego
# def append_book_to_file(filename, book_row):
#     formatted_line = ", ".join(str(value).strip() for value in book_row.values() if value is not None)  # łączymy pola rekordu w czytelny wiersz
#     with open(filename, "a", encoding="utf-8") as target_file:  # otwieramy plik docelowy do dopisywania w UTF-8
#         target_file.write(f"{formatted_line}\n")  # zapisujemy wiersz zakończony znakiem nowej linii

# # Funkcja odczytująca plik books.csv i kierująca książki do plików według ich gatunku
# def distribute_books_by_genre(source_file, genre_files):
#     initialize_genre_files(genre_files)  # przygotowujemy czyste pliki wyjściowe dla każdego gatunku
#     with open(source_file, "r", encoding="utf-8", newline="") as csv_file:  # otwieramy plik CSV w kodowaniu UTF-8
#         reader = csv.DictReader(csv_file)  # czytamy rekordy jako słowniki na podstawie nagłówka kolumn
#         for row in reader:  # sprawdzamy kolejne książki w pliku wejściowym
#             genre = (row.get("Genre") or row.get("genre") or "").strip()  # pobieramy i oczyszczamy nazwę gatunku
#             if genre in genre_files:  # sprawdzamy, czy gatunek ma przypisany plik docelowy
#                 append_book_to_file(genre_files[genre], row)  # dopisujemy książkę do właściwego pliku

# distribute_books_by_genre(SOURCE_FILE, GENRE_FILES)  # uruchamiamy przetwarzanie książek według gatunków
# print("Dane książek zostały skopiowane do odpowiednich plików według gatunku.")