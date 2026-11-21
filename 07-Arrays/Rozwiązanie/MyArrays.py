# Pomocnicza funkcja sortująca kopię tablicy rosnąco algorytmem bąbelkowym
def _sort_ascending(array):
    sorted_arr = []  # tworzymy nową listę, aby nie modyfikować oryginalnej tablicy
    for item in array:  # kopiujemy kolejno wszystkie elementy z tablicy wejściowej
        sorted_arr.append(item)

    count = 0  # licznik elementów bez użycia wbudowanej funkcji len()
    for _ in sorted_arr:
        count += 1

    # Przechodzimy przez tablicę wielokrotnie, wypychając największe elementy na koniec
    for i in range(count):
        for j in range(0, count - i - 1):  # porównujemy sąsiednie pary w nieposortowanej części
            if sorted_arr[j] > sorted_arr[j + 1]:  # jeśli lewy element jest większy od prawego
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]  # zamieniamy je miejscami

    return sorted_arr  # zwracamy posortowaną rosnąco kopię tablicy


# Zwraca drugi największy element w tablicy
def second_largest(array):
    sorted_arr = _sort_ascending(array)  # sortujemy tablicę rosnąco
    count = 0  # liczymy długość tablicy własną pętlą
    for _ in sorted_arr:
        count += 1
    return sorted_arr[count - 2]  # element przedostatni to drugi największy w porządku rosnącym


# Zwraca różnicę między największą a najmniejszą wartością w tablicy
def difference_min_max(array):
    smallest_and_largest = min_max_array(array)  # pobieramy tablicę [najmniejsza, największa]
    return smallest_and_largest[1] - smallest_and_largest[0]  # odejmujemy minimum od maksimum


# Zwraca medianę liczb w tablicy (wartość środkową po uporządkowaniu)
def median(array):
    sorted_arr = _sort_ascending(array)  # porządkujemy liczby rosnąco
    count = 0  # obliczamy liczbę elementów bez len()
    for _ in sorted_arr:
        count += 1
    middle = count // 2  # wyznaczamy środkowy indeks dzieląc całkowitoliczbowo przez 2
    if count % 2 == 1:  # dla nieparzystej liczby elementów mediana to dokładnie środkowa wartość
        return sorted_arr[middle]
    # Dla parzystej liczby elementów mediana to średnia dwóch środkowych wartości
    return (sorted_arr[middle - 1] + sorted_arr[middle]) / 2


# Zwraca dwuelementową tablicę zawierającą najmniejszą i największą wartość w tablicy
def min_max_array(array):
    smallest = array[0]  # przyjmujemy pierwszy element jako początkowe minimum
    largest = array[0]  # przyjmujemy pierwszy element jako początkowe maksimum
    for item in array:  # sprawdzamy kolejne elementy tablicy
        if item < smallest:  # aktualizujemy minimum, gdy znajdziemy mniejszą wartość
            smallest = item
        if item > largest:  # aktualizujemy maksimum, gdy znajdziemy większą wartość
            largest = item
    return [smallest, largest]  # zwracamy wynik w postaci dwuelementowej listy


# Zwraca elementy tablicy jako napis oddzielony znakiem minusa
def array_to_minus_string(array):
    result = ""  # wynikowy napis
    is_first = True  # flaga informująca, czy przetwarzamy pierwszy element
    for item in array:
        if is_first:  # pierwszy element dodajemy bez poprzedzającego minusa
            result = f"{item}"
            is_first = False
        else:  # kolejne elementy dołączamy po znaku minusa
            result = f"{result}-{item}"
    return result  # zwracamy gotowy napis