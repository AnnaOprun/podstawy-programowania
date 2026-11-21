# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...
# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Spróbuj utworzyć poniższe tablice. Następnie wypisz zawartość utworzonych tablic

# import random

# arr1 = [3, 7, 1, 0, 4]
# arr2 = [[2, 3], [7, 1], [0, 4]]
# arr3 = [7 for i in range(5)]
# arr4 = [i for i in range(1, 10)]
# arr5 = [i * 2 for i in range(1, 10)]
# arr6 = [random.randint(1, 20) for i in range(10)]
# arr7 = [[] for i in range(5)]
# arr8 = [[1 for i in range(2)] for j in range(4)]
# arr9 = [[random.randint(1, 20) for i in range(3)] for j in range(5)]

# # Tablica o wartościach: 4, 0, 3
# arr_values = [4, 0, 3]

# # Tablica 15-elementowa wypełniona zerami
# arr_zeros = [0 for i in range(15)]

# # Tablica liczb całkowitych z przedziału <1, 30> (przykładowo 10 losowych wartości)
# arr_range_1_30 = [random.randint(1, 30) for i in range(10)]

# # Tablica 20-elementowa wypełniona losowo zerami lub jedynkami
# arr_random_0_1 = [random.randint(0, 1) for i in range(20)]

# # Tablica dwuwymiarowa o pięciu wierszach i dwóch kolumnach wypełniona False
# arr_2d_false = [[False for j in range(2)] for i in range(5)]

# print("arr1:", arr1)
# print("arr2:", arr2)
# print("arr3:", arr3)
# print("arr4:", arr4)
# print("arr5:", arr5)
# print("arr6:", arr6)
# print("arr7:", arr7)
# print("arr8:", arr8)
# print("arr9:", arr9)
# print("Tablica o wartościach 4, 0, 3:", arr_values)
# print("Tablica 15 zer:", arr_zeros)
# print("Tablica wartości całkowitych z <1, 30>:", arr_range_1_30)
# print("Tablica 20 losowych 0 lub 1:", arr_random_0_1)
# print("Tablica 2D (5 wierszy, 2 kolumny) z False:", arr_2d_false)

# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Tablica zawiera liczby całkowite: 34, 7, 19, 4, 21, 8. Utwórz program, który oblicza i wypisuje liczbę wartości parzystych w tablicy. Użyj instrukcji pętli while.

# numbers = [34, 7, 19, 4, 21, 8] 

# even_count = 0  # licznik liczb parzystych
# index = 0  # bieżący indeks w tablicy

# # Przechodzimy przez wszystkie elementy tablicy za pomocą pętli while
# while index < len(numbers):
#     # Liczba jest parzysta, gdy reszta z dzielenia przez 2 wynosi 0
#     if numbers[index] % 2 == 0:
#         even_count += 1  # zwiększamy licznik liczb parzystych
#     index += 1  # przechodzimy do kolejnego elementu tablicy

# print("Liczba wartości parzystych w tablicy:", even_count)

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Tablica zawiera liczby naturalne: 15, 8, 31, 47, 2, 19. Utwórz program, który wypisuje zawartość tablicy w odwrotnej kolejności. Użyj dowolnej instrukcji pętli.

# numbers = [15, 8, 31, 47, 2, 19]

# print("Istniejąca tablica:", end=" ")
# for number in numbers:
#     print(number, end=" ")
# print()

# print("Odwrócona tablica:", end=" ")
# for i in range(len(numbers) - 1, -1, -1):
#     print(numbers[i], end=" ")
# print()

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Utwórz program, który oblicza drugą potęgę każdego elementu tablicy.

# numbers = [8, 2, 5, 1, 9] 

# # Obliczamy drugą potęgę każdego elementu tablicy
# second_powers = [number ** 2 for number in numbers]

# # Wypisujemy oryginalną tablicę oraz jej elementy podniesione do drugiej potęgi
# print("Tablica:", end=" ")
# for number in numbers:
#     print(number, end=" ")
# print()

# print("2. potęga:", end=" ")
# for power in second_powers:
#     print(power, end=" ")
# print()

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Tablica zawiera liczby: -15, 8, -31, 47, -2, 19. Utwórz program, który znajduje i wypisuje największą oraz najmniejszą liczbę. Nie używaj dostępnych funkcji.

# numbers = [-15, 8, -31, 47, -2, 19]  # tablica liczb wejściowych

# # Przyjmujemy pierwszy element jako początkowe minimum i maksimum
# min_number = numbers[0]
# max_number = numbers[0]

# # Przechodzimy przez kolejne elementy tablicy i aktualizujemy wartości skrajne
# for number in numbers:
#     if number < min_number:
#         min_number = number
#     if number > max_number:
#         max_number = number

# print("Najmniejsza liczba w tablicy:", min_number)
# print("Największa liczba w tablicy:", max_number)

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Tablica zawiera wartości: 15, 8, 31, 47, 2, 19. Utwórz program, który oblicza i wypisuje tablicę oraz średnią arytmetyczną wartości z tablicy. Użyj instrukcji pętli „for”.

# numbers = [15, 8, 31, 47, 2, 19] 

# total = 0  # suma wszystkich elementów w tablicy
# for number in numbers:  # przechodzimy przez każdy element tablicy pętlą for
#     total += number  # dodajemy bieżącą wartość do sumy

