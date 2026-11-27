# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
#   ...

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Napisz program tłumaczący słowa z języka angielskiego na język polski. Użytkownik wpisuje słowo po angielsku z klawiatury. 
# Program wyświetla tłumaczenie tego słowa albo informację, że tłumaczenie jest niedostępne.

# translations = {
#     'computer': 'komputer',
#     'mouse': 'myszka',
#     'keyboard': 'klawiatura',
#     'printer': 'drukarka'
# }  # słownik mapujący angielskie słowa na ich polskie odpowiedniki

# word = input("Podaj słowo po angielsku: ").strip().lower()  # wczytujemy słowo i ujednolicamy wielkość liter

# if word in translations:  # sprawdzamy, czy podane słowo istnieje jako klucz w słowniku
#     print(f"Tłumaczenie słowa '{word}': {translations[word]}")
# else:
#     print(f"Tłumaczenie słowa '{word}' jest niedostępne.")  # komunikat, gdy brak słowa w słowniku

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Słownik zawiera nazwy przedmiotów wraz z liczbą godzin. Napisz program, który oblicza i wypisuje łączną liczbę godzin. Przykładowe wyniki:

# winter_semester = {
#     "math": 60,
#     "programming": 30,
#     "history": 15
# }  # słownik przedmiotów i odpowiadającej im liczby godzin

# total_hours = sum(winter_semester.values())  # sumujemy wszystkie wartości (liczby godzin) ze słownika

# print(f"Łączna liczba godzin w semestrze zimowym wynosi {total_hours}.")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który zlicza, ile razy każde słowo występuje w akapicie.
# Wskazówka: Sprawdź w słowniku, czy kolejne słowo w nim występuje. Jeśli tak, zwiększ liczbę wystąpień tego słowa o 1. 
# Akapit możesz łatwo podzielić na pojedyncze słowa za pomocą metody split(). Wyszukaj w internecie, jak jej używać. 

# paragraph = "cat dog mouse cat rat cat mouse"  # przykładowy tekst wejściowy
# words = paragraph.split()  # dzielimy akapit na listę pojedynczych słów według spacji
# word_counts = {}  # pusty słownik: słowo -> liczba wystąpień

# for word in words:  # przeglądamy kolejne słowa z listy
#     if word in word_counts:  # jeśli słowo pojawiło się już wcześniej w słowniku[cite: 20]
#         word_counts[word] += 1  # zwiększamy jego licznik o 1[cite: 20]
#     else:
#         word_counts[word] = 1  # jeśli słowo pojawia się po raz pierwszy, ustawiamy licznik na 1

# print("Liczba wystąpień poszczególnych słów:")
# for word, count in word_counts.items():  # wypisujemy każde słowo oraz liczbę jego wystąpień po polsku
#     print(f"{word}: {count}")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Program zawiera dwa słowniki z danymi osobowymi. Napisz program, który tworzy słownik o nazwie person zawierający dane z obu pozostałych słowników (pięć par klucz-wartość). 
# Wypisz zawartość słownika person.

# basic_data = {
#     "name": "Barbara",
#     "age": 21
# }  # podstawowe dane osobowe

# advanced_data = {
#     "status": "student",
#     "married": False,
#     "interest": ["reading", "swimming"]
# }  # rozszerzone dane osobowe

# person = basic_data | advanced_data  # łączymy oba słowniki w nowy słownik person (pięć par klucz-wartość)

# print("Zawartość słownika person:")
# for key, value in person.items():  # wypisujemy wszystkie pary klucz-wartość ze słownika person
#     print(f"{key}: {value}")

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Program zawiera dwie funkcje:
    # i. hotel_list(hotels), która zwraca listę nazw hoteli rozdzielonych przecinkiem
    # ii. avg_price(hotels), która zwraca średnią cenę pokoju dla podanej listy hoteli, zaokrągloną do wartości całkowitej
# Napisz program, który oblicza i wyświetla średnią cenę pokoju w hotelach w Krakowie i Sopocie oraz wskazuje, w którym mieście hotele są tańsze.

