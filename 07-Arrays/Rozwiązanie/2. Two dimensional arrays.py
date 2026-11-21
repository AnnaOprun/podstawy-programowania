# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...
# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Kółko i krzyżyk to prosta, a jednocześnie dająca dużo frajdy gra dla dwóch graczy. Gra się na siatce dziewięciu pól ułożonych w trzech wierszach i trzech kolumnach.
# Poniższa tablica przedstawia planszę do gry w kółko i krzyżyk. Napisz program, który wypisuje planszę na ekranie.

# print("Plansza do gry w kółko i krzyżyk:")

# # Plansza do gry w kółko i krzyżyk 3x3
# tic_tac_toe_board = [
#     ['x', 'o', 'x'],
#     [' ', 'x', 'o'],
#     ['o', ' ', 'x']
# ]

# for row in tic_tac_toe_board:
#     for cell in row:
#         print(cell, end=" ")
#     print()

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Poniższe dane przedstawiają miesięczne wydatki podzielone na kategorie oraz tygodnie. Napisz program, który oblicza i wypisuje:

# Tygodniowe wydatki dla różnych kategorii [Food, Transport, Utilities]
# monthly_expenses = [
#     [200, 50, 100],  # Tydzień 1
#     [180, 60, 110],  # Tydzień 2
#     [220, 55, 105],  # Tydzień 3
#     [210, 65, 95]    # Tydzień 4
# ]

# # Łączne wydatki dla każdej kategorii (indeksy kolumn: 0 - Food, 1 - Transport, 2 - Utilities)
# food_total = 0
# transport_total = 0
# utilities_total = 0

# for week in monthly_expenses:
#     food_total += week[0]
#     transport_total += week[1]
#     utilities_total += week[2]

# # Łączne wydatki dla każdego tygodnia (sumy poszczególnych wierszy)
# week_totals = []
# for week in monthly_expenses:
#     week_sum = 0
#     for amount in week:
#         week_sum += amount
#     week_totals.append(week_sum)

# # Łączne wydatki za cały miesiąc
# month_total = 0
# for week_sum in week_totals:
#     month_total += week_sum

# print("WYDATKI MIESIĘCZNE")
# print("------------------")
# print("Jedzenie:", food_total)
# print("Transport:", transport_total)
# print("Media:", utilities_total)
# print("Tydzień 1:", week_totals[0])
# print("Tydzień 2:", week_totals[1])
# print("Tydzień 3:", week_totals[2])
# print("Tydzień 4:", week_totals[3])
# print("------------------")
# print("SUMA:", month_total)

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Poniższe dane zawierają tygodniowy plan posiłków. Napisz program, który wypisuje tygodniowy plan posiłków wraz z nazwą dnia tak jak w poniższym przykładzie.

# Tygodniowy plan posiłków [Breakfast, Lunch, Dinner] dla 7 dni
# meal_plan = [
#     ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
#     ["Pancakes", "Sandwich", "Steak"],
#     ["Smoothie", "Chicken Wrap", "Salmon"],
#     ["Eggs", "Pasta", "Soup"],
#     ["Toast", "Burrito", "Pizza"],
#     ["Cereal", "Salad", "Fish Tacos"],
#     ["Bagel", "Rice and Beans", "Stir-fry"],
# ]

# # Zwraca nazwę dnia tygodnia
# def weekday(n):
#     weekdays = [
#         "Monday",
#         "Tuesday",
#         "Wednesday",
#         "Thursday",
#         "Friday",
#         "Saturday",
#         "Sunday",
#     ]
#     return weekdays[n - 1]

# # Zwraca napis z nazwami posiłków z danego dnia oddzielonymi przecinkiem
# def day_meal_plan(meal_plan, day_number):
#     meals = meal_plan[day_number - 1]
#     return ", ".join(meals)

# print("TYGODNIOWY PLAN POSIŁKÓW")
# print("(Śniadanie, Obiad, Kolacja)")
# print("===========================")

