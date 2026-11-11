# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# W języku Python instrukcja elif (skrót od „else if”) służy w instrukcjach warunkowych do sprawdzania dodatkowych warunków, jeśli poprzedni warunek if lub elif był fałszywy.
# Pozwala ona na wykonanie różnych bloków kodu w zależności od tego, który warunek jest prawdziwy. 
# Używanie elif pomaga unikać zagnieżdżania wielu instrukcji if, dzięki czemu kod staje się bardziej czytelny i łatwiejszy w zarządzaniu.

# Podstawowa składnia wygląda następująco:
# if condition1:
#     # kod do wykonania, jeśli condition1 jest prawdziwy
# elif condition2:
#     # kod do wykonania, jeśli condition1 jest fałszywy, a condition2 prawdziwy
# elif condition3:
#     # kod do wykonania, jeśli condition2 jest fałszywy, a condition3 prawdziwy
# else:
#     # kod do wykonania, jeśli wszystkie powyższe warunki są fałszywe

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Rozmiary odzieży są często oznaczane symbolami literowymi. Napisz program, który zachęca użytkownika do podania rozmiaru odzieży.

# size = input('Enter size symbol: ')

# if size == 'S':
#     print('S: Small size')
# elif size == 'M':
#     print('M: Medium size')
# elif size == 'L':
#     print('L: Large size')
# elif size == 'XL':
#     print('XL: Extra large size')
# else:
#     print('Incorrect symbol')

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Samochód posiada trzy tryby jazdy: Auto (A), Manualny (M) oraz Eco (E). W każdym z tych trzech trybów średnie zużycie paliwa w litrach na 100 km wynosi odpowiednio 7, 9 oraz 6. 
# Napisz program, który oblicza całkowite zużycie paliwa dla danego dystansu w km oraz danego trybu jazdy.

# driving_mode = input("Podaj tryb jazdy (A/M/E): ").upper()
# distance = int(input("Podaj dystans w km: "))

# if driving_mode == 'A':
#     fuel_consumption = 7  # litrów na 100 km
# elif driving_mode == 'M':
#     fuel_consumption = 9  # litrów na 100 km
# elif driving_mode == 'E':
#     fuel_consumption = 6  # litrów na 100 km
# else:
#     fuel_consumption = 0

# total_consumption = (distance / 100) * fuel_consumption # Obliczenie całkowitego zużycia paliwa

# print(f"Całkowite zużycie paliwa na dystansie {distance} km w trybie jazdy {driving_mode} wynosi {total_consumption} litrów")

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który działa jak prosty kalkulator. Program prosi użytkownika o podanie symbolu operacji matematycznej (+, -, *, /) oraz dwóch liczb. 
# Następnie program wykonuje odpowiednią operację matematyczną na podanych liczbach i zwraca wynik.
# Prosty kalkulator

# number1 = float(input("Podaj pierwszą liczbę: "))
# number2 = float(input("Podaj drugą liczbę: "))
# operator = input("Podaj operator (+, -, *, /): ")

# if operator == "+":
#     result = number1 + number2
# elif operator == "-":
#     result = number1 - number2
# elif operator == "*":
#     result = number1 * number2
# elif operator == "/":
#     if number2 != 0:
#         result = number1 / number2
#     else:
#         result = "Nie można dzielić przez zero"
# else:
#     result = "Nieznany operator"

# print(f"{number1} {operator} {number2} = {result}")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza i wypisuje kwartał roku dla podanego numeru miesiąca (1..12).

# month = int(input("Podaj numer miesiąca (1..12): "))

# if month >= 10:
#     quarter = 4
# elif month >= 7:
#     quarter = 3
# elif month >= 4:
#     quarter = 2
# elif month >= 1:
#     quarter = 1
# else:
#     quarter = 0

# if quarter > 0:
#     print(f"Month {month} is in quarter {quarter}")
# else:
#     print("Niepoprawny numer miesiąca")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który sprawdza, jaka liczba została wprowadzona z klawiatury, i wypisuje jeden z poniższych komunikatów.

# number = int(input("Enter number: "))

# if number > 0:
#     print(f"Number {number} is positive")
# elif number < 0:
#     print(f"Number {number} is negative")
# else:
#     print("Number is 0")









