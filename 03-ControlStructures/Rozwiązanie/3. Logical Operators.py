# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Możesz łączyć warunki za pomocą operatorów logicznych takich jak:
#   - and: Wszystkie warunki muszą być prawdziwe.
#   - or: Przynajmniej jeden warunek musi być prawdziwy.
#   - not: Odwraca wartość logiczną warunku.

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który sprawdza, czy wprowadzony login i hasło są poprawne.

# login = 'joe'
# password = 'abcd'

# entered_login = input('Login: ')
# entered_password = input('Password: ')

# if login == entered_login and password == entered_password:
#     print('Zostałeś zalogowany')
# else:
#     print('Niepoprawny login lub hasło!!')

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Zniżka przysługuje dzieciom poniżej 18 roku życia lub osobom w wieku 65 lat i starszym. 
# Napisz program, który sprawdza, czy osoba w danym wieku kwalifikuje się do zniżki.

# age = int(input("Podaj swój wiek: "))

# if age < 18 or age >= 65:
#     print("Zniżka przysługuje")
# else:
#     print("Brak zniżki")

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Użytkownik wprowadza z klawiatury dwie liczby całkowite. Napisz program, który sprawdza, czy co najmniej jedna z nich nie jest ujemna.

# x = int(input("Podaj pierwszą liczbę: "))
# y = int(input("Podaj drugą liczbę: "))

# if not x < 0 or not y < 0:
#     print(f"Przynajmniej jedna z liczb {x} i {y} nie jest ujemna")
# else:
#     print(f"Obie liczby ({x} i {y}) są ujemne")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza i wypisuje liczbę dni w danym miesiącu (1..12). Przyjmij, że luty zawsze ma 28 dni.

# month = int(input("Podaj numer miesiąca (1..12): "))

# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     days = 31 
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     days = 30 
# elif month == 2:
#     days = 28
# else:
#     days = 0

# if days > 0:
#     print(f"Miesiąc {month} ma {days} dni")
# else:
#     print("Niepoprawny numer miesiąca")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który sprawdza, czy podany numer dnia miesiąca jest poprawny.

# month = int(input("Podaj numer miesiąca (1..12): "))
# day = int(input("Podaj numer dnia w miesiącu: "))
# day_ok = False

# if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
#     if day >= 1 and day <= 31:
#         day_ok = True
# elif month == 4 or month == 6 or month == 9 or month == 11:
#     if day >= 1 and day <= 30:
#         day_ok = True
# elif month == 2:
#     if day >= 1 and day <= 28:
#         day_ok = True

# message = f"Dzień {day} dla miesiąca {month}"

# if day_ok:
#     print(f"{message} jest poprawny")
# else:
#     print(f"{message} jest niepoprawny")