# hotels_in_Krakow = [
#     {"name": "Sky", "price": 320.00},
#     {"name": "Metropol", "price": 480.00},
#     {"name": "New Port", "price": 420.00},
#     {"name": "Aparthotel", "price": 390.00}
# ]  # lista słowników reprezentujących hotele w Krakowie

# hotels_in_Sopot = [
#     {"name": "Focus", "price": 510.00},
#     {"name": "Aqua", "price": 345.00},
#     {"name": "La Boutique", "price": 390.00},
#     {"name": "Marina", "price": 410.00}
# ]  # lista słowników reprezentujących hotele w Sopocie


# def hotel_list(hotels):
#     """Zwraca listę nazw hoteli oddzielonych przecinkiem."""
#     names = []  # lista na nazwy hoteli
#     for hotel in hotels:  # przeglądamy każdy słownik z opisem hotelu
#         names.append(hotel["name"])  # pobieramy wartość pod kluczem 'name'
#     return ", ".join(names)  # łączymy nazwy w napis rozdzielony przecinkiem


# def avg_price(hotels):
#     """Zwraca średnią cenę pokoju dla podanej listy hoteli zaokrągloną do liczby całkowitej."""
#     if not hotels:  # zabezpieczenie na wypadek pustej listy hoteli
#         return 0
#     total = 0.0  # suma cen pokoi
#     for hotel in hotels:  # sumujemy ceny ze wszystkich hoteli na liście
#         total += hotel["price"]
#     average = total / len(hotels)  # obliczamy średnią arytmetyczną
#     return round(average)  # zaokrąglamy wynik do wartości całkowitej


# krakow_names = hotel_list(hotels_in_Krakow)  # nazwy hoteli w Krakowie
# krakow_avg = avg_price(hotels_in_Krakow)  # średnia cena w Krakowie (1610 / 4 = 402.5 -> 402)

# sopot_names = hotel_list(hotels_in_Sopot)  # nazwy hoteli w Sopocie
# sopot_avg = avg_price(hotels_in_Sopot)  # średnia cena w Sopocie (1655 / 4 = 413.75 -> 414)

# print(f"Hotele w Krakowie: {krakow_names}")
# print(f"Średnia cena hotelu w Krakowie: {krakow_avg}")
# print(f"Hotele w Sopocie: {sopot_names}")
# print(f"Średnia cena hotelu w Sopocie: {sopot_avg}")

# if krakow_avg < sopot_avg:  # porównujemy średnie ceny i wypisujemy tańsze miasto
#     print("Tańsze hotele są w: Krakowie")
# elif sopot_avg < krakow_avg:
#     print("Tańsze hotele są w: Sopocie")
# else:
#     print("Średnie ceny hoteli w Krakowie i Sopocie są równe.")

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Napisz program obliczający łączny koszt koszyka zakupowego na podstawie cennika.

# prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# # Koszyk zakupowy (nazwa produktu -> zakupiona ilość)
# cart = {'juice': 3, 'bread': 1, 'milk': 2}

# total_cost = 0.0  # zmienna przechowująca sumę kosztów całego koszyka

# for item, quantity in cart.items():  # przeglądamy kolejne pozycje i ich ilości w koszyku
#     if item in prices:  # sprawdzamy, czy produkt znajduje się w cenniku
#         total_cost += prices[item] * quantity  # doliczamy koszt danej pozycji (cena * ilość)
#     else:
#         print(f"Uwaga: brak produktu '{item}' w cenniku, pomijam.")

# print(f"Łączny koszt koszyka wynosi: {total_cost:.2f}")

# ZADANIE 9________________________________________________________________________________________________________________________________________________________________________
# Kamera drogowa rejestruje przejeżdżające pojazdy. Kamera zapisuje ich numery rejestracyjne w pliku vehicle.txt. 
# Napisz program, który oblicza i wypisuje, ile zarejestrowanych samochodów pochodzi z każdego województwa Polski. 
# Lista województw oraz odpowiadające im pierwsze litery numerów rejestracyjnych pojazdów znajdują się w pliku province.csv.   
# Wskazówka: użyj słownika zawierającego litery odpowiadające województwom oraz liczby pojazdów, których pierwsze litery numeru rejestracyjnego pasują do liter województwa.   

# import csv