# mean = total / len(numbers)  # średnia arytmetyczna jako suma podzielona przez liczbę elementów

# print("Tablica:", numbers)
# print(f"Średnia arytmetyczna: {mean:.2f}")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Tablica zawiera wartości: 15, 8, 31, 47, 2, 19. Utwórz program, który oblicza i wypisuje tablicę oraz średnią arytmetyczną wartości z tablicy. Użyj instrukcji pętli „while”.

# numbers = [15, 8, 31, 47, 2, 19]

# total = 0  # suma wszystkich elementów w tablicy
# index = 0  # bieżący indeks elementu w tablicy

# # Sumujemy wszystkie elementy tablicy za pomocą pętli while
# while index < len(numbers):
#     total += numbers[index]  # dodajemy element pod bieżącym indeksem do sumy
#     index += 1  # przesuwamy indeks na kolejny element

# mean = total / len(numbers)  # obliczamy średnią arytmetyczną

# print("Tablica:", numbers)
# print(f"Średnia arytmetyczna: {mean:.2f}")

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Utwórz program, który wypisuje najdłuższe imię (składające się z największej liczby znaków).

# names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]  

# longest_name = names[0]  # przyjmujemy pierwsze imię jako punkt odniesienia

# # Porównujemy długość kolejnych imion z dotychczas najdłuższym imieniem
# for name in names:
#     if len(name) > len(longest_name):
#         longest_name = name

# print("Imiona:", end=" ")
# for name in names:
#     print(name, end=" ")
# print()

# print("Najdłuższe imię:", longest_name)

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Tablica zawiera liczby całkowite: 2, 6, 4, 9, 7. Utwórz program, który wypisuje wartości z tablicy w postaci graficznej tak jak poniżej. 
# Zdefiniuj funkcję star(n), która zwraca podaną liczbę gwiazdek jako napis (string). Użyj zdefiniowanej funkcji w programie.


# def star(n):      # Funkcja zwracająca napis złożony z n gwiazdek
#     return "*" * n

# numbers = [2, 6, 4, 9, 7]  # tablica liczb całkowitych z zadania

# print("Graficzne przedstawienie wartości z tablicy:")
# for number in numbers:
#     print(f"{number}: {star(number)}")

# ZADANIE 9________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję compare(array1, array2), która zwraca True, jeśli obie tablice są takie same, lub False w przeciwnym razie. 
# Dwie tablice są takie same, jeśli mają tę samą liczbę elementów oraz wartości elementów w komórkach tablic o tym samym indeksie są równe.

# def compare(array1, array2):
#     if len(array1) != len(array2):  # jeśli liczby elementów się różnią, tablice nie mogą być takie same
#         return False
#     for i in range(len(array1)):  # sprawdzamy po kolei każdy indeks od 0 do len(array1) - 1
#         if array1[i] != array2[i]:  # jeśli choć jedna para elementów na tym samym indeksie jest różna
#             return False
#     return True  # wszystkie długości i elementy na odpowiadających pozycjach są zgodne


# # Lista par tablic do porównania zgodnie z treścią zadania
# pairs = [
#     (["water", "book", "sky"], ["water", "book", "sky"]),
#     ([True, False], [True, False, True]),
#     ([5, 3, 1], [5, 3, 1]),
#     ([3, 2, 1], [3, 2]),
# ]

# # Przechodzimy przez każdą parę tablic, wypisujemy je i drukujemy wynik porównania
# for arr1, arr2 in pairs:
#     print("Tablica1:", end=" ")  # etykieta dla pierwszej tablicy w jednej linii
#     for item in arr1:  # wypisujemy kolejne elementy pierwszej tablicy oddzielone spacją
#         print(item, end=" ")
#     print()  # przechodzimy do nowego wiersza po wypisaniu całej pierwszej tablicy

#     print("Tablica2:", end=" ")  # etykieta dla drugiej tablicy w jednej linii
#     for item in arr2:  # wypisujemy kolejne elementy drugiej tablicy oddzielone spacją
#         print(item, end=" ")
#     print()  # przechodzimy do nowego wiersza po wypisaniu całej drugiej tablicy

#     # Wywołujemy funkcję compare() i wypisujemy czytelny komunikat w języku polskim
#     if compare(arr1, arr2):
#         print("Porównanie: tablice są takie same")
#     else:
#         print("Porównanie: tablice są różne")
#     print()  # pusta linia oddzielająca kolejne pary wyników

# ZADANIE 10________________________________________________________________________________________________________________________________________________________________________
# Dwie tablice zawierają następujące liczby całkowite [4,36,12,28,9,44,5] oraz [5,1,36]. 
# Utwórz program, który wypisuje liczby z pierwszej tablicy, które nie występują w drugiej tablicy.

# first_array = [4, 36, 12, 28, 9, 44, 5]  # pierwsza tablica liczb całkowitych
# second_array = [5, 1, 36]  # druga tablica liczb całkowitych

# # Zbieramy elementy z pierwszej tablicy, których nie ma w drugiej tablicy
# unique_numbers = []
# for number in first_array:
#     if number not in second_array:  # sprawdzamy, czy bieżąca liczba nie występuje w drugiej tablicy
#         unique_numbers.append(number)  # dopisujemy liczbę do listy wynikowej

