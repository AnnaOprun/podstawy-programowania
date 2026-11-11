# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Instrukcje warunkowe w Pythonie służą do podejmowania decyzji na podstawie warunków logicznych. 
# Główną strukturą decyzyjną jest instrukcja if, która pozwala na wykonanie określonego bloku kodu, jeśli podany warunek jest prawdziwy

# Podstawowa składnia wygląda następująco:
# if condition:
#     # kod do wykonania, jeśli warunek jest prawdziwy
# else:
#     # kod do wykonania, jeśli warunek jest fałszywy
#     # (pamiętaj, że sekcja else jest opcjonalna)

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Ograniczenie prędkości na autostradzie w Polsce wynosi 140 km/h. 
# Poniższy program sprawdza, czy samochód przekroczył dozwoloną prędkość. Jeśli tak, wyświetlane jest ostrzeżenie.

# speed_limit = 140
# car_speed = int(input("Podaj prędkość samochodu (km/h): "))

# if car_speed > speed_limit:
#     print(f"Twoja prędkość to {car_speed} km/h")
#     print("Ostrzeżenie: przekroczono dozwoloną prędkość!!")

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Terminal płatniczy w sklepie umożliwia płatności kartą. Klient posiada środki na swoim koncie bankowym, a całkowita wartość zakupów jest podana.
# Terminal wypisuje komunikat, czy płatność może zostać zrealizada, czy też brakuje środków na koncie klienta. Napisz program, który działa jak terminal płatniczy.

# account_balance = 500
# total_payment = float(input("Podaj kwotę płatności: "))

# if total_payment <= account_balance:
#     print("Płatność zrealizowana")
# else:
#     print("Brak środków")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Test jest zaliczony, gdy liczba poprawnie wykonanych zadań wynosi co najmniej 50%. Napisz program, który sprawdza, czy test został zaliczony.

# total_tasks = 20
# tasks_ok = int(input("Podaj liczbę poprawnie wykonanych zadań: "))

# test_passed = False

# if tasks_ok >= total_tasks * 0.5:
#     test_passed = True

# if test_passed:
#     print("Gratulacje! Zdałeś test.")
# else:
#     print("Niestety, nie zdałeś testu.")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który sprawdza, czy liczba wprowadzona z klawiatury jest parzysta czy nieparzysta.

# number = int(input("Podaj liczbę: "))

# if number % 2 == 0:
#     print(f"Liczba {number} jest parzysta")
# else:
#     print(f"Liczba {number} jest nieparzysta")

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Podstawowe wynagrodzenie pracownika wynosi 5000 PLN. Pracownik może otrzymać premię stanowiącą kilka procent wynagrodzenia zasadniczego. 
# Napisz program, który oblicza wynagrodzenie pracownika, biorąc pod uwagę możliwość otrzymania premii. 
# Następnie oblicz całkowite wynagrodzenie pracownika dla następujących przypadków: Pracownik nie otrzymuje premii | Pracownik otrzymuje premię w wysokości 30%

# basic_salary = 5000
# total_salary = 0
# bonus = 0.30  # premia 30%

# is_bonus = input("Czy pracownik otrzymuje premię? (T/N): ").upper() == 'T'

# if is_bonus:
#     total_salary = basic_salary + (basic_salary * bonus)
#     bonus_included = "Tak (30%)"
# else:
#     total_salary = basic_salary
#     bonus_included = "Nie"

# print(f"Wynagrodzenie zasadnicze: {basic_salary} PLN")
# print(f"Uwzględniono premię? {bonus_included}")
# print(f"Całkowite wynagrodzenie: {total_salary} PLN")