# # Program zliczający pojazdy z poszczególnych województw na podstawie plików province.csv oraz vehicle.txt

# letter_to_province = {}  # słownik mapujący pierwszą literę rejestracji -> nazwa województwa
# province_counts = {}  # słownik zliczający pojazdy dla każdego województwa: województwo -> liczba

# # Wczytujemy powiązania litery rejestracji z województwem z pliku province.csv
# with open("province.csv", "r", encoding="utf-8", newline="") as csv_file:
#     reader = csv.DictReader(csv_file)  # czytamy wiersze jako słowniki na podstawie nagłówków kolumn
#     for row in reader:
#         # Dopasowujemy nazwy kolumn (np. 'Letter'/'Province' lub 'letter'/'province') bez względu na wielkość liter
#         normalized_row = {key.strip().lower(): value.strip() for key, value in row.items() if key}
#         letter = normalized_row.get("letter", "").upper()
#         province = normalized_row.get("province", "")
#         if letter and province:
#             letter_to_province[letter] = province  # wiążemy pierwszą literę tablicy z województwem
#             province_counts[province] = 0  # inicjalizujemy licznik pojazdów dla danego województwa

# # Odczytujemy numery rejestracyjne z pliku vehicle.txt i zliczamy auta według pierwszej litery
# with open("vehicle.txt", "r", encoding="utf-8") as vehicle_file:
#     for line in vehicle_file:
#         registration = line.strip().upper()  # usuwamy białe znaki i ujednolicamy wielkość liter
#         if not registration:  # pomijamy puste linie
#             continue
#         first_letter = registration[0]  # pobieramy pierwszą literę numeru rejestracyjnego
#         if first_letter in letter_to_province:  # sprawdzamy, czy litera odpowiada znanemu województwu
#             province_name = letter_to_province[first_letter]
#             province_counts[province_name] += 1  # zwiększamy licznik pojazdów dla tego województwa
#         else:
#             print(f"Nie rozpoznano województwa dla rejestracji: {registration}")

# print("Liczba zarejestrowanych pojazdów według województw:")
# for province, count in province_counts.items():  # wypisujemy zestawienie po polsku
#     print(f"{province}: {count}")

# ZADANIE 10________________________________________________________________________________________________________________________________________________________________________
#   ...

# ZADANIE 11________________________________________________________________________________________________________________________________________________________________________
# Napisz program rejestrujący głosowanie. Wyniki głosowania są zapisywane w pliku voting.json o poniższej strukturze. 
# Program pobiera z klawiatury imię osoby i zwiększa liczbę głosów oddanych na tę osobę o 1. Jeśli jest to nowa osoba, zostaje dodana do listy z liczbą głosów równą 1. 
# Program można uruchamiać wielokrotnie, aby dodawać kolejne głosy do pliku JSON.

# import json
# import os

# # Program rejestrujący głosy na wybraną osobę i zapisujący wyniki w pliku voting.json

# voting_file = "voting.json"  # nazwa pliku JSON przechowującego wyniki głosowania

# # Odczytujemy zawartość pliku json, jeśli plik już istnieje; w przeciwnym razie startujemy z pustym słownikiem
# if os.path.exists(voting_file):  # sprawdzamy, czy plik voting.json znajduje się na dysku
#     with open(voting_file, "r", encoding="utf-8") as file:  # otwieramy plik do odczytu w kodowaniu UTF-8
#         votes = json.load(file)  # wczytujemy słownik z wynikami głosowania
# else:
#     votes = {}  # tworzymy pusty słownik, gdy głosowanie dopiero się zaczyna

# # Oddajemy głos na wskazaną osobę
# person_name = input("Podaj imię osoby, na którą głosujesz: ").strip()  # wczytujemy imię i usuwamy zbędne spacje

# if person_name == "":  # zabezpieczenie przed pustym imieniem
#     print("Nie podano imienia. Głos nie został zapisany.")
# else:
#     if person_name in votes:  # jeśli osoba jest już w słowniku, zwiększamy liczbę jej głosów o 1
#         votes[person_name] += 1
#     else:  # jeśli to nowa osoba, dodajemy ją z liczbą głosów równą 1
#         votes[person_name] = 1