# print("Liczby z pierwszej tablicy niewystępujące w drugiej tablicy:", unique_numbers)

# ZADANIE 11________________________________________________________________________________________________________________________________________________________________________
# Utwórz program, który sortuje elementy tablicy zawierającej liczby całkowite. Zastosuj algorytm sortowania bąbelkowego. 
# Zdefiniuj funkcję bubblesort(array), która zwraca posortowaną tablicę. Spróbuj posortować i wypisać dowolne trzy tablice.

# def bubblesort(array):
#     n = len(array)  # liczba elementów w tablicy
#     for i in range(n):  # zewnętrzna pętla wykonująca kolejne przebiegi sortowania
#         # W każdym przebiegu ostatnie i elementów jest już na właściwym miejscu
#         for j in range(0, n - i - 1):
#             if array[j] > array[j + 1]:  # jeśli lewy element jest większy od prawego
#                 array[j], array[j + 1] = array[j + 1], array[j]  # zamieniamy je miejscami
#     return array  # zwracamy posortowaną tablicę


# first_numbers = [64, 34, 25, 12, 22, 11, 90]  # pierwsza tablica liczb całkowitych
# second_numbers = [-10, 45, 0, -3, 18, 7]  # druga tablica zawierająca też liczby ujemne
# third_numbers = [9, 3, 8, 1, 5, 2]  # trzecia tablica liczb całkowitych

# print("Pierwsza tablica przed sortowaniem:", first_numbers)
# print("Pierwsza tablica po sortowaniu:", bubblesort(first_numbers))
# print()

# print("Druga tablica przed sortowaniem:", second_numbers)
# print("Druga tablica po sortowaniu:", bubblesort(second_numbers))
# print()

# print("Trzecia tablica przed sortowaniem:", third_numbers)
# print("Trzecia tablica po sortowaniu:", bubblesort(third_numbers))

# ZADANIE 12________________________________________________________________________________________________________________________________________________________________________
# Utwórz program, który wypisuje wszystkie unikalne elementy w tablicy.

# numbers = [2, 3, 2, 5, 8, 1, 9, 8]  # tablica liczb wejściowych

# # Elementy unikalne to te, które pojawiają się w tablicy tylko jeden raz
# unique_elements = []
# for number in numbers:
#     if numbers.count(number) == 1:
#         unique_elements.append(number)

# print("Tablica:", end=" ")
# for number in numbers:
#     print(number, end=" ")
# print()

# print("Unikalne elementy:", end=" ")
# for element in unique_elements:
#     print(element, end=" ")
# print()

# ZADANIE 13________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję occurs(number, array), która zwraca True, jeśli podana liczba znajduje się w tablicy. 
# Następnie utwórz program, który sprawdza, czy liczba wprowadzona z klawiatury znajduje się w tablicy [15, 38, 7, 23, 14].

# def occurs(number, array):
#     for item in array:
#         if item == number:
#             return True
#     return False


# numbers = [15, 38, 7, 23, 14]  # tablica liczb całkowitych z zadania
# user_number = int(input("Podaj liczbę: "))  # wczytanie liczby całkowitej z klawiatury

# print("Liczba:", user_number)
# print("Tablica:", end=" ")
# for item in numbers:
#     print(item, end=" ")
# print()

# if occurs(user_number, numbers):
#     print(f"Wynik: liczba {user_number} występuje w tablicy")
# else:
#     print(f"Wynik: liczba {user_number} nie występuje w tablicy")

# ZADANIE 14________________________________________________________________________________________________________________________________________________________________________
# Krotka (tuple) w Pythonie to niemodyfikowalna, uporządkowana kolekcja elementów. 
# Krotki są podobne do list, ale w przeciwieństwie do list, gdy krotka zostanie utworzona, jej elementy nie mogą być modyfikowane, dodawane ani usuwane.
# Napisz program, który tworzy krotkę zawierającą pojedyncze słowo 'computation'. Zapisz krotkę w zmiennej. Następnie wypisz typ tej zmiennej.

# word_tuple = ("computation",)

# print("Wartość zmiennej:", word_tuple)
# print("Typ zmiennej:", type(word_tuple))

# ZADANIE 15________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje krotkę (10,20,30,40,50) w odwrotnej kolejności.

# numbers_tuple = (10, 20, 30, 40, 50)  # krotka liczb całkowitych z zadania

# # Łączymy elementy w napis oddzielony przecinkiem bez spacji, jak w przykładowym wyniku
# original_str = ",".join(str(item) for item in numbers_tuple)
# reversed_str = ",".join(str(item) for item in reversed(numbers_tuple))

# print(f"Krotka: {original_str}")
# print(f"Odwrotna kolejność: {reversed_str}")

# ZADANIE 16________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który dla krotki ("Seven", [10, 20, 30], (5, 15, 25)) wypisuje wartości:

# data = ("Seven", [10, 20, 30], (5, 15, 25))  # krotka zawierająca napis, listę oraz krotkę

# print("Pierwsza wartość:", data[0])
# print("Druga wartość:", data[1][2])

# ZADANIE 17________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który zlicza liczbę wystąpień dowolnej wartości z krotki.

# numbers_tuple = (50, 20, 40, 50, 30, 50)  # krotka liczb całkowitych z zadania
# target_value = int(input("Podaj wartość do zliczenia: "))  # szukana wartość podana przez użytkownika

