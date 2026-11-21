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

# def sum_digits(number):
    
#     number = abs(number)    # Usuwamy znak minusa, aby nie traktować '-' jako znaku do zamiany na int
#     text = str(number)  # Zamieniamy liczbę na tekst, aby móc przechodzić po pojedynczych cyfrach
#     total = 0    # Zmienna przechowująca bieżącą sumę cyfr

#     for char in text:
#         total += int(char)  # Każdy znak zamieniamy na liczbę całkowitą i dodajemy do sumy
#     return total    # Zwracamy obliczoną sumę

# any_number = int(input("Podaj liczbę całkowitą: "))  # Wczytanie liczby całkowitej z klawiatury
# result = sum_digits(any_number)     # Wywołanie funkcji i zapisanie wyniku

# print(f"Suma cyfr w liczbie {any_number} wynosi {result}")


# matematycznie bez zamiany na tekst
# def sum_digits_math(number):

#     number = abs(number)
#     total = 0

#     while number > 0:
        
#         last_digit = number % 10        # Reszta z dzielenia przez 10 wyciąga ostatnią cyfrę liczby
#         total += last_digit     # Dodajemy ostatnią cyfrę do sumy
#         number //= 10       # Dzielenie całkowite przez 10 odrzuca ostatnią cyfrę liczby

#     return total

# user_number = int(input("Podaj liczbę całkowitą: "))        # Wczytanie liczby od użytkownika
# result = sum_digits_math(user_number)       # Wywołanie funkcji matematycznej
# print(f"Suma cyfr w liczbie {user_number} wynosi {result}")     # Wypisanie wyniku

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję, która oblicza ocenę końcową z testu na podstawie liczby zdobytych punktów, zgodnie z zasadami:

# def pts_to_grade(points):   # Zmienna przechowująca tekstową nazwę oceny
    
#     grade = ""
#     if points >= 18:
#         grade = "Excellent"
#     elif points >= 14:
#         grade = "Good"
#     elif points >= 10:
#         grade = "Satisfactory"
#     else:
#         grade = "Fail"

#     return grade

# test_result = 15
# final_grade = pts_to_grade(test_result)
# print(f"Zdobyłeś {test_result} punktów na teście. Twoja ocena końcowa to {final_grade}.")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję, która zwraca pełną nazwę dnia tygodnia na podstawie jego numeru.

# def day_name(day_number):

#     result = ""    # Zmienna przechowująca nazwę dnia tygodnia

#     if day_number == 1:
#         result = "Monday"
#     elif day_number == 2:
#         result = "Tuesday"
#     elif day_number == 3:
#         result = "Wednesday"
#     elif day_number == 4:
#         result = "Thursday"
#     elif day_number == 5:
#         result = "Friday"
#     elif day_number == 6:
#         result = "Saturday"
#     elif day_number == 7:
#         result = "Sunday"
#     else:
#         result = "Unknown day"  # Komunikat na wypadek podania numeru spoza zakresu 1-7

#     return result

# print("Nazwa 5. dnia tygodnia to:", day_name(5))
# print("Nazwa 3. dnia tygodnia to:", day_name(3))
# print("Nazwa 7. dnia tygodnia to:", day_name(7))


# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Alfabet fonetyczny ICAO (Międzynarodowej Organizacji Lotnictwa Cywilnego) jest używany na całym świecie do literowania liter w łączności radiowej. 
# Program icao.py zawiera funkcję, która zwraca odpowiadające słowo dla podanej litery. Uzupełnij program tak, aby przeliterował imię wprowadzone z klawiatury.

# def icao(letter):
#     letter = letter.capitalize()
#     if letter == 'A':
#         icao_name = 'Alfa'
#     elif letter == 'B':
#         icao_name = 'Bravo'
#     elif letter == 'C':
#         icao_name = 'Charlie'
#     elif letter == 'D':
#         icao_name = 'Delta'
#     elif letter == 'E':
#         icao_name = 'Echo'
#     elif letter == 'F':
#         icao_name = 'Foxtrot'
#     elif letter == 'G':
#         icao_name = 'Golf'
#     elif letter == 'H':
#         icao_name = 'Hotel'
#     elif letter == 'I':
#         icao_name = 'India'
#     elif letter == 'J':
#         icao_name = 'Juliett'
#     elif letter == 'K':
#         icao_name = 'Kilo'
#     elif letter == 'L':
#         icao_name = 'Lima'
#     elif letter == 'M':
#         icao_name = 'Mike'
#     elif letter == 'N':
#         icao_name = 'November'
#     elif letter == 'O':
#         icao_name = 'Oscar'
#     elif letter == 'P':
#         icao_name = 'Papa'
#     elif letter == 'Q':
#         icao_name = 'Quebec'
#     elif letter == 'R':
#         icao_name = 'Romeo'
#     elif letter == 'S':
#         icao_name = 'Sierra'
#     elif letter == 'T':
#         icao_name = 'Tango'
#     elif letter == 'U':
#         icao_name = 'Uniform'
#     elif letter == 'V':
#         icao_name = 'Victor'
#     elif letter == 'W':
#         icao_name = 'Whiskey'
#     elif letter == 'X':
#         icao_name = 'X-ray'
#     elif letter == 'Y':
#         icao_name = 'Yankee'
#     elif letter == 'Z':
#         icao_name = 'Zulu'
#     else:
#         icao_name = '???'

#     return icao_name

# name = input('Podaj swoje imię: ')
# print('Słowa ICAO do przeliterowania Twojego imienia:')

# for char in name:
#     word = icao(char)
#     print(word, end=" ")

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję time_string(hours, minutes, time_format), która dla podanej liczby godzin (0..23) oraz liczby minut (0..59) zwraca napis określający czas 
# w podanym formacie ('24' dla formatu 24-godzinnego oraz '12' dla formatu 12-godzinnego).

# def time_string(hours, minutes, time_format):   # Minuty w obu formatach zawsze mają dwa znaki (np. '03', '05', '15') 
#     formatted_minutes = f"{minutes:02d}"    # oznacza liczbę całkowitą formatowaną na co najmniej dwa znaki z dopisanym zerem z przodu, jeśli minuty są jednocyfrowe 
#                                             # – dzięki temu na przykład 3 zamienia się w '03'.
 
#     if time_format == "24": # W formacie 24-godzinnym godziny również uzupełniamy zerem wiodącym do dwóch cyfr
#         return f"{hours:02d}:{formatted_minutes}"

#     elif time_format == "12": # Określamy końcówkę 'am' (przed południem) lub 'pm' (od południa)
#         if hours < 12:
#             period = "am" 
#         else: 
#             period = "pm" 

#         # Przeliczamy godzinę z zakresu 0..23 na zapis 12-godzinny (1..12)
#         if hours == 0:
#             hour_12 = 12
#         elif hours > 12:
#             hour_12 = hours - 12
#         else:
#             hour_12 = hours

#         # W formacie 12-godzinnym z przykładów godziny nie mają zera wiodącego (np. '7:30am')
#         return f"{hour_12}:{formatted_minutes}{period}"

#     else:
#         return "Nieprawidłowy format"

# print(time_string(15, 38, "24"))
# print(time_string(8, 3, "24"))  # liczb całkowitych nie poprzedza się zerem – dlatego w kodzie przekazujemy 3, a nie 03 (SyntaxError)
# print(time_string(0, 5, "24"))
# print(time_string(11, 15, "12"))
# print(time_string(0, 7, "12"))
# print(time_string(7, 30, "12"))
# print(time_string(12, 46, "12"))
# print(time_string(13, 10, "12"))
# print(time_string(19, 2, "12"))