# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Oprócz funkcji wbudowanych możesz używać wielu funkcji dostępnych w gotowych modułach. Jednym z przykładów jest moduł math.   
# Korzystając z funkcji i stałych dostępnych w module math, napisz program, który oblicza i wypisuje:

# import math # Na początku programu dołączamy moduł, aby odblokować zawarte w nim narzędzia

# # Pierwiastek kwadratowy z 7
# square_root = math.sqrt(7)   # Kropka oznacza: weź funkcję sqrt z modułu math
# print("Pierwiastek kwadratowy z 7 wynosi:", square_root)

# # Logarytm naturalny z 5 (czyli o podstawie e)
# natural_log = math.log(5)
# print("Logarytm naturalny z 5 wynosi:", natural_log)

# # Funkcja math.sin() oczekuje kąta w radianach, więc najpierw zamieniamy 90 stopni na radiany
# angle_in_radians = math.radians(90)
# sine_of_90 = math.sin(angle_in_radians)
# print("Sinus 90 stopni wynosi:", sine_of_90)

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który generuje i wypisuje losową liczbę całkowitą od 1 do 6, podobnie jak rzut kostką. Użyj jednej z funkcji z modułu random, aby wygenerować losową liczbę całkowitą w podanym zakresie.

# import random

# dice_roll = random.randint(1, 6)

# print("Wylosowana liczba na kostce:", dice_roll)