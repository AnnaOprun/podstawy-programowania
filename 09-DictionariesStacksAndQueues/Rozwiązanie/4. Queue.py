# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Kolejka to liniowa struktura danych działająca zgodnie z zasadą FIFO (First In, First Out — pierwszy na wejściu, pierwszy na wyjściu). 
# znacza to, że pierwszy element dodany do kolejki będzie pierwszym elementem, który zostanie z niej usunięty. 
# Kolejka działa podobnie do kolejki w prawdziwym życiu, na przykład kolejki osób oczekujących na obsługę — osoba, która przyjdzie jako pierwsza, jest obsługiwana jako pierwsza.

# W pliku queue_example.py znajdziesz prosty przykład tworzenia kolejki i operowania na niej. Przeanalizuj i uruchom program.

# import queue

# # Przykładowy program demonstrujący działanie kolejki FIFO na bazie queue.Queue()

# waiting_line = queue.Queue()  # tworzymy kolejkę FIFO z modułu queue

# waiting_line.put("Anna")  # dodajemy pierwszy element na koniec kolejki (enqueue)
# waiting_line.put("Marek")  # dodajemy drugi element na koniec kolejki
# waiting_line.put("Kasia")  # dodajemy trzeci element na koniec kolejki

# print("Liczba osób w kolejce:", waiting_line.qsize())  # sprawdzamy bieżącą liczbę elementów

# while not waiting_line.empty():  # dopóki kolejka nie jest pusta, obsługujemy kolejne osoby
#     person = waiting_line.get()  # pobieramy element z przodu kolejki (dequeue - zasada FIFO)
#     print("Obsługiwana osoba:", person)

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Korzystając z kolejki, napisz program zarządzający kolejką plików do wydrukowania.

# import queue

# files_to_print = queue.Queue()  # kolejka plików oczekujących na wydruk (zasada FIFO)

# while True:  # główna pętla obsługująca menu użytkownika
#     print('1. Dodaj plik do drukowania')
#     print('2. Drukuj plik')
#     print('0. Wyjdź')
#     menu = input('Wybierz opcję: ').strip()

#     if menu == '1':  # dodajemy nowy plik na koniec kolejki
#         file_name = input('Podaj nazwę pliku do wydrukowania: ').strip()
#         if file_name != '':
#             files_to_print.put(file_name)  # dopisujemy plik na koniec kolejki FIFO
#             print(f"Dodano plik '{file_name}' do kolejki drukowania.")
#         else:
#             print("Nazwa pliku nie może być pusta.")
#     elif menu == '2':  # pobieramy do druku pierwszy plik z kolejki
#         if not files_to_print.empty():  # sprawdzamy, czy w kolejce są jeszcze pliki
#             file_to_print = files_to_print.get()  # zdejmujemy najstarszy plik z przodu kolejki
#             print(f"Trwa drukowanie pliku {file_to_print}. Proszę czekać!")
#         else:
#             print("Kolejka plików do wydrukowania jest pusta.")
#     elif menu == '0':  # kończymy działanie programu
#         print("Kończę pracę programu.")
#         break
#     else:
#         print("Nieprawidłowa opcja. Wybierz 1, 2 lub 0.")