# for day in range(1, len(meal_plan) + 1):
#     print(f"{weekday(day)}: {day_meal_plan(meal_plan, day)}")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Poniższe dane przedstawiają rozmieszczenie miejsc w kinie. Napisz program, który:
#               oblicza, ile miejsc jest dostępnych
#               oblicza, ile miejsc jest zarezerwowanych
#               informuje, jaki jest status miejsca w podanym rzędzie i podanym miejscu (dostępne lub zarezerwowane)

# Rozmieszczenie miejsc na sali kinowej w układzie 5x5
# 'A' oznacza miejsce dostępne, a 'B' oznacza miejsce zarezerwowane

# cinema_seats = [
#     ['A', 'A', 'B', 'A', 'A'],  
#     ['A', 'B', 'B', 'A', 'A'],  
#     ['A', 'A', 'A', 'A', 'B'], 
#     ['B', 'A', 'A', 'A', 'A'],  
#     ['A', 'B', 'A', 'A', 'A']   
# ]

# # Funkcja zwracająca łączną liczbę wszystkich miejsc w tablicy dwuwymiarowej
# def seats_total(seats):
#     total = 0  
#     for row in seats:  # przechodzimy przez każdy wiersz (rząd)
#         total += len(row)  # dodajemy liczbę miejsc w bieżącym rzędzie
#     return total  

# # Funkcja zliczająca wszystkie miejsca dostępne ('A')
# def seats_available(seats):
#     available = 0  
#     for row in seats:  # przechodzimy przez każdy rząd
#         for seat in row:  # sprawdzamy każde miejsce w danym rzędzie
#             if seat == 'A': 
#                 available += 1  
#     return available  

# # Funkcja zliczająca wszystkie miejsca zarezerwowane ('B')
# def seats_booked(seats):
#     booked = 0  
#     for row in seats:  # przechodzimy przez każdy rząd
#         for seat in row:  # sprawdzamy każde miejsce w danym rzędzie
#             if seat == 'B':  
#                 booked += 1  
#     return booked 

# # Funkcja sprawdzająca status konkretnego miejsca (numery rzędu i miejsca liczone od 1)
# def seat_status(seats, row, place):
#     # Odejmujemy 1 od row i place, ponieważ indeksy list w Pythonie zaczynają się od 0
#     if seats[row - 1][place - 1] == 'A':
#         return "dostępne" 
#     return "zarezerwowane" 

# print("TABELA INFORMACYJNA KINA")
# print("Liczba miejsc ogółem:", seats_total(cinema_seats))
# print("Liczba dostępnych miejsc:", seats_available(cinema_seats))
# print("Liczba zarezerwowanych miejsc:", seats_booked(cinema_seats))
# print("Miejsce w rzędzie 1, miejsce 1:", seat_status(cinema_seats, 1, 1))
# print("Miejsce w rzędzie 5, miejsce 5:", seat_status(cinema_seats, 5, 5))
# print("Miejsce w rzędzie 3, miejsce 5:", seat_status(cinema_seats, 3, 5))

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Poniższa tablica reprezentuje macierz kwadratową i zawiera wartości:
# [0, 0, 0],
# [0, 0, 0],
# [0, 0, 0],

# Utwórz program, który zastępuje wartości na głównej przekątnej jedynkami (`1`). Użyj instrukcji pętli. Wypisz zmodyfikowaną tablicę.
# 1 0 0
# 0 1 0
# 0 0 1

# matrix = [
#     [0, 0, 0],  
#     [0, 0, 0],  
#     [0, 0, 0],  
# ]

# # Na głównej przekątnej indeks wiersza i indeks kolumny są równe (0-0, 1-1, 2-2)
# for i in range(len(matrix)):
#     matrix[i][i] = 1

# print("Macierz z jedynkami na głównej przekątnej:")
# for row in matrix:
#     for value in row:
#         print(value, end=" ")
#     print()