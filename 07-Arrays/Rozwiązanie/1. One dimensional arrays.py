# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...
# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
#   ...
# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Wiele języków programowania udostępnia zarówno tablice, jak i listy do przechowywania kolekcji danych i zarządzania nimi. 
# Pomimo wielu podobieństw występują między nimi kluczowe różnice pod względem funkcjonalności, elastyczności oraz wydajności.

# CECHA	                        LISTY	                                        TABLICE
# Typy danych	                Mieszane	                                    Pojedynczy, ustalony typ danych
# Elastyczność	                Wysoce elastyczne	                            Mniej elastyczne
# Wydajność	                    Wolniejsze przy operacjach numerycznych	        Szybsze przy operacjach numerycznych
# Efektywność pamięciowa	    Mniej wydajne	                                Bardziej wydajne
# Wbudowane wsparcie	        Tak	                                            Wymagają array lub numpy

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Tablica zawiera wartości: 2, 3, 7, 5, 4. Napisz program, który wypisuje:

# def main():
#     arr = [2, 3, 7, 5, 4]

#     # i. tablicę
#     print("Tablica:", arr)

#     # ii. liczbę elementów
#     print("Liczba elementów:", len(arr))

#     # iii. pierwszą wartość (indeks 0)
#     print("Pierwsza wartość:", arr[0])

#     # iv. drugą wartość (indeks 1)
#     print("Druga wartość:", arr[1])

#     # v. ostatnią wartość (indeks len(arr) - 1)
#     print("Ostatnia wartość:", arr[len(arr) - 1])

#     # vi. przedostatnią wartość bez używania ujemnych indeksów (indeks len(arr) - 2)
#     print("Przedostatnia wartość:", arr[len(arr) - 2])

#     # vii. sumę pierwszej i ostatniej wartości
#     print("Suma pierwszej i ostatniej wartości:", arr[0] + arr[len(arr) - 1])

#     # viii. środkową wartość (dzielenie całkowite długości przez 2 daje indeks 2)
#     print("Środkowa wartość:", arr[len(arr) // 2])

#     # ix. wszystkie wartości tablicy oddzielone pojedynczą spacją z użyciem pętli
#     print("Wszystkie wartości:", end=" ")
#     for item in arr:
#         print(item, end=" ")
#     print()

# if __name__ == "__main__":
#     main()

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Tablica zawiera wartości: 1, 2, 3, 4, 5. Napisz program, który modyfikuje wartości tablicy. Wypisz tablicę po każdej zmianie.

# def main():
#     arr = [1, 2, 3, 4, 5]
#     print("Tablica:", arr)

#     # i. odejmujemy 1 od pierwszego elementu (indeks 0)
#     arr[0] -=  1
#     print("Tablica:", arr)

#     # ii. zwiększamy ostatni element o 4 (indeks len(arr) - 1)
#     arr[len(arr) - 1] += 4
#     print("Tablica:", arr)

#     # iii. mnożymy środkowy element przez 2 (indeks len(arr) // 2)
#     arr[len(arr) // 2] *= 2
#     print("Tablica:", arr)

# if __name__ == "__main__":
#     main()

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje nazwę dnia tygodnia dla podanego numeru dnia.

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
#     # Numery dni zaczynają się od 1, natomiast indeksy listy w Pythonie od 0, więc odjmujemy 1
#     return weekdays[n - 1]

# def main():
#     print("Dzień tygodnia dla numeru 1:", weekday(1))
#     print("Dzień tygodnia dla numeru 4:", weekday(4))
#     print("Dzień tygodnia dla numeru 7:", weekday(7))

# if __name__ == "__main__":
#     main()

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje listę zakupów, każdy produkt w osobnym wierszu.

# shopping_list = [
#     "milk",
#     "bread",
#     "eggs",
#     "butter",
#     "cheese",
#     "tomatoes",
#     "potatoes",
#     "carrots",
#     "onions",
#     "garlic",
#     ]

# for item in shopping_list:
#     print(item)

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje popularne gry komputerowe, każdą nazwę gry w osobnym wierszu. Użyj instrukcji while. 
# Dodatkowo ponumeruj listę (wypisz kolejny numer przed każdym elementem listy) i posortuj listę alfabetycznie (użyj jednej z wbudowanych funkcji Pythona do sortowania).

