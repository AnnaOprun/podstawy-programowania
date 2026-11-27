# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Słownik to wbudowana struktura danych, która przechowuje dane w postaci par klucz–wartość. Każdy klucz jest unikalny i odwzorowuje konkretną wartość, 
# co pozwala sprawnie pobierać, aktualizować i zarządzać danymi. Słowniki są mutowalne, co oznacza, że możesz zmieniać ich zawartość po utworzeniu.

# Spójrz na poniższy słownik. Zawiera on trzy elementy oddzielone przecinkami. Każdy element słownika składa się z klucza oraz wartości, 
# gdzie klucz działa jako identyfikator pozwalający uzyskać dostęp do powiązanej z nim wartości.

# student = {'name':'John', 'age':25, 'major':'Computer Science'}

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Zapoznaj się z podstawowymi operacjami, jakie możesz wykonywać na słowniku.

# ============================================================ Podstawowe operacje na słowniku
# Utworzenie słownika
# student = {
#     'name': 'John',
#     'age': 22,
#     'major': 'Computer Science'
# }

# # Dostęp do wartości
# print(student['name'])

# # Dodanie nowej pary klucz-wartość
# student['grade'] = 'A'

# # Modyfikacja istniejącej wartości
# student['age'] = 23

# # Usunięcie pary klucz-wartość
# del student['major']
# print(student)

# ============================================================ Iterowanie po słowniku
# Utworzenie słownika
# fruits = {
#           'apple': 3, 
#           'banana': 5, 
#           'orange': 2
#           }

# # Iterowanie po kluczach
# for fruit in fruits:
#     print(fruit)

# # Iterowanie po wartościach
# for count in fruits.values():
#     print(count)

# # Iterowanie po parach klucz-wartość
# for fruit, count in fruits.items():
#     print(f"Liczba owoców ({fruit}) wynosi {count}")

# ============================================================ Sprawdzanie, czy klucz istnieje
# Utworzenie słownika
# person = {'name': 'Alice', 'age': 30}

# # Sprawdzenie, czy klucz istnieje
# if 'name' in person:
#     print("Imię znajduje się w słowniku.")
# else:
#     print("Brak imienia.")

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Utwórz słownik opisujący Twój telefon komórkowy. Użyj 6 par klucz–wartość. Następnie, za pomocą pętli for, wyświetl zawartość słownika. 
# Aby odczytać klucz i wartość, użyj metody items().

# mobile = {
#     "OS": "IOS",  # system operacyjny telefonu
#     "brand": "Iphone",  # marka urządzenia
#     "model": "16 PRO",  # model telefonu
#     "memory_gb": 258,  # pamięć wewnętrzna w gigabajtach
#     "dual_sim": False,  # obsługa dwóch kart SIM
#     "color": "czarny"  # kolor obudowy
# }

# print("Dane telefonu komórkowego:")
# for key, value in mobile.items():  # iterujemy po parach klucz-wartość zwracanych przez items()
#     print(f"{key} : {value}")  # wypisujemy klucz oraz przypisaną do niego wartość

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Utwórz słownik taki jak w poniższym przykładzie. Czy wiesz, jaki typ wartości użyto w każdej z sześciu par klucz–wartość?

# person = {
#     "name": "Marek",  # str (napis)
#     "surname": "Banach",  # str (napis)
#     "age": 25,  # int (liczba całkowita)
#     "hobby": ["swimming", "excursions"],  # list (lista napisów)
#     "married": True,  # bool (wartość logiczna)
#     "phone": {"landline": "123444321", "mobile": "777888999"}  # dict (zagnieżdżony słownik)
# }

# # i. Wyświetla imię
# print("Imię:", person["name"])

# # ii. Wyświetla hobby
# print("Hobby:", person["hobby"])

# # iii. Wyświetla całą zawartość słownika
# print("Cała zawartość słownika:", person)

# # iv. Zmienia nazwisko na 'Nowak'
# person["surname"] = "Nowak"

# # v. Zmienia status małżeński osoby (z True na False)
# person["married"] = False

# # vi. Dodaje płeć: 'male'
# person["gender"] = "male"

# # vii. Dodaje nowe hobby: 'bicycle' do listy pod kluczem 'hobby'
# person["hobby"].append("bicycle")

# # viii. Dodaje telefon służbowy do istniejących telefonów pod kluczem 'phone'
# person["phone"]["work"] = "313131444"

# # ix. Wyświetla całą zawartość słownika, iterując po elementach słownika
# print("Zawartość słownika po modyfikacjach:")
# for key, value in person.items():
#     print(f"{key} : {value}")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Utwórz tablicę (listę) zawierającą 5 słowników, z których każdy przechowuje nazwę kraju oraz jego liczbę ludności. Następnie wypisz zawartość tablicy.

# countries = [
#     {"name": "Poland", "population": 38000000},  # pierwszy rekord kraju z liczbą ludności
#     {"name": "Germany", "population": 83200000},  # drugi rekord kraju
#     {"name": "France", "population": 67800000},  # trzeci rekord kraju
#     {"name": "Italy", "population": 58900000},  # czwarty rekord kraju
#     {"name": "Spain", "population": 48300000}  # piąty rekord kraju
# ]

