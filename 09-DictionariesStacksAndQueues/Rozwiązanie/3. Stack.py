# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Stos to liniowa struktura danych działająca zgodnie z zasadą LIFO (Last In, First Out — ostatni na wejściu, pierwszy na wyjściu). 
# Oznacza to, że ostatni element dodany na stos jest pierwszym elementem, który zostanie z niego usunięty. Wyobraź sobie stos jako stertę talerzy — ostatni talerz, 
# który położysz na górze, będzie pierwszym, który zdejmiesz.

# W pliku stack_example.py znajdziesz prosty przykład tworzenia stosu i operowania na nim. Przeanalizuj i uruchom program. 
# Następnie zmodyfikuj program tak, aby wykonał następujące operacje:

# stack = []  # tworzymy pusty stos reprezentowany przez listę

# # i.–vii. Odkładamy kolejne liczby na wierzch stosu metodą append()
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.append(4)
# stack.append(1)
# stack.append(9)
# stack.append(8)

# # viii. Zdejmujemy dwie ostatnie liczby ze stosu metodą pop() (LIFO) i liczymy ich sumę
# last_one = stack.pop()  # zdejmuje 8 (ostatni dodany element)
# last_two = stack.pop()  # zdejmuje 9 (poprzedni dodany element)
# sum_last_two = last_one + last_two
# print(f"Suma dwóch ostatnich liczb ze stosu ({last_two} + {last_one}): {sum_last_two}")

# # ix. Obliczamy sumę pozostałych elementów na stosie w pętli while, zdejmując je ze stosu
# remaining_sum = 0
# while stack:  # pętla działa dopóki na stosie znajdują się jeszcze elementy
#     remaining_sum += stack.pop()  # zdejmujemy kolejny element z wierzchu i dodajemy do sumy

# print(f"Suma pozostałych elementów na stosie: {remaining_sum}")

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Program back.py symuluje działanie przycisku „Wstecz” w przeglądarce internetowej (zapisuje nazwę nowej odwiedzonej strony lub wyświetla poprzednio odwiedzoną stronę). 

# import queue

# # Program symulujący przycisk "Wstecz" w przeglądarce internetowej za pomocą stosu LifoQueue

# visited_websites = queue.LifoQueue()  # tworzymy stos na historię odwiedzonych stron (zasada LIFO)

# # Przykładowe wcześniej odwiedzone strony odłożone na stos
# visited_websites.put('instagram.com')
# visited_websites.put('uek.krakow.pl')
# visited_websites.put('microsoft.com')  # na samej górze stosu

# while True:  # pętla obsługująca wpisywanie adresów oraz cofanie się
#     website = input('Podaj nazwę strony (0 aby cofnąć): ').strip()

#     if website == '0':  # użytkownik chce wrócić do poprzedniej strony
#         if visited_websites.empty():  # gdy stos jest pusty, nie ma już do czego wrócić
#             print("Brak wcześniejszych stron w historii. Kończę działanie.")
#             break
#         else:
#             print('<-- Powrót do poprzednio odwiedzonej strony')
#             website = visited_websites.get()  # zdejmujemy ostatnio odwiedzoną stronę ze stosu
#     elif website != "":  # gdy wpisano niepusty adres nowej strony
#         visited_websites.put(website)  # zapisujemy nową stronę na wierzchu stosu
#     else:
#         print("Nie podano nazwy strony.")  # obsługa pustego wejścia bez dodawania pustego wpisu
#         continue

#     # Wyświetlamy nazwę aktualnie oglądanej strony
#     print('Aktualnie przeglądasz:', website)
#     print()

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję, która zwraca True, jeśli nawiasy (), {}, [] zostały użyte poprawnie w podanym wyrażeniu. 
# W przeciwnym razie funkcja zwraca False. Następnie napisz program, który sprawdza poprawność podanych poniżej wyrażeń.

# Użyj stosu. Czytaj kolejne znaki wyrażenia. Pomijaj wszystkie znaki poza nawiasami. Jeśli jest to nawias otwierający, połóż go na stosie. 
# Jeśli jest to nawias zamykający, pobierz element ze stosu i sprawdź, czy jest to pasujący nawias otwierający.