#     # Zapisujemy zaktualizowane dane głosowania do pliku json
#     with open(voting_file, "w", encoding="utf-8") as file:  # otwieramy plik do zapisu w kodowaniu UTF-8
#         json.dump(votes, file, ensure_ascii=False, indent=4)  # zapisujemy słownik z czytelnym wcięciem

#     print(f"Zapisano głos na osobę '{person_name}'. Aktualna liczba głosów: {votes[person_name]}.")

# ZADANIE 12________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję, która przyjmuje napis jako wejście i używa stosu do jego odwrócenia. Następnie napisz program, który odwraca dowolny tekst wpisany z klawiatury.
# Wskazówka: Odłóż każdy znak napisu na stos, a następnie zdejmuj znaki, aby utworzyć odwrócony napis. 

# import queue

# def reverse_text(text):
#     """Zwraca podany napis odwrócony znak po znaku przy użyciu stosu LIFO."""
#     stack = queue.LifoQueue()  # tworzymy stos na znaki napisu (zasada LIFO)

#     for char in text:  # odkładamy każdy znak napisu na wierzch stosu
#         stack.put(char)

#     reversed_chars = []  # lista na znaki zdejmowane ze stosu w odwrotnej kolejności
#     while not stack.empty():  # zdejmujemy znaki ze stosu, dopóki nie będzie pusty
#         reversed_chars.append(stack.get())

#     return "".join(reversed_chars)  # łączymy znaki w jeden odwrócony napis

# user_text = input("Podaj dowolny tekst do odwrócenia: ")  # wczytujemy tekst z klawiatury
# result = reverse_text(user_text)  # odwracamy wpisany tekst za pomocą funkcji

# print(f"Oryginalny tekst: {user_text}")
# print(f"Odwrócony tekst: {result}")

# ZADANIE 13________________________________________________________________________________________________________________________________________________________________________
# Wyszukaj w internecie informacje i zapoznaj się z odwrotną notacją polską (RPN, Reverse Polish Notation).
# Następnie napisz program, który oblicza wyrażenia w zapisie RPN. Wyrażenia RPN można wygodnie obliczać za pomocą stosu. 
# Użytkownik może wpisywać z klawiatury dowolną liczbę, operator (+, -, *, /) albo znak równości (=).

    # i. Jeśli wpisana wartość jest liczbą, połóż tę liczbę na stosie.
    # ii. Jeśli wpisana wartość jest operatorem, zdejmij dwa elementy z wierzchu stosu, wykonaj działanie i połóż wynik operacji na stosie.
    # iii. Jeśli wpisana wartość jest znakiem równości, zdejmij końcowy wynik ze stosu i wyświetl wynik obliczeń.

# import queue

# stack = queue.LifoQueue()  # stos przechowujący liczby oraz wyniki pośrednie działań

# print("Kalkulator RPN. Wpisuj liczby, operatory (+, -, *, /) lub '=' aby wyświetlić wynik.")

# while True:  # wczytujemy kolejne elementy wyrażenia aż do napotkania znaku '='
#     token = input("Podaj liczbę, operator (+, -, *, /) lub '=': ").strip()

#     if token == "=":  # znak równości kończy wprowadzanie i pobiera końcowy wynik ze stosu
#         if stack.empty():
#             print("Stos jest pusty, brak wyniku do wyświetlenia.")
#         else:
#             result = stack.get()  # zdejmujemy wynik końcowy z wierzchu stosu
#             print(f"Wynik obliczeń: {result}")
#         break

#     elif token in ("+", "-", "*", "/"):  # obsługa operatorów arytmetycznych
#         if stack.qsize() < 2:  # do wykonania działania potrzebujemy co najmniej dwóch liczb na stosie
#             print("Za mało liczb na stosie, aby wykonać operację.")
#             continue

#         # Pierwszy zdjęty element to prawy operand (druga liczba w działaniu), a drugi to lewy operand (pierwsza liczba)
#         second_operand = stack.get()
#         first_operand = stack.get()