# print("COUNTRY  POPULATION")  # wypisujemy nagłówek tabeli zgodnie z przykładem
# for country in countries:  # iterujemy przez każdy słownik znajdujący się na liście countries
#     print(f"{country['name']} {country['population']}")  # odczytujemy pola 'name' oraz 'population' z danego słownika

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje dane osób z książki telefonicznej, których imiona zaczynają się na literę 'D'.

# Program wypisujący dane kontaktowe osób ze słownika phone_book, których imię zaczyna się na literę 'D'

# phone_book = {
#     'John': '555-1234',
#     'David': '555-5678',
#     'Bob': '555-8765',
#     'Charlie': '555-4321',
#     'Diana': '555-9876',
#     'Eve': '555-6543',
#     'Frank': '555-3456',
#     'Grace': '555-7890',
#     'Hank': '555-1111',
#     'Ivy': '555-2222',
#     'Jack': '555-3333',
#     'Daniel': '555-4444',
#     'Liam': '555-5555',
#     'Mia': '555-6666',
#     'Nina': '555-7777',
#     'Oscar': '555-8888',
#     'Paul': '555-9999',
#     'Dominic': '555-1010',
#     'Rachel': '555-2020',
#     'Sam': '555-3030'
# }

# print("Osoby w książce telefonicznej na literę 'D':")
# for name, number in phone_book.items():  # przechodzimy przez wszystkie pary imię-numer w słowniku
#     if name.startswith("D"):  # sprawdzamy, czy imię (klucz) zaczyna się od wielkiej litery 'D'
#         print(f"{name}: {number}")  # wypisujemy imię oraz przypisany numer telefonu

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Poniższe dane zawierają informacje o liczbie produktów dostępnych w sklepie komputerowym. Napisz program, który wypisuje:
    # listę produktów oraz ich ilość,
    # łączną liczbę produktów w sklepie.

# inventory = {
#     'Laptop': 15,
#     'Desktop PC': 10,
#     'Monitor': 25,
#     'Keyboard': 50,
#     'Mouse': 60,
#     'External Hard Drive': 30,
#     'Printer': 12,
#     'Router': 20,
#     'USB Flash Drive': 100,
#     'Graphics Card': 8
# }

# total_quantity = 0  # licznik przechowujący łączną liczbę wszystkich produktów w sklepie

# print("Lista produktów i ich ilość:")
# for product, quantity in inventory.items():  # iterujemy po parach nazwa produktu - ilość
#     print(f"{product}: {quantity}")  # wypisujemy nazwę produktu oraz jego stan magazynowy
#     total_quantity += quantity  # doliczamy ilość danego produktu do łącznej sumy

# print(f"Łączna liczba produktów w sklepie: {total_quantity}")

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Poniższe dane zawierają cennik produktów ze sklepu odzieżowego wraz z ich cenami. Z powodu sezonowej wyprzedaży sklep obniża cenę każdego produktu o 10%. Napisz program, który:
    # wypisuje listę produktów oraz ich ceny przed obniżką,
    # wypisuje łączną wartość produktów przed obniżką,
    # modyfikuje cennik zgodnie z obniżką (zaokrąglając ceny do dwóch miejsc po przecinku),
    # wypisuje listę produktów oraz ich ceny po 10% obniżce,
    # wypisuje łączną wartość produktów po obniżce.

# Program wyświetlający cennik przed i po 10% obniżce oraz obliczający łączną wartość produktów

# price_list = {
#     'T-shirt': 19.99,
#     'Jeans': 49.99,
#     'Jacket': 89.99,
#     'Sneakers': 59.99,
#     'Hat': 15.99
# }

# total_before = 0.0  # suma cen wszystkich produktów przed obniżką

# print("Lista produktów i ich ceny przed obniżką:")
# for product, price in price_list.items():  # przeglądamy produkty i ich pierwotne ceny
#     print(f"{product}: {price:.2f}")  # wypisujemy produkt oraz cenę z dokładnością do dwóch miejsc po przecinku
#     total_before += price  # doliczamy cenę produktu do łącznej kwoty przed obniżką

# print(f"Łączna wartość produktów przed obniżką: {total_before:.2f}")

# total_after = 0.0  # suma cen wszystkich produktów po 10% obniżce

# for product, price in price_list.items():  # modyfikujemy każdy wpis w słowniku o 10% rabatu
#     discounted_price = round(price * 0.9, 2)  # obniżamy cenę o 10% i zaokrąglamy do dwóch miejsc po przecinku
#     price_list[product] = discounted_price  # zapisujemy nową cenę w słowniku price_list
#     total_after += discounted_price  # doliczamy nową cenę do łącznej wartości po obniżce

# print("Lista produktów i ich ceny po 10% obniżce:")
# for product, price in price_list.items():  # wypisujemy zaktualizowany cennik ze słownika
#     print(f"{product}: {price:.2f}")

# print(f"Łączna wartość produktów po obniżce: {total_after:.2f}")