# # Zliczamy wystąpienia wybranej wartości w krotce
# occurrences = 0
# for item in numbers_tuple:
#     if item == target_value:
#         occurrences += 1

# tuple_str = ",".join(str(item) for item in numbers_tuple)
# print(f"Krotka: {tuple_str}")
# print(f"Wartość: {target_value}")
# print(f"Liczba wystąpień: {occurrences}")

# ZADANIE 18________________________________________________________________________________________________________________________________________________________________________
# Utwórz moduł MyArrays zawierający funkcje do operacji na tablicy liczb:   

#                 i. Funkcja zwracająca drugi największy element w tablicy.
#                 ii. Funkcja zwracająca różnicę między największą a najmniejszą wartością w tablicy.
#                 iii. Funkcja zwracająca medianę liczb w tablicy.   

# Nie używaj funkcji wbudowanych. Mediana to wartość środkowa w uporządkowanym ciągu liczb:

#                 i. Funkcja zwracająca dwuelementową tablicę zawierającą najmniejszą i największą wartość w tablicy.
#                 ii. Funkcja zwracająca elementy tablicy jako napis (string), oddzielone znakiem minusa.

# Plik 'MyArrays.py'

# import MyArrays  # importujemy utworzony wcześniej moduł z funkcjami tablicowymi

# numbers = [7, 3, 8, 5, 2]  # tablica liczb wejściowych z zadania

# # Wypisujemy ciąg liczb rozdzielony przecinkami za pomocą funkcji tworzącej napis z minusami
# print("Liczby:", MyArrays.array_to_minus_string(numbers).replace("-", ","))
# # Wypisujemy drugi największy element wyznaczony przez moduł MyArrays
# print("Druga największa liczba:", MyArrays.second_largest(numbers))
# # Wypisujemy różnicę pomiędzy największą a najmniejszą liczbą
# print("Różnica między największą a najmniejszą wartością:", MyArrays.difference_min_max(numbers))
# # Wypisujemy medianę ciągu liczbowego
# print("Mediana:", MyArrays.median(numbers))

# min_max = MyArrays.min_max_array(numbers)  # zapisujemy dwuelementową tablicę [min, max] do zmiennej
# # Wypisujemy najmniejszą oraz największą liczbę oddzielone przecinkiem
# print(f"Najmniejsza i największa liczba: {min_max[0]},{min_max[1]}")
# # Wypisujemy wszystkie elementy tablicy połączone znakiem minusa
# print("Liczby jako napis:", MyArrays.array_to_minus_string(numbers))

# ZADANIE 19________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który dla podanej tablicy liczb rzeczywistych wypisuje liczbę elementów większych niż podana wartość wprowadzona z klawiatury.

# real_numbers = [12.5, -3.4, 8.0, 19.75, 4.2, 15.1, 0.8]  # przykładowa tablica liczb rzeczywistych
# threshold = float(input("Podaj wartość progową: "))  # wczytanie liczby rzeczywistej z klawiatury

# greater_count = 0  # licznik elementów większych od podanej wartości
# for number in real_numbers:  # przeglądamy kolejno wszystkie elementy tablicy
#     if number > threshold:  # sprawdzamy, czy bieżący element jest ściśle większy od podanej wartości
#         greater_count += 1  # zwiększamy licznik o jeden

# print("Tablica liczb rzeczywistych:", real_numbers)
# print(f"Liczba elementów większych od {threshold}: {greater_count}")

# ZADANIE 20________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który rozdziela liczby parzyste i nieparzyste z podanej tablicy liczb całkowitych. Umieść najpierw wszystkie liczby parzyste, a następnie liczby nieparzyste.

# arr = [7, 9, 2, 4, 5, 6]  # początkowa tablica liczb całkowitych

# even_numbers = []  # lista przechowująca liczby parzyste
# odd_numbers = []  # lista przechowująca liczby nieparzyste

# # Rozdzielamy elementy tablicy na parzyste i nieparzyste z zachowaniem ich kolejności
# for number in arr:
#     if number % 2 == 0:  # reszta z dzielenia przez 2 równa 0 oznacza liczbę parzystą
#         even_numbers.append(number)
#     else:  # w przeciwnym razie liczba jest nieparzysta
#         odd_numbers.append(number)

# # Łączymy listy: najpierw liczby parzyste, a potem nieparzyste
# arr = even_numbers + odd_numbers

# print("Tablica po rozdzieleniu:", arr)

# ZADANIE 21________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który sprawdza, czy pierwsza tablica jest podzbiorem drugiej tablicy (czy wszystkie elementy pierwszej tablicy występują w drugiej tablicy).

# first_array = [3, 7, 12]  # pierwsza tablica (sprawdzany podzbiór)
# second_array = [1, 3, 5, 7, 9, 12, 15]  # druga tablica (zbiór odniesienia)

# is_subset = True  # zakładamy na start, że każdy element pierwszej tablicy znajduje się w drugiej

# # Sprawdzamy kolejno każdy element pierwszej tablicy
# for element in first_array:
#     if element not in second_array:  # jeśli choć jeden element nie występuje w drugiej tablicy
#         is_subset = False  # ustawiamy flagę na False
#         break  # przerywamy pętlę, ponieważ brak już jednego elementu przesądza o wyniku