#         if token == "+":
#             operation_result = first_operand + second_operand
#         elif token == "-":
#             operation_result = first_operand - second_operand
#         elif token == "*":
#             operation_result = first_operand * second_operand
#         elif token == "/":
#             if second_operand == 0:
#                 print("Błąd: nie można dzielić przez zero.")
#                 stack.put(first_operand)  # odkładamy liczby z powrotem na stos, aby nie stracić danych
#                 stack.put(second_operand)
#                 continue
#             operation_result = first_operand / second_operand

#         stack.put(operation_result)  # odkładamy wynik działania z powrotem na wierzch stosu

#     else:  # próbujemy potraktować wpisany token jako liczbę
#         try:
#             number = float(token)
#             if number.is_integer():  # jeśli liczba jest całkowita (np. 5.0), przechowujemy ją jako int dla czystszego zapisu
#                 number = int(number)
#             stack.put(number)  # kładziemy liczbę na wierzchu stosu
#         except ValueError:
#             print("Nieprawidłowy znak. Wpisz liczbę, operator (+, -, *, /) lub '='.")

# ZADANIE 14________________________________________________________________________________________________________________________________________________________________________
# Napisz program obsługujący obsługę klienta w urzędzie lub biurze. Użyj kolejki. 
# Każdy nowy klient otrzymuje bilet z automatycznie przypisywanym kolejnym numerem i jest dodawany na koniec kolejki. Następny klient do obsłużenia jest pobierany z początku kolejki.

# import queue

# customer_queue = queue.Queue()  # kolejka przechowująca numery biletów oczekujących klientów
# next_ticket_number = 1  # licznik automatycznie przydzielanych kolejnych numerów biletów

# while True:  # główna pętla obsługi klientów w urzędzie
#     print("1. Nowy klient (pobierz bilet)")
#     print("2. Obsłuż następnego klienta")
#     print("3. Pokaż liczbę oczekujących klientów")
#     print("0. Wyjdź")
#     choice = input("Wybierz opcję: ").strip()

#     if choice == "1":  # przydzielamy kolejny numer biletu i dopisujemy klienta na koniec kolejki
#         ticket = next_ticket_number
#         customer_queue.put(ticket)  # dodajemy bilet na koniec kolejki FIFO
#         next_ticket_number += 1  # zwiększamy licznik dla kolejnego klienta
#         print(f"Wydano bilet nr {ticket}. Klient dodany na koniec kolejki.")

#     elif choice == "2":  # pobieramy klienta z początku kolejki do obsługi
#         if not customer_queue.empty():  # sprawdzamy, czy ktoś czeka w kolejce
#             served_ticket = customer_queue.get()  # zdejmujemy najstarszy bilet z początku kolejki
#             print(f"Proszę do stanowiska — obsługiwany jest bilet nr {served_ticket}.")
#         else:
#             print("Brak klientów oczekujących w kolejce.")

#     elif choice == "3":  # informujemy o aktualnej liczbie oczekujących osób
#         print(f"Liczba klientów w kolejce: {customer_queue.qsize()}")

#     elif choice == "0":  # kończymy pracę programu
#         print("Kończę obsługę klientów.")
#         break

#     else:
#         print("Nieprawidłowa opcja. Wybierz 1, 2, 3 lub 0.")

# ZADANIE 15________________________________________________________________________________________________________________________________________________________________________
# JSON (JavaScript Object Notation) to lekki format wymiany danych, który jest łatwy do odczytania i napisania dla ludzi oraz łatwy do parsowania i generowania przez maszyny. 
# Często służy do przesyłania danych między serwerem a aplikacją internetową, a także do przechowywania danych ustrukturyzowanych.
# Zwróć uwagę na główne cechy formatu JSON:

    # Czytelność: JSON jest oparty na tekście, dzięki czemu ludzie mogą go łatwo odczytać.
    # Prostota: opiera się na parach klucz–wartość.
    # Niezależność od języka: chociaż wywodzi się z języka JavaScript, JSON jest obsługiwany przez wiele języków programowania, takich jak Python, Java, PHP, C# i inne.

# ZADANIE 16________________________________________________________________________________________________________________________________________________________________________
# Plik computer.json zawiera przykładowe dane komputera. Otwórz plik JSON w edytorze i przejrzyj jego zawartość. Zwróć uwagę, że plik zawiera pojedynczy słownik danych.
# Następnie napisz program, który wypisuje informacje o komputerze.