# computer_games = [
#     "Minecraft",
#     "Fortnite",
#     "Cyberpunk 2077",
#     "The Witcher 3",
#     "League of Legends",
#     "Valorant",
#     "Grand Theft Auto V",
#     "Elden Ring",
#     "Apex Legends",
#     "Call of Duty: Warzone",
# ]

# # Sortujemy listę alfabetycznie za pomocą wbudowanej funkcji sorted()
# sorted_games = sorted(computer_games)

# print("Posortowana lista gier:")
# i = 0
# while i < len(sorted_games):
#     print(f"{i + 1}. {sorted_games[i]}")
#     i += 1

# ZADANIE 9________________________________________________________________________________________________________________________________________________________________________
# Lista zawiera numery rejestracyjne pojazdów w Polsce. Samochody z Krakowa mają numery zaczynające się od liter 'KR' lub 'KK'. 
# Napisz program, który wypisuje numery rejestracyjne samochodów z Krakowa. Ponumeruj wypisywaną listę.

# polish_license_plates = [
#     'KR5233F',
#     'PO6987E',
#     'KR16179',
#     'BI7192L',
#     'KK12255',
#     'WA7930T',
#     'SK6922I',
#     'KK61108',
#     'KR90538',
#     'BI8052Q',
#     'KK54985',
#     'LU4864U',
# ]

# print("Numery rejestracyjne z Krakowa:")
# counter = 1
# for car_number in polish_license_plates:
#     if car_number[0:2] == 'KR' or car_number[0:2] == 'KK':
#         print(counter, car_number)
#         counter += 1

# ZADANIE 10________________________________________________________________________________________________________________________________________________________________________
# Tablica zawiera wyniki testu ucznia. Wartość True oznacza, że uczeń odpowiedział na pytanie poprawnie, natomiast wartość False oznacza błędną odpowiedź. 
# Napisz program, który wypisuje informacje o wynikach testu:

# test_results = [
#     False, True, False, True, True, True,
#     True, True, False, True, True, True,
#     False, True, True, True, False
# ]

# # Oblicza liczbę pytań testowych
# question_number = len(test_results)

# # Oblicza liczbę poprawnych odpowiedzi
# correct_answers = 0
# for answer in test_results:
#     if answer:
#         correct_answers += 1

# # Oblicza liczbę błędnych odpowiedzi
# incorrect_answers = question_number - correct_answers

# # Oblicza procent poprawnych odpowiedzi
# correct_percentage = (correct_answers / question_number) * 100

# print("STATYSTYKI TESTU")
# print("================")
# print("Liczba pytań:", question_number)
# print("Liczba poprawnych odpowiedzi:", correct_answers)
# print("Liczba błędnych odpowiedzi:", incorrect_answers)
# print(f"Procent poprawnych odpowiedzi: {correct_percentage:.2f}%")

# ZADANIE 11________________________________________________________________________________________________________________________________________________________________________
# Stacja pogodowa mierzy temperaturę raz dziennie. Wyniki pomiarów dla każdego dnia w marcu są przechowywane w tablicy. 
# Napisz program, który analizuje temperaturę na podstawie obserwacji z marca i wypisuje następujący raport:

# temperatures = [
#     3, 7, 1, -2, 6, -4, 5, 1, 2, 3,
#     4, -1, 0, 2, -1, -2, 5, -2, 7, 2,
#     -1, 4, 1, -4, 2, 3, 6, 7, 5, 7
# ]

# # Liczba pomiarów
# measurements = len(temperatures)

# # Oblicza średnią temperaturę w miesiącu
# temp_total = 0
# for temp in temperatures:
#     temp_total += temp
# avg_temp = temp_total / measurements

# # Oblicza minimalną i maksymalną temperaturę
# min_temp = min(temperatures)
# max_temp = max(temperatures)

# # Oblicza liczbę dni z ujemną temperaturą (poniżej 0)
# negative_temp = 0
# i = 0
# while i < len(temperatures):
#     if temperatures[i] < 0:
#         negative_temp += 1
#     i += 1

# # Wypisuje raport miesięczny po polsku
# print("RAPORT TEMPERATUR")
# print("Miesiąc: Marzec")
# print("Liczba pomiarów:", measurements)
# print(f"Średnia temperatura w miesiącu: {avg_temp:.2f}")
# print("Minimalna temperatura:", min_temp)
# print("Maksymalna temperatura:", max_temp)
# print("Liczba dni z ujemną temperaturą:", negative_temp)

