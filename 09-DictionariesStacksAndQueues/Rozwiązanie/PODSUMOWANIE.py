import csv
import json
import os
import queue

# ==============================================================================
# ŚCIĄGA Z PYTHONA: SŁOWNIKI, ZBIORY, STOS (LIFO), KOLEJKA (FIFO), JSON I CSV
# ==============================================================================


# ------------------------------------------------------------------------------
# 1. SŁOWNIKI (dict) — pary klucz: wartość
# ------------------------------------------------------------------------------
person = {
    "imie": "Anna",
    "wiek": 20,
    "kierunek": "Informatyka Stosowana"
}

person["miasto"] = "Kraków"  # dodanie nowej pary klucz-wartość lub nadpisanie istniejącej
wiek = person.get("wiek", 0)  # bezpieczny odczyt wartości (zwraca 0, jeśli brak klucza)
czy_jest = "imie" in person  # sprawdzenie, czy klucz istnieje w słowniku (True/False)

# Iteracja po kluczach, wartościach oraz parach (klucz, wartość)
for key, value in person.items():
    print(f"{key}: {value}")

# Łączenie dwóch słowników w jeden nowy słownik (Python 3.9+)
extra = {"status": "student"}
full_profile = person | extra

# Zliczanie wystąpień elementów (np. słów w tekście) za pomocą słownika
words = "kot pies kot".split()
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1  # zwiększa licznik o 1 albo startuje od 1


# ------------------------------------------------------------------------------
# 2. ZBIORY (set) — unikalne elementy i operacje teoriomnogościowe
# ------------------------------------------------------------------------------
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

suma = set_a | set_b  # suma zbiorów: {1, 2, 3, 4, 5, 6}
czesc_wspolna = set_a & set_b  # część wspólna (przecięcie): {3, 4}
roznica = set_a - set_b  # elementy w A, których nie ma w B: {1, 2}
roznica_symetryczna = set_a ^ set_b  # elementy należące tylko do jednego ze zbiorów: {1, 2, 5, 6}
czy_podzbior = {1, 2}.issubset(set_a)  # sprawdza, czy wszystkie elementy zawierają się w set_a


# ------------------------------------------------------------------------------
# 3. STOS (LIFO — Last In, First Out: ostatni na wejściu, pierwszy na wyjściu)
# ------------------------------------------------------------------------------
stack = queue.LifoQueue()

stack.put("pierwszy")  # odłożenie elementu na wierzch stosu
stack.put("drugi")
liczba_na_stosie = stack.qsize()  # aktualna liczba elementów na stosie

if not stack.empty():  # zawsze sprawdzamy przed zdjęciem, czy stos nie jest pusty
    top_item = stack.get()  # zdjęcie elementu z wierzchu stosu ("drugi")


# ------------------------------------------------------------------------------
# 4. KOLEJKA (FIFO — First In, First Out: pierwszy na wejściu, pierwszy na wyjściu)
# ------------------------------------------------------------------------------
fifo_queue = queue.Queue()

fifo_queue.put("Klient 1")  # dodanie elementu na koniec kolejki
fifo_queue.put("Klient 2")
liczba_w_kolejce = fifo_queue.qsize()  # aktualna długość kolejki

if not fifo_queue.empty():  # sprawdzamy, czy w kolejce ktoś czeka
    first_item = fifo_queue.get()  # pobranie najstarszego elementu z początku kolejki ("Klient 1")


# ------------------------------------------------------------------------------
# 5. PLIKI JSON — zapis i odczyt danych ustrukturyzowanych (zawsze encoding="utf-8")
# ------------------------------------------------------------------------------
json_filename = "dane.json"
sample_data = {
    "produkt": "Klawiatura",
    "cena": 199.99,
    "oplacone": True
}

# Zapis słownika lub listy do pliku JSON (ensure_ascii=False zachowuje polskie znaki)
with open(json_filename, "w", encoding="utf-8") as file:
    json.dump(sample_data, file, indent=4, ensure_ascii=False)

# Bezpieczny odczyt z pliku JSON po uprzednim sprawdzeniu, czy plik istnieje
if os.path.exists(json_filename):
    with open(json_filename, "r", encoding="utf-8") as file:
        loaded_data = json.load(file)
        print(f"Wczytano z JSON: {loaded_data['produkt']} - {loaded_data['cena']} zł")


# ------------------------------------------------------------------------------
# 6. PLIKI CSV — odczyt tabelaryczny wiersz po wierszu jako słowniki
# ------------------------------------------------------------------------------
csv_filename = "przyklad.csv"
if os.path.exists(csv_filename):
    with open(csv_filename, "r", encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)  # każdy wiersz to słownik {nazwa_kolumny: wartość}
        for row in reader:
            print(row)