# import json

# # Otwieramy plik computer.json w trybie do odczytu z jawnym kodowaniem UTF-8
# with open('computer.json', 'r', encoding='utf-8') as file:
#     # Wczytujemy zawartość pliku JSON do zmiennej data (pojedynczy słownik)
#     data = json.load(file)

# print("Informacje o komputerze:")

# # Przechodzimy przez wszystkie pary klucz-wartość wczytane z pliku JSON
# for key, value in data.items():
#     print(f"{key} : {value}")

# ZADANIE 17________________________________________________________________________________________________________________________________________________________________________
# Plik cities.json zawiera dane o wybranych miastach w Polsce. Otwórz plik JSON w edytorze i przejrzyj jego zawartość. Zwróć uwagę, że plik zawiera tablicę słowników.   
# Następnie napisz program, który wypisuje informacje o miastach.   
# Uwaga: użycie parametru encoding='utf-8' podczas otwierania pliku jest konieczne, ponieważ plik JSON zawiera również polskie znaki w nazwach miast, które muszą zostać 
# poprawnie przetworzone. Pamiętaj, aby zawsze używać tego parametru podczas otwierania plików zawierających znaki spoza alfabetu łacińskiego.

# import json

# # Otwieramy plik cities.json w trybie do odczytu z jawnym kodowaniem UTF-8 dla polskich znaków
# with open('cities.json', 'r', encoding='utf-8') as file:
#     # Wczytujemy tablicę obiektów JSON jako listę słowników w Pythonie
#     data = json.load(file)

# print("Informacje o wybranych miastach w Polsce:\n")

# # Zewnętrzna pętla przechodzi przez kolejne słowniki reprezentujące miasta na liście
# for city in data:
#     # Wewnętrzna pętla wypisuje wszystkie pary klucz-wartość danego miasta
#     for key, value in city.items():
#         print(f"{key} : {value}")
#     print()  # pusty wiersz oddzielający kolejne miasta

# ZADANIE 18________________________________________________________________________________________________________________________________________________________________________
# Plik dogs.json zawiera dane o psach. Napisz program, który wypisuje informacje o psach młodszych niż 5 lat.

# import json

# # Otwieramy plik dogs.json w trybie do odczytu z jawnym kodowaniem UTF-8
# with open("dogs.json", "r", encoding="utf-8") as file:
#     dogs = json.load(file)  # wczytujemy listę słowników opisujących poszczególne psy

# print("Psy młodsze niż 5 lat:\n")

# for dog in dogs:  # przeglądamy po kolei każdy słownik psa z listy
#     if dog["age"] < 5:  # sprawdzamy, czy wiek psa jest mniejszy niż 5 lat
#         for key, value in dog.items():  # wypisujemy wszystkie pary klucz-wartość dla wybranego psa
#             print(f"{key}: {value}")
#         print()  # pusty wiersz oddzielający kolejne psy

# ZADANIE 19________________________________________________________________________________________________________________________________________________________________________
# System informatyczny hotelu zawiera listę zarezerwowanych pokoi. Dane znajdują się w pliku reservations.json. 
# Napisz program, który wypisuje podsumowanie zgodnie z poniższymi punktami. Podziel program na mniejsze części, definiując funkcje:
#     liczba pokoi
#     liczba opłaconych rezerwacji
#     liczba nieopłaconych rezerwacji
#     łączna wartość opłaconych rezerwacji
#     łączna wartość nieopłaconych rezerwacji

# import json

# def load_reservations(filename):
#     """Wczytuje listę rezerwacji z pliku JSON z jawnym kodowaniem UTF-8."""
#     with open(filename, "r", encoding="utf-8") as file:
#         return json.load(file)  # zwraca listę słowników opisujących rezerwacje


# def count_rooms(reservations):
#     """Zwraca liczbę zarezerwowanych pokoi (wpisów w liście rezerwacji)."""
#     return len(reservations)