# print("Pierwsza tablica:", first_array)
# print("Druga tablica:", second_array)

# if is_subset:
#     print("Wynik: pierwsza tablica jest podzbiorem drugiej tablicy.")
# else:
#     print("Wynik: pierwsza tablica nie jest podzbiorem drugiej tablicy.")

# ZADANIE 22________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję rand_elem(array), która zwraca losowo wybrany element tablicy. Korzystając z tej funkcji, wypisz kilka losowo wybranych elementów tablicy.

# import random  # moduł pozwalający losować indeksy elementów tablicy

# # Funkcja zwracająca losowo wybrany element z podanej tablicy
# def rand_elem(array):
#     random_index = random.randint(0, len(array) - 1)  # losujemy poprawny indeks z zakresu tablicy
#     return array[random_index]  # zwracamy element znajdujący się pod wylosowanym indeksem

# fruits = ["jabłko", "banan", "gruszka", "śliwka", "truskawka", "pomarańcza"]  # przykładowa tablica

# print("Tablica:", fruits)
# print("Kilka losowo wybranych elementów:")
# for _ in range(5):  # wypisujemy pięć losowych wyborów z tablicy
#     print(rand_elem(fruits))

# ZADANIE 23________________________________________________________________________________________________________________________________________________________________________
# Utwórz moduł `MyText`, zawierający:

#    i. Funkcję zwracającą liczbę słów w tekście.
#    ii. Funkcję zwracającą uporządkowaną tablicę słów od najdłuższego do najkrótszego.
#    iii. Funkcję zwracającą alfabetycznie uporządkowaną tablicę słów.

# Następnie napisz program, wywołaj funkcje i wypisz wyniki. Przykładowy wynik

# Plik 'MyText.py'

# import MyText  # importujemy utworzony moduł MyText

# sample_text = "An apple a day keeps the doctor away"  # tekst wejściowy z zadania

# word_count = MyText.count_words(sample_text)  # wyznaczamy liczbę słów
# longest_first = MyText.words_by_length_desc(sample_text)  # pobieramy słowa od najdłuższego
# alphabetical = MyText.words_alphabetically(sample_text)  # pobieramy słowa alfabetycznie

# print("Tekst:", sample_text)
# print("Liczba słów:", word_count)
# print("Słowa od najdłuższego:", ",".join(longest_first))
# print("Słowa uporządkowane alfabetycznie:", ",".join(alphabetical))

# ZADANIE 24________________________________________________________________________________________________________________________________________________________________________
# Używając biblioteki matplotlib, narysuj linię na wykresie od pozycji (1, 3) do pozycji (8, 10).

# import matplotlib.pyplot as plt  # importujemy moduł pyplot pod wygodnym aliasem plt

# xpoints = [1, 8]  # współrzędne X punktu początkowego (1) i końcowego (8)
# ypoints = [3, 10]  # współrzędne Y punktu początkowego (3) i końcowego (10)

# plt.plot(xpoints, ypoints)  # rysujemy linię łączącą punkty (1, 3) oraz (8, 10)
# plt.title("Linia od punktu (1, 3) do punktu (8, 10)")  # polski tytuł wykresu
# plt.xlabel("Oś X")  # polska etykieta osi poziomej
# plt.ylabel("Oś Y")  # polska etykieta osi pionowej
# plt.show()  # wyświetlamy okno z narysowanym wykresem

# ZADANIE 25________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który rysuje wykres funkcji

# import matplotlib.pyplot as plt  # importujemy moduł pyplot do rysowania wykresów

# x = []  # lista wartości argumentów x
# y = []  # lista odpowiadających wartości funkcji y

# # Tworzymy wartości x w zakresie od -100 do 100 włącznie
# for n in range(-100, 101):
#     x = x + [n]  # dołączamy kolejną liczbę całkowitą n do listy x

# # Obliczamy wartości y zgodnie ze wzorem f(x) = x^2 - 3
# for n in x:
#     y = y + [n**2 - 3]  # dołączamy obliczoną wartość funkcji dla danego n do listy y

# # Rysujemy i wyświetlamy wykres funkcji
# plt.plot(x, y)  # rysujemy krzywą na podstawie par współrzędnych (x, y)
# plt.title("Wykres funkcji f(x) = x^2 - 3")  # polski tytuł wykresu
# plt.xlabel("x")  # etykieta osi poziomej
# plt.ylabel("f(x)")  # etykieta osi pionowej
# plt.show()  # otwieramy okno z wykresem

# ZADANIE 26________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który rysuje wykres funkcji ... dla wartości kąta z zakresu 0–360 stopni.

# import math  # moduł matematyczny zawierający funkcję math.sin() oraz math.radians()
# import matplotlib.pyplot as plt  # moduł pyplot do rysowania wykresów

# angles_deg = list(range(0, 361))  # kąty w stopniach od 0 do 360 włącznie
# # Funkcja math.sin() oczekuje argumentu w radianach, więc przeliczamy każdy kąt przez math.radians()
# sin_values = [math.sin(math.radians(angle)) for angle in angles_deg]

