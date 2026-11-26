# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Oto program, który zapisuje do pliku tekstowego dane zawierające tytuł filmu, jego reżysera oraz głównego aktora. 
# Skopiuj program do pliku movie.py, a następnie uruchom program. Na koniec otwórz utworzony plik tekstowy w edytorze i sprawdź jego zawartość.

# Aby zapisać dane do pliku, musisz otworzyć go z parametrem 'w' (zapis). Metoda write() zapisuje do pliku jedną linię danych. 
# Zwróć uwagę na znak \n. Oznacza on przejście kursorem do następnej linii. Jeśli go nie dodasz, wszystkie kolejne dane zostaną umieszczone w jednej linii

# # Zmienne zawierające szczegóły filmu
# movie_title = "Inception"
# director = "Christopher Nolan"
# lead_actor = "Leonardo DiCaprio"

# # Nazwa pliku, do którego zapisujemy dane
# file_name = 'movie_details.txt'

# # Zapisywanie szczegółów filmu do pliku
# with open(file_name, 'w') as file:
#     file.write(f"Movie Title: {movie_title}\n")
#     file.write(f"Director: {director}\n")
#     file.write(f"Lead Actor: {lead_actor}\n")

# print(f"Movie details have been written to {file_name}.") 

# Automatyczne zamykanie pliku: instrukcja with zapewnia, że plik zostanie poprawnie zamknięty po zakończeniu zapisu.

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który zapisuje listę Siedmiu Cudów Świata do pliku tekstowego w porządku alfabetycznym, z każdą nazwą w osobnym wierszu. 
# Następnie otwórz utworzony plik w edytorze i sprawdź, czy jego zawartość jest zgodna z zadaniem.

# seven_wonders = [
#     "Great Wall of China",
#     "Petra",
#     "Christ the Redeemer",
#     "Machu Picchu",
#     "Chichen Itza",
#     "Roman Colosseum",
#     "Taj Mahal",
# ]

# file_name = "seven_wonders.txt"  # nazwa pliku tekstowego, w którym zapiszemy wynik

# sorted_wonders = sorted(seven_wonders)  # sortujemy nazwy cudów świata alfabetycznie

# # Otwieramy plik w trybie zapisu ('w') z kodowaniem UTF-8 i zapisujemy każdą nazwę w osobnym wierszu
# with open(file_name, "w", encoding="utf-8") as file:
#     for item in sorted_wonders:  # przechodzimy przez posortowaną listę elementów
#         file.write(f"{item}\n")  # dopisujemy znak nowej linii, aby każdy wpis był w osobnym wierszu

# print(f"Posortowana lista Siedmiu Cudów Świata została zapisana do pliku {file_name}.")

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który kopiuje zawartość pliku healthy_lifestyle.txt do pliku copy_healthy_lifestyle.txt.
# Wskazówka: odczytaj całą zawartość oryginalnego pliku i zapisz ją do pliku docelowego (kopii).   

# original_file = "healthy_lifestyle.txt"  # nazwa pliku źródłowego do odczytu
# target_file = "copy_healthy_lifestyle.txt"  # nazwa pliku docelowego, w którym powstanie kopia

# # Otwieramy oryginalny plik w trybie odczytu ('r') z kodowaniem UTF-8 i pobieramy całą jego treść
# with open(original_file, "r", encoding="utf-8") as source_file:
#     content = source_file.read()  # wczytujemy cały tekst wraz ze wszystkimi znakami nowej linii

# # Otwieramy plik docelowy w trybie zapisu ('w') z kodowaniem UTF-8 i zapisujemy odczytaną zawartość
# with open(target_file, "w", encoding="utf-8") as destination_file:
#     destination_file.write(content)  # zapisujemy dokładnie tę samą treść do kopii pliku

# print(f"Zawartość pliku {original_file} została skopiowana do pliku {target_file}.")

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który zapisuje dane pracowników zatrudnionych na stanowisku Software Engineer do pliku software_engineer.txt. Dane znajdują się w pliku it_company.csv.
# Wskazówka: odczytuj dane pracowników linia po linii. Dla każdej linii sprawdź, czy zawiera nazwę wskazanego stanowiska. Jeśli tak, zapisz tę linię do pliku wyjściowego.

# employees_file = "it_company.csv"  # nazwa pliku wejściowego CSV z listą pracowników
# position_file = "software_engineer.txt"  # nazwa pliku wyjściowego z wybranymi pracownikami
# job_title = "Software Engineer"  # poszukiwane stanowisko pracy

# # Otwieramy jednocześnie plik wejściowy do odczytu ('r') oraz plik wyjściowy do zapisu ('w') w kodowaniu UTF-8
# with open(employees_file, "r", encoding="utf-8") as input_file:
#     with open(position_file, "w", encoding="utf-8") as output_file:
#         for line in input_file:  # czytamy plik z pracownikami linia po linii
#             if job_title in line:  # sprawdzamy, czy wiersz zawiera nazwę wskazanego stanowiska
#                 output_file.write(line)  # zapisujemy pasujący wiersz (już ze znakiem nowej linii) do pliku wynikowego

# print(f"Dane pracowników na stanowisku {job_title} zostały zapisane do pliku {position_file}.")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który pozwala utworzyć listę zakupów. Program pobiera dane wejściowe od użytkownika z klawiatury, dopóki użytkownik nie wpisze 0. 
# Każda pobrana wartość jest zapisywana do pliku tekstowego shopping_list.txt.
# Wskazówka: otwórz plik w trybie dopisywania, używając parametru 'a' (append) w funkcji open().

# shopping_list = "shopping_list.txt"  # nazwa pliku tekstowego z listą zakupów

# # Funkcja dopisująca nazwę produktu na końcu wskazanego pliku w trybie 'a'
# def add_product(file_name, product_name):
#     with open(file_name, "a", encoding="utf-8") as file:  # kolejne produkty trafiają na koniec pliku w osobnych wierszach bez kasowania wcześniejszej zawartości
#         file.write(f"{product_name}\n")  # dopisujemy produkt w nowym wierszu

# product = ""  # inicjalizujemy zmienną sterującą pętlą
# while product != "0":  # powtarzamy pobieranie nazw produktów, dopóki użytkownik nie wpisze 0
#     product = input("Podaj nazwę produktu (0 kończy): ")  # pobieramy nazwę produktu z klawiatury
#     if product == "0":
#         break  # przerywamy pętlę, gdy wpisano 0, aby nie zapisywać zera do listy zakupów
#     else:
#         add_product(shopping_list, product)  # dopisujemy wpisany produkt do pliku

# print(f"Lista zakupów została zaktualizowana w pliku {shopping_list}.")