# def get_paid_and_unpaid_stats(reservations):
#     """Oblicza liczbę oraz łączną wartość opłaconych i nieopłaconych rezerwacji."""
#     paid_count = 0  # licznik opłaconych rezerwacji
#     unpaid_count = 0  # licznik nieopłaconych rezerwacji
#     paid_total = 0.0  # suma kwot za opłacone rezerwacje
#     unpaid_total = 0.0  # suma kwot za nieopłacone rezerwacje

#     for reservation in reservations:  # przeglądamy każdą rezerwację z listy
#         is_paid = reservation.get("paid", False)  # status opłacenia rezerwacji
#         nights = reservation.get("nights", 1)  # liczba nocy (domyślnie 1, jeśli brak klucza)
#         price_per_night = reservation.get("price_per_night", reservation.get("price", 0))  # cena za noc lub łączna cena

#         # Jeśli w rekordzie występuje osobna liczba nocy oraz cena za noc, mnożymy je; w przeciwnym razie bierzemy cenę
#         if "nights" in reservation and ("price_per_night" in reservation or "price" in reservation):
#             amount = nights * price_per_night
#         else:
#             amount = reservation.get("total_price", reservation.get("amount", 0))

#         if is_paid:  # rozdzielamy statystyki na rezerwacje opłacone i nieopłacone
#             paid_count += 1
#             paid_total += amount
#         else:
#             unpaid_count += 1
#             unpaid_total += amount

#     return paid_count, unpaid_count, paid_total, unpaid_total


# def print_summary(reservations):
#     """Wypisuje pełne podsumowanie rezerwacji w języku polskim."""
#     rooms_count = count_rooms(reservations)  # liczba pokoi
#     paid_count, unpaid_count, paid_total, unpaid_total = get_paid_and_unpaid_stats(reservations)

#     print("Podsumowanie rezerwacji hotelowych:")
#     print(f"Liczba pokoi: {rooms_count}")
#     print(f"Liczba opłaconych rezerwacji: {paid_count}")
#     print(f"Liczba nieopłaconych rezerwacji: {unpaid_count}")
#     print(f"Łączna wartość opłaconych rezerwacji: {paid_total:.2f}")
#     print(f"Łączna wartość nieopłaconych rezerwacji: {unpaid_total:.2f}")


# reservations_data = load_reservations("reservations.json")  # wczytujemy dane rezerwacji z pliku JSON
# print_summary(reservations_data)  # wyświetlamy podsumowanie na ekranie

# ZADANIE 20________________________________________________________________________________________________________________________________________________________________________
# Poniższy program zapisuje dane do pliku JSON. Przeanalizuj ten program. Następnie uruchom go i sprawdź, czy plik JSON został utworzony. Wyświetl utworzony plik JSON w edytorze.

# import json

# data = {
#     "patient_record": {
#         "patient_id": "P001234",
#         "first_name": "John",
#         "last_name": "Doe",
#         "date_of_birth": "1985-05-15",
#         "gender": "Male",
#         "contact_info": {
#             "phone_number": "+1-555-123-4567",
#             "email": "johndoe@example.com",
#             "address": {
#                 "street": "123 Main St",
#                 "city": "New York",
#                 "state": "NY",
#                 "postal_code": "10001",
#                 "country": "USA"
#             }
#         },
#         "medical_history": {
#             "allergies": ["Penicillin", "Peanuts"],
#             "current_medications": ["Lisinopril 10mg", "Metformin 500mg"],
#             "past_illnesses": ["Hypertension", "Type 2 Diabetes"],
#             "surgeries": [
#                 {
#                     "surgery_type": "Appendectomy",
#                     "date": "2015-08-20"
#                 }
#             ]
#         }
#     }
# }  # zagnieżdżony słownik łączący obiekty, listy oraz listę słowników

# # Określamy nazwę i ścieżkę docelowego pliku JSON
# file_name = "patient.json"

# # Otwieramy plik w trybie do zapisu ('w') z jawnym kodowaniem UTF-8 i zapisujemy strukturę JSON
# with open(file_name, "w", encoding="utf-8") as file:
#     json.dump(data, file, indent=4, ensure_ascii=False)

# print(f"Dane zostały zapisane do pliku {file_name}.")