# ZADANIE 12________________________________________________________________________________________________________________________________________________________________________
# Miesięczne wydatki oraz odpowiadające im kategorie wydatków znajdują się w poniższych tablicach. Napisz program, który oblicza, która kategoria wydatków była najdroższa.

# categories = ["Food", "Transport", "Rent", "Entertainment"]
# expenses = [500, 150, 1000, 200]

# max_index = 0
# for i in range(len(expenses)):
#     if expenses[i] > expenses[max_index]:
#         max_index = i

# print(
#     f"Najdroższa kategoria wydatków to {categories[max_index]} ({expenses[max_index]})."
# )

# ZADANIE 13________________________________________________________________________________________________________________________________________________________________________
# Sklep ma na stanie 10 rodzajów towarów. Ceny towarów oraz liczba sztuk towarów są podane poniżej. Napisz program, który oblicza wartość wszystkich towarów dostępnych w sklepie.

# Ceny 10 produktów w sklepie komputerowym (w jednostkach walutowych)
# product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# # Liczba dostępnych sztuk dla każdego produktu
# product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

# total_value = 0
# for i in range(len(product_prices)):
#     total_value += product_prices[i] * product_quantities[i]

# print(f"Łączna wartość wszystkich towarów w sklepie: {total_value:.2f}")

# ZADANIE 14________________________________________________________________________________________________________________________________________________________________________
# Bardzo często zachodzi potrzeba uporządkowania danych zawartych w tablicy. Uporządkowane dane pozwalają na szybsze wyszukiwanie, analizę oraz prezentację informacji. 
# Istnieje wiele algorytmów sortowania, które porządkują dane w tablicy. Jednym z najprostszych jest sortowanie bąbelkowe, które porządkuje dane w kolejności rosnącej lub malejącej.
# Sortowanie bąbelkowe to jeden z najprostszych algorytmów sortowania. 
# Działa poprzez wielokrotne przechodzenie przez listę lub tablicę, porównywanie sąsiadujących elementów i zamienianie ich miejscami, jeśli są w złej kolejności. 
# Proces ten powtarza się dopóki żadne zamiany nie są już potrzebne, co oznacza, że lista jest posortowana.

# procedure bubbleSort(arr):
#     n = length(arr)
#     for i = 0 to n-1:
#         for j = 0 to n-i-2:
#             if arr[j] > arr[j+1]:
#                swap arr[j] and arr[j+1]
#    return arr

# ZADANIE 15________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję, która sortuje tablicę liczb za pomocą algorytmu sortowania bąbelkowego. Skorzystaj z informacji zawartych we wcześniejszym pseudokodzie. 
# Następnie napisz program, który sortuje poniższe kolekcje danych:

# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#     return arr

# car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
# print("Spalanie przed sortowaniem:", car_fuel_consumption)
# sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
# print("Spalanie po sortowaniu:", sorted_car_fuel_consumption)

# bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
# print("Transakcje bankowe przed sortowaniem:", bank_transactions)
# sorted_bank_transactions = bubble_sort(bank_transactions)
# print("Transakcje bankowe po sortowaniu:", sorted_bank_transactions)

# ZADANIE 16________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który używa funkcji wbudowanej do posortowania poniższych danych:

# distances_traveled = [120, 150, 180, 90, 200, 175, 160]
# sorted_distances = sorted(distances_traveled)
# print("Pokonane dystanse rosnąco:", sorted_distances)

# # Sortowanie danych w kolejności malejącej, od najwyższej do najniższej wartości
# daily_temperatures = [16, 17, 15, 14, 18, 19, 17, 15, 16, 18]
# sorted_temperatures = sorted(daily_temperatures, reverse=True)
# print("Dzienne temperatury malejąco:", sorted_temperatures)

# # Sortowanie danych w kolejności rosnącej
# file_names = [
#     "report.docx",
#     "presentation.pptx",
#     "data.csv",
#     "photo.jpg",
#     "notes.txt",
#     "invoice.pdf",
#     "resume.docx",
#     "budget.xlsx",
#     "meeting.mp4",
#     "schedule.pdf",
# ]
# sorted_files = sorted(file_names)
# print("Nazwy plików rosnąco:", sorted_files)