# plt.plot(angles_deg, sin_values)  # rysujemy krzywą sinusa dla podanych kątów
# plt.title("Wykres funkcji y = sin(x) dla kątów 0-360°")  # polski tytuł wykresu
# plt.xlabel("Kąt (stopnie)")  # polska etykieta osi poziomej
# plt.ylabel("sin(x)")  # polska etykieta osi pionowej
# plt.grid(True)  # włączamy siatkę pomocniczą ułatwiającą odczyt wartości
# plt.show()  # wyświetlamy okno z wykresem

# ZADANIE 27________________________________________________________________________________________________________________________________________________________________________
# Tablica dwuwymiarowa o rozmiarze 2 na 4 zawiera liczby całkowite. Utwórz program, który wypisuje wartości tablicy w wierszach i kolumnach.

# matrix = [
#     [10, 20, 30, 40],  # pierwszy wiersz (indeks 0) zawierający 4 elementy
#     [50, 60, 70, 80],  # drugi wiersz (indeks 1) zawierający 4 elementy
# ]

# print("Zawartość tablicy dwuwymiarowej (2x4):")
# for row in matrix:  # zewnętrzna pętla przechodzi przez kolejne wiersze tablicy
#     for value in row:  # wewnętrzna pętla przechodzi przez kolejne kolumny w bieżącym wierszu
#         print(value, end=" ")  # wypisujemy element w tym samym wierszu oddzielony spacją
#     print()  # po zakończeniu wypisywania całego wiersza przechodzimy do nowej linii

# ZADANIE 28________________________________________________________________________________________________________________________________________________________________________
# Tablica dwuwymiarowa zawiera następujące liczby:
# 7 3 7 9 0
# 2 9 0 1 5
# 3 8 6 4 7
# 8 7 1 1 5
# Utwórz program, który oblicza sumę wartości w ostatniej kolumnie.

# matrix = [
#     [7, 3, 7, 9, 0],
#     [2, 9, 0, 1, 5],
#     [3, 8, 6, 4, 7],
#     [8, 7, 1, 1, 5],
# ]

# last_column_sum = 0  # zmienna przechowująca sumę elementów z ostatniej kolumny

# for row in matrix:  # przechodzimy przez każdy wiersz tablicy dwuwymiarowej
#     last_column_sum += row[-1]  # indeks -1 wskazuje zawsze ostatni element (ostatnią kolumnę) wiersza

# print("Suma wartości w ostatniej kolumnie:", last_column_sum)

# ZADANIE 29________________________________________________________________________________________________________________________________________________________________________
# Funkcja create_2d_arr(x,y) tworzy i zwraca tablicę dwuwymiarową wypełnioną wartościami 0. Utwórz program oraz tę funkcję. 
# Następnie utwórz tablicę dwuwymiarową o wymiarach 3 na 5 i wypisz utworzoną tablicę.

# def create_2d_arr(x, y):
#     array_2d = []  # pusta lista, do której będziemy dokładać kolejne wiersze
#     for _ in range(x):  # powtarzamy x razy, aby utworzyć x wierszy
#         row = []  # tworzymy nowy, pusty wiersz
#         for _ in range(y):  # powtarzamy y razy, aby wypełnić wiersz y zerami
#             row.append(0)  # dodajemy wartość 0 jako kolejny element wiersza
#         array_2d.append(row)  # dołączamy gotowy wiersz do tablicy dwuwymiarowej
#     return array_2d  # zwracamy kompletną tablicę dwuwymiarową

# matrix = create_2d_arr(3, 5)  # tworzymy tablicę o wymiarach 3 wiersze na 5 kolumn

# print("Utworzona tablica dwuwymiarowa (3x5):")
# for row in matrix:  # przechodzimy przez każdy wiersz utworzonej tablicy
#     for value in row:  # przechodzimy przez każdą wartość w bieżącym wierszu
#         print(value, end=" ")  # wypisujemy element oddzielony spacją w jednej linii
#     print()  # przechodzimy do nowego wiersza po wypisaniu całej linii

# ZADANIE 30________________________________________________________________________________________________________________________________________________________________________
# Tablica zawiera wartości: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
# Utwórz program, który modyfikuje wartości tablicy, aby utworzyć tabliczkę mnożenia przedstawioną poniżej. Użyj instrukcji pętli. Wypisz tablicę.

# Początkowa tablica pięciu wierszy po pięć zer
# table = [
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]

# # Modyfikujemy elementy tablicy tak, aby powstała tabliczka mnożenia od 1 do 5
# for row_idx in range(len(table)):  # iterujemy po indeksach wierszy od 0 do 4
#     for col_idx in range(len(table[row_idx])):  # iterujemy po indeksach kolumn od 0 do 4
#         # Numer wiersza i kolumny liczymy od 1, dlatego dodajemy 1 do indeksów
#         table[row_idx][col_idx] = (row_idx + 1) * (col_idx + 1)

# print("Tabliczka mnożenia:")
# for row in table:  # przechodzimy przez każdy wiersz zmodyfikowanej tablicy
#     for value in row:  # przechodzimy przez wszystkie wartości w bieżącym wierszu
#         print(f"{value:2d}", end=" ")  # wyrównujemy liczby do szerokości dwóch znaków dla czytelności
#     print()  # przechodzimy do nowej linii po zakończeniu wiersza

# ZADANIE 31________________________________________________________________________________________________________________________________________________________________________
# Tablica zawiera liczby całkowite: [[-38, 19], [5,40],[-7,11],[29,16]]
# Utwórz program, który znajduje najmniejszą i największą wartość w tablicy oraz określa, w którym wierszu i w której kolumnie się znajdują.