# ZADANIE 21________________________________________________________________________________________________________________________________________________________________________
# Utwórz słownik opisujący Twoją ulubioną książkę lub film, zawierający co najmniej pięć par klucz–wartość. Następnie napisz program, który zapisze dane ze słownika do pliku

# import json

# favourite_book = {
#     "title": "Milczenie owiec",
#     "author": "Thomas Harris",
#     "year": 1988,
#     "genre": "thriller psychologiczny",
#     "rating": 9.5,
#     "main_characters": ["Clarice Starling", "Hannibal Lecter"]
# }  # słownik zawierający sześć par klucz-wartość (napisy, liczbę całkowitą, zmiennoprzecinkową oraz listę)

# file_name = "favourite.json"  # nazwa pliku docelowego w formacie JSON

# # Otwieramy plik w trybie do zapisu ('w') z jawnym kodowaniem UTF-8 i zapisujemy zawartość słownika
# with open(file_name, "w", encoding="utf-8") as file:
#     json.dump(favourite_book, file, indent=4, ensure_ascii=False)

# print(f"Dane ulubionej pozycji zostały zapisane do pliku {file_name}.")

# ZADANIE 22________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który pobiera z klawiatury dane o zakupionym produkcie:
    # nazwa (name)
    # cena (price — liczba rzeczywista z dwoma miejscami po przecinku)
    # opłacone (paid — yes/no)
# Następnie program zapisuje dane produktu w pliku product.json. Zwróć uwagę na odpowiednie typy danych opisujące produkt (string, float, bool).

# import json

# product = {}  # słownik opisujący zakupiony produkt (name: str, price: float, paid: bool)

# # Wczytujemy dane produktu z klawiatury i konwertujemy je na docelowe typy
# name = input("Podaj nazwę produktu: ").strip()  # typ str

# price_input = input("Podaj cenę produktu (np. 19.99): ").strip().replace(",", ".")  # obsługujemy też przecinek
# price = round(float(price_input), 2)  # typ float zaokrąglony do dwóch miejsc po przecinku

# paid_input = input("Czy produkt jest opłacony (yes/no)? ").strip().lower()
# paid = paid_input in ("yes", "y", "tak", "t", "true", "1")  # typ bool

# # Budujemy słownik z odpowiednimi typami danych
# product = {
#     "name": name,
#     "price": price,
#     "paid": paid
# }

# # Zapisujemy dane produktu do pliku product.json z jawnym kodowaniem UTF-8
# with open("product.json", "w", encoding="utf-8") as file:
#     json.dump(product, file, indent=4, ensure_ascii=False)

# print("Dane produktu zostały zapisane do pliku product.json.")

# ZADANIE 23________________________________________________________________________________________________________________________________________________________________________
# Strona [https://api.nbp.pl/en.html](https://api.nbp.pl/en.html) zawiera dane o kursach walut publikowanych przez Narodowy Bank Polski. 
# Serwis udostępnia dane zarówno w formacie JSON, jak i XML. Wyświetl dziesięć ostatnich kursów euro w formacie JSON w przeglądarce internetowej. 
# Następnie zapisz te dane do pliku euro.json. Na koniec napisz program, który wyświetla dane z pliku euro.json

# import json

# # Otwieramy plik euro.json w trybie do odczytu z jawnym kodowaniem UTF-8
# with open("euro.json", "r", encoding="utf-8") as file:
#     data = json.load(file)  # wczytujemy strukturę JSON zwróconą przez API NBP

# rates = data["rates"]  # pobieramy listę notowań z klucza 'rates'

# # Wyświetlamy nagłówek tabeli oraz linię oddzielającą
# print(f"{'Date':<14}{'Buying Rate':<16}{'Selling Rate'}")
# print("=" * 50)

# # Przechodzimy przez wszystkie notowania i wypisujemy datę, kurs kupna oraz kurs sprzedaży
# for rate in rates:
#     effective_date = rate["effectiveDate"]
#     bid_rate = f"{rate['bid']:.4f}"  # kurs kupna (Buying Rate)
#     ask_rate = f"{rate['ask']:.4f}"  # kurs sprzedaży (Selling Rate)
#     print(f"{effective_date:<14}{bid_rate:<16}{ask_rate}")