# import queue

# # Program sprawdzający poprawność nawiasów (), {}, [] w wyrażeniu za pomocą stosu LifoQueue

# expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # nawiasy poprawne
# expression2 = "[(2+3]/4)"                # nawiasy niepoprawne
# expression3 = "(2-3*4+(5/6)"              # nawiasy niepoprawne


# def brackets_ok(expression):
#     """Zwraca True, jeśli nawiasy (), {} oraz [] w wyrażeniu są poprawnie sparowane."""
#     stack = queue.LifoQueue()  # stos przechowujący otwarte nawiasy (zasada LIFO)
#     matching = {')': '(', '}': '{', ']': '['}  # mapa: nawias zamykający -> odpowiadający mu otwierający

#     for char in expression:  # przeglądamy wyrażenie znak po znaku[cite: 19]
#         if char in "({[":  # jeśli napotkamy nawias otwierający, odkładamy go na stos[cite: 19]
#             stack.put(char)
#         elif char in ")}]":  # jeśli napotkamy nawias zamykający, sprawdzamy zgodność ze stosem[cite: 19]
#             if stack.empty():  # brak otwierającego nawiasu dla zamykającego
#                 return False
#             top_bracket = stack.get()  # zdejmujemy ostatnio otwarty nawias ze stosu[cite: 19]
#             if top_bracket != matching[char]:  # sprawdzamy, czy nawiasy do siebie pasują[cite: 19]
#                 return False
#         # pozostałe znaki (cyfry, operatory, spacje itp.) pomijamy[cite: 19]

#     return stack.empty()  # poprawne tylko wtedy, gdy na stosie nie zostało nic niezamkniętego


# if brackets_ok(expression1):
#     print("Wyrażenie 1 ma poprawne nawiasy.")
# else:
#     print("Wyrażenie 1 ma niepoprawne nawiasy.")

# if brackets_ok(expression2):
#     print("Wyrażenie 2 ma poprawne nawiasy.")
# else:
#     print("Wyrażenie 2 ma niepoprawne nawiasy.")

# if brackets_ok(expression3):
#     print("Wyrażenie 3 ma poprawne nawiasy.")
# else:
#     print("Wyrażenie 3 ma niepoprawne nawiasy.")

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który zamienia dowolną liczbę naturalną na liczbę binarną. Użyj stosu. 
# Aby zamienić liczbę, dziel ją przez 2, za każdym razem biorąc resztę z dzielenia i odkładając tę resztę na stos. Powtarzaj dzielenie, dopóki dzielona liczba nie osiągnie zera. 
# Następnie zdejmij ze stosu i wyświetl wszystkie wartości.

# import queue

# # Program zamieniający liczbę naturalną na zapis binarny za pomocą stosu LifoQueue

# number = int(input("Podaj liczbę naturalną: "))  # wczytujemy liczbę naturalną od użytkownika
# stack = queue.LifoQueue()  # stos przechowujący reszty z dzielenia przez 2 (zasada LIFO)

# if number == 0:
#     stack.put(0)  # dla zera zapis binarny to po prostu 0
# else:
#     current = number  # kopia liczby, którą będziemy dzielić całkowitoliczbowo przez 2
#     while current > 0:  # powtarzamy dzielenie, dopóki liczba nie spadnie do zera
#         remainder = current % 2  # obliczamy resztę z dzielenia przez 2
#         stack.put(remainder)  # odkładamy resztę na wierzch stosu
#         current //= 2  # wykonujemy dzielenie całkowite przez 2

# binary_digits = []  # lista na cyfry binarne odczytane ze stosu w odwrotnej kolejności
# while not stack.empty():  # zdejmujemy elementy ze stosu od góry (od ostatniej reszty)
#     binary_digits.append(str(stack.get()))

# binary_representation = "".join(binary_digits)  # łączymy cyfry w jeden napis binarny

# print(f"Liczba naturalna: {number}")
# print(f"Liczba binarna: {binary_representation}")