# numbers = [[-38, 19], [5, 40], [-7, 11], [29, 16]]  # tablica dwuwymiarowa liczb całkowitych

# smallest_value = numbers[0][0]  # początkowo przyjmujemy pierwszy element jako najmniejszy
# smallest_row = 0  # indeks wiersza najmniejszego elementu
# smallest_col = 0  # indeks kolumny najmniejszego elementu

# largest_value = numbers[0][0]  # początkowo przyjmujemy pierwszy element jako największy
# largest_row = 0  # indeks wiersza największego elementu
# largest_col = 0  # indeks kolumny największego elementu

# # Przeglądamy wszystkie wiersze i kolumny tablicy, aby znaleźć wartości skrajne i ich indeksy
# for row_idx in range(len(numbers)):
#     for col_idx in range(len(numbers[row_idx])):
#         current = numbers[row_idx][col_idx]  # bieżąca wartość w tablicy
#         if current < smallest_value:  # sprawdzamy, czy znaleziono mniejszą wartość
#             smallest_value = current
#             smallest_row = row_idx
#             smallest_col = col_idx
#         if current > largest_value:  # sprawdzamy, czy znaleziono większą wartość
#             largest_value = current
#             largest_row = row_idx
#             largest_col = col_idx

# print(f"Najmniejsza wartość: {smallest_value}, wiersz: {smallest_row}, kolumna: {smallest_col}")
# print(f"Największa wartość: {largest_value}, wiersz: {largest_row}, kolumna: {largest_col}")

# ZADANIE 32________________________________________________________________________________________________________________________________________________________________________
# Tablica dwuwymiarowa o rozmiarze 3 na 5 zawiera liczby całkowite. Utwórz program, który zamienia miejscami pierwszy i ostatni wiersz. 
# Wypisz wartości tablicy w wierszach i kolumnach przed zmianami oraz po zmianach.

# matrix = [
#     [1, 2, 3, 4, 5],     # pierwszy wiersz (indeks 0)
#     [6, 7, 8, 9, 10],    # środkowy wiersz (indeks 1)
#     [11, 12, 13, 14, 15] # ostatni wiersz (indeks 2 lub -1)
# ]

# # Wypisujemy zawartość tablicy przed zamianą wierszy
# print("Tablica przed zmianą:")
# for row in matrix:
#     for value in row:
#         print(f"{value:2d}", end=" ")  # wyrównujemy liczby do 2 znaków w jednej linii
#     print()  # przechodzimy do nowej linii po wypisaniu każdego wiersza

# # Zamieniamy miejscami pierwszy wiersz (indeks 0) z ostatnim wierszem (indeks -1)
# matrix[0], matrix[-1] = matrix[-1], matrix[0]

# # Wypisujemy zawartość tablicy po zamianie wierszy
# print("\nTablica po zmianie:")
# for row in matrix:
#     for value in row:
#         print(f"{value:2d}", end=" ")  # wyrównujemy liczby do 2 znaków w jednej linii
#     print()  # przechodzimy do nowej linii po wypisaniu każdego wiersza

# ZADANIE 33________________________________________________________________________________________________________________________________________________________________________
# Tablica dwuwymiarowa o rozmiarze 3 na 5 zawiera liczby całkowite. Utwórz program, który zamienia miejscami pierwszą i ostatnią kolumnę. 
# Wypisz wartości tablicy w wierszach i kolumnach przed zmianami oraz po zmianach.

# matrix = [
#     [1, 2, 3, 4, 5],     # pierwszy wiersz, kolumna 0 to 1, a kolumna -1 to 5
#     [6, 7, 8, 9, 10],    # drugi wiersz, kolumna 0 to 6, a kolumna -1 to 10
#     [11, 12, 13, 14, 15] # trzeci wiersz, kolumna 0 to 11, a kolumna -1 to 15
# ]

# # Wypisujemy zawartość tablicy przed zamianą kolumn
# print("Tablica przed zmianą:")
# for row in matrix:
#     for value in row:
#         print(f"{value:2d}", end=" ")  # wyrównujemy liczby do 2 znaków w tym samym wierszu
#     print()  # przechodzimy do nowego wiersza po wypisaniu wszystkich kolumn

# # W każdym wierszu zamieniamy miejscami pierwszy element (indeks 0) z ostatnim elementem (indeks -1)
# for row in matrix:
#     row[0], row[-1] = row[-1], row[0]

# # Wypisujemy zawartość tablicy po zamianie kolumn
# print("\nTablica po zmianie:")
# for row in matrix:
#     for value in row:
#         print(f"{value:2d}", end=" ")  # wyrównujemy liczby do 2 znaków w tym samym wierszu
#     print()  # przechodzimy do nowego wiersza po wypisaniu wszystkich kolumn

# ZADANIE 34________________________________________________________________________________________________________________________________________________________________________
# W matematyce macierz to prostokątna tablica lub tabela liczb, symboli albo wyrażeń ułożonych w wierszach i kolumnach. 
# Utwórz funkcję `identity_matrix(n)`, która zwraca macierz jednostkową (tablicę dwuwymiarową) o rozmiarze `n`.

