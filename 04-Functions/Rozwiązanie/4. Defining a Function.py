# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Funkcję definiuje się za pomocą słowa kluczowego def, po którym następuje nazwa funkcji, nawiasy oraz dwukropek. 
# Wewnątrz nawiasów możesz określić parametry, które funkcja może przyjmować. Blok kodu funkcji jest wcięty.

# def function_name(parameters):
#     # Blok kodu (ciało funkcji)
#     return result  # Opcjonalnie: Zwraca wartość

# Spójrz na poniższą funkcję, która pozwala zsumować dwie liczby. Funkcja add przyjmuje dwa parametry, a oraz b, i zwraca ich sumę. 
# Zwrócona wartość jest zapisywana w zmiennej sum_value, a następnie wypisywana.

# def add(a, b):
#     result = a + b
#     return result #bez tego wypisze 'None'

# sum_value = add(5, 3)
# print(sum_value)

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję triangle_area, która oblicza i zwraca pole trójkąta o bokach a, b i c. Użyj wzoru Herona
# Napisz program, który oblicza pole trójkąta na podstawie długości boków trójkąta wczytanych z klawiatury. Użyj zdefiniowanej funkcji. 
# Następnie oblicz pole trójkąta dla następujących wymiarów boków a, b i c

# import math
 
# def triangle_area(a, b, c): # definiuje funkcję przyjmującą trzy parametry
#     # Obliczamy połowę obwodu trójkąta (s)
#     s = (a + b + c) / 2
#     # Stosujemy wzór Herona i wyciągamy pierwiastek kwadratowy
#     area = math.sqrt(s * (s - a) * (s - b) * (s - c))
#     return area # zwraca obliczone pole z funkcji do miejsca jej wywołania, dzięki czemu możemy je łatwo wypisać albo dalej przetwarzać.

# # wczytuje długości boków z klawiatury i zamienia je na liczby zmiennoprzecinkowe, aby poprawnie działały także boki niecałkowite.
# side_a = float(input("Podaj długość boku a: "))
# side_b = float(input("Podaj długość boku b: "))
# side_c = float(input("Podaj długość boku c: "))

# user_area = triangle_area(side_a, side_b, side_c)
# print(f"Pole trójkąta o bokach {side_a}, {side_b}, {side_c} wynosi {user_area}")

# # Obliczenia dla podanych przykładowych zestawów boków
# print(f"Pole trójkąta o bokach 3, 4, 5 wynosi {triangle_area(3, 4, 5)}")
# print(f"Pole trójkąta o bokach 5, 12, 13 wynosi {triangle_area(5, 12, 13)}")
# print(f"Pole trójkąta o bokach 7, 24, 25 wynosi {triangle_area(7, 24, 25)}")

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję, która oblicza i zwraca sumę cyfr w liczbie. Następnie napisz program, który wczytuje liczbę z klawiatury i wypisuje sumę jej cyfr.   
# Kroki algorytmu sumowania cyfr w liczbie:   

# i. Pobierz od użytkownika liczbę całkowitą. Liczba może być dodatnia, ujemna lub równa zero.
# ii. Obsłuż liczby ujemne: Zamień liczbę na jej wartość bezwzględną za pomocą funkcji abs(). Ten krok sprawia, że algorytm poprawnie przetwarza liczby ujemne, ignorując znak minusa.
# iii. Zamień na napis: Zamień liczbę na ciąg znaków (string) za pomocą str(). Pozwala to na iterowanie (przechodzenie) po każdej cyfrze w liczbie.
# iv. Przejdź po cyfrach:   
#                        Przejdź w pętli po każdym znaku (cyfrze) w tekstowej reprezentacji liczby
#                        Zamień każdy znak z powrotem na liczbę całkowitą.
# v. Zsumuj cyfry: Dodawaj każdą wartość całkowitą do bieżącej sumy.
# vi. Zwróć wynik: Zwróć sumę cyfr.

def sum_digits(number):
    
    number = abs(number)    # Usuwamy znak minusa, aby nie traktować '-' jako znaku do zamiany na int
    text = str(number)  # Zamieniamy liczbę na tekst, aby móc przechodzić po pojedynczych cyfrach
    total = 0    # Zmienna przechowująca bieżącą sumę cyfr

    for char in text:
        total += int(char)  # Każdy znak zamieniamy na liczbę całkowitą i dodajemy do sumy
    return total    # Zwracamy obliczoną sumę

any_number = int(input("Podaj liczbę całkowitą: "))  # Wczytanie liczby całkowitej z klawiatury
result = sum_digits(any_number)     # Wywołanie funkcji i zapisanie wyniku

print(f"Suma cyfr w liczbie {any_number} wynosi {result}")