# def identity_matrix(n):
#     matrix = []  # lista wierszy macierzy jednostkowej
#     for row_idx in range(n):  # iterujemy po indeksach wierszy od 0 do n - 1
#         row = []  # tworzymy nowy wiersz
#         for col_idx in range(n):  # iterujemy po indeksach kolumn od 0 do n - 1
#             if row_idx == col_idx:  # na głównej przekątnej indeks wiersza równa się indeksowi kolumny
#                 row.append(1)  # wpisujemy jedynkę na głównej przekątnej
#             else:  # poza główną przekątną wpisujemy zera
#                 row.append(0)
#         matrix.append(row)  # dołączamy gotowy wiersz do macierzy
#     return matrix  # zwracamy utworzoną macierz jednostkową

# # Funkcja wypisująca tablicę dwuwymiarową w wierszach i kolumnach
# def print_2d_array(array):
#     for row in array:  # przechodzimy przez każdy wiersz tablicy
#         for value in row:  # przechodzimy przez kolejne wartości w wierszu
#             print(value, end=" ")  # wypisujemy element w tej samej linii oddzielony spacją
#         print()  # przechodzimy do nowej linii po zakończeniu wiersza

# # Tworzymy i wypisujemy trzy macierze jednostkowe o wymiarach 3, 5 oraz 8
# for size in [3, 5, 8]:
#     print(f"\nMacierz jednostkowa o wymiarach {size}x{size}:")
#     current_matrix = identity_matrix(size)  # generujemy macierz jednostkową danego rozmiaru
#     print_2d_array(current_matrix)  # wypisujemy macierz w wierszach i kolumnach

# ZADANIE 35________________________________________________________________________________________________________________________________________________________________________
# Utwórz funkcję transpose_matrix(m), która zwraca macierz transponowaną m. 
# Następnie utwórz program, który wypisuje macierze transponowane w wierszach i kolumnach dla poniższych macierzy:

# def transpose_matrix(m):
#     num_rows = len(m)  # liczba wierszy oryginalnej macierzy
#     num_cols = len(m[0])  # liczba kolumn oryginalnej macierzy
#     transposed = []  # lista wierszy nowej, transponowanej macierzy

#     # W macierzy transponowanej liczba wierszy odpowiada liczbie kolumn oryginału
#     for col_idx in range(num_cols):
#         new_row = []  # budujemy nowy wiersz macierzy transponowanej
#         for row_idx in range(num_rows):  # pobieramy elementy z kolejnych wierszy w danej kolumnie
#             new_row.append(m[row_idx][col_idx])
#         transposed.append(new_row)  # dodajemy gotowy wiersz do macierzy transponowanej

#     return transposed  # zwracamy macierz transponowaną


# # Funkcja pomocnicza wypisująca tablicę dwuwymiarową w wierszach i kolumnach
# def print_2d_array(array):
#     for row in array:  # przechodzimy po każdym wierszu tablicy
#         for value in row:  # przechodzimy po kolejnych wartościach w wierszu
#             print(value, end=" ")  # wypisujemy element oddzielony spacją w jednej linii
#         print()  # przechodzimy do nowej linii po zakończeniu wiersza

# matrix_i = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# matrix_ii = [
#     [1, 2, 3, 4, 5],
#     [6, 7, 8, 9, 0],
# ]

# matrix_iii = [
#     [5, 6, 7, 8],
# ]

# matrices = [matrix_i, matrix_ii, matrix_iii]  # zestaw macierzy z podpunktów i, ii, iii

# for idx, current_matrix in enumerate(matrices, start=1):
#     print(f"\nMacierz transponowana dla podpunktu {idx}:")
#     transposed_matrix = transpose_matrix(current_matrix)  # obliczamy macierz transponowaną
#     print_2d_array(transposed_matrix)  # wypisujemy macierz w wierszach i kolumnach

# ZADANIE 36________________________________________________________________________________________________________________________________________________________________________
# Utwórz funkcję, która konwertuje tablicę dwuwymiarową (2D) na tablicę jednowymiarową (1D). 
# Następnie utwórz program, który wypisuje tablicę jednowymiarową dla poniższych tablic dwuwymiarowych:

# def flatten_2d_to_1d(array_2d):
#     array_1d = []  # pusta lista, do której przeniesiemy wszystkie elementy z wierszy
#     for row in array_2d:  # przechodzimy przez każdy wiersz tablicy dwuwymiarowej
#         for value in row:  # przechodzimy przez kolejne elementy wewnątrz wiersza
#             array_1d.append(value)  # dopisujemy element do płaskiej listy jednowymiarowej
#     return array_1d  # zwracamy gotową tablicę jednowymiarową

# array_i = [
#     [2, 3],
#     [1, 5],
# ]

# array_ii = [
#     [5, 0, 3, 7, 5],
#     [9, 0, 9, 1, 2],
# ]

# array_iii = [
#     [2, 1],
#     [3, 5],
#     [7, 4],
#     [2, 6],
# ]

# arrays_2d = [array_i, array_ii, array_iii]  # zestaw tablic dwuwymiarowych z podpunktów i, ii, iii

# for idx, current_array in enumerate(arrays_2d, start=1):
#     flattened = flatten_2d_to_1d(current_array)  # konwertujemy tablicę 2D na 1D
#     print(f"Tablica jednowymiarowa dla podpunktu {idx}: {flattened}")