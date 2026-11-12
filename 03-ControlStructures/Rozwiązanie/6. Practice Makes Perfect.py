# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...
# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Program vowels.py liczy samogłoski w tekście. Zmodyfikuj program i zastąp instrukcję for instrukcją while.

# text = "This is a sample text."
# vowels = "aeiouAEIOU"
# vowel_count = 0

# # Inicjalizacja indeksu początkowego do przechodzenia po znakach tekstu
# index = 0

# # Pętla while wykonująca się dopóki indeks nie przekroczy długości tekstu
# while index < len(text):
    
#     char = text[index] # Pobranie pojedynczego znaku z tekstu na podstawie aktualnego indeksu

#     if char in vowels:   # Sprawdzenie, czy znak jest samogłoską
#         vowel_count += 1

#     index += 1  # Przejście do kolejnego znaku w tekście

# print(f"Liczba samogłosek w tekście wynosi: {vowel_count}")

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Lampa w pokoju ma trzy żarówki. Pierwszy przełącznik włącza jedną żarówkę, a drugi przełącznik włącza pozostałe dwie żarówki. 
# Napisz program, który informuje, ile żarówek świeci w zależności od stanu pierwszego i drugiego przełącznika.

# light_switch1 = True   # Stan pierwszego przełącznika (False - wyłączony, True - włączony)
# light_switch2 = False  # Stan drugiego przełącznika (False - wyłączony, True - włączony)
# bulbs_on = 0

# if light_switch1:
#     bulbs_on += 1 # Jeśli pierwszy przełącznik jest włączony, dodajemy 1 żarówkę

# if light_switch2:
#     bulbs_on += 2 # Jeśli drugi przełącznik jest włączony, dodajemy pozostałe 2 żarówki

# print(f"Liczba włączonych żarówek: {bulbs_on}")

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Długość hasła ma istotny wpływ na poziom ochrony danych. Napisz program, który sprawdza, czy nowe podane hasło ma co najmniej 12 znaków.

# new_password = input('Podaj nowe hasło: ')

# if len(new_password) < 12:
#     print('Hasło jest za krótkie (min. 12 znaków)')
# else:
#     print('Hasło ma odpowiednią długość')

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Elektroniczny termometr wypisuje temperaturę w stopniach Celsjusza oraz informację słowną zgodnie z następującymi kryteriami:
#       - Jest niezwykle gorąco (It is extremely hot), dla temperatury powyżej 35 stopni,
#       - Jest gorąco (It is hot), dla temperatury powyżej 30 stopni,
#       - Jest ciepło (It is warm), dla temperatury wynoszącej co najmniej 15 stopni,
#       - Jest zimno (It is cold), dla temperatury wynoszącej co najmniej 0 stopni,
#       - Ostrzeżenie, mróz (Warning, frost), dla temperatury poniżej 0 stopni.

# temperature = 32  # Możesz zmienić tę wartość, aby przetestować inne temperatury (np. 33, 30, 8, 0, -2)

# if temperature > 35:
#     print("It is extremely hot")
# elif temperature > 30:
#     print("It is hot")
# elif temperature >= 15:
#     print("It is warm")
# elif temperature >= 0:
#     print("It is cold")
# else:
#     print("Warning, frost")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Parkometr oblicza opłatę za parkowanie na podstawie liczby godzin, przez które samochód stał na parkingu, zgodnie z następującymi zasadami:
#       - 1-2 godziny: 5 PLN
#       - 3-6 godzin: 15 PLN
#       - Powyżej 6 godzin: 20 PLN
# Napisz program, który pyta o liczbę godzin parkowania, a następnie oblicza i wypisuje odpowiednią opłatę.

# hours = int(input("Podaj liczbę godzin parkowania: "))

# if 1 <= hours <= 2:
#     fee = 5
#     print(f"Opłata za {hours} godz. wynosi: {fee} PLN")
# elif 3 <= hours <= 6:
#     fee = 15
#     print(f"Opłata za {hours} godz. wynosi: {fee} PLN")
# elif hours > 6:
#     fee = 20
#     print(f"Opłata za {hours} godz. wynosi: {fee} PLN")
# else:
#     print("Niepoprawna liczba godzin.")

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który pyta użytkownika o jego wiek, a następnie sprawdza, do której grupy wiekowej należy:   
#       - Dziecko (Child): poniżej 13 lat   
#       - Nastolatek (Teen): od 13 do 19 lat   
#       - Dorosły (Adult): od 20 do 64 lat   
#       - Senior (Senior): 65 lat lub starszy

# age = int(input("Podaj swój wiek: "))

# if age < 13:
#     print("Grupa wiekowa: Dziecko")
# elif 13 <= age <= 19:
#     print("Grupa wiekowa: Nastolatek")
# elif 20 <= age <= 64:
#     print("Grupa wiekowa: Dorosły")
# else:
#     print("Grupa wiekowa: Senior")

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który sprawdza, czy obie osoby są pełnoletnie. Wczytaj dane osób z klawiatury.

# person1_name = input('Podaj imię pierwszej osoby: ')
# person1_age = int(input('Podaj wiek pierwszej osoby: '))
# person2_name = input('Podaj imię drugiej osoby: ')
# person2_age = int(input('Podaj wiek drugiej osoby: '))

# if person1_age >= 18 and person2_age >= 18:
#     print(f'Zarówno {person1_name}, jak i {person2_name} są pełnoletni.')
# else:
#     print(f'Przynajmniej jedna z osób ({person1_name} lub {person2_name}) nie jest pełnoletnia.')

# ZADANIE 9________________________________________________________________________________________________________________________________________________________________________
# Większość polskich imion żeńskich kończy się na literę „a”. Napisz program, który wypisuje imię wprowadzone z klawiatury, pod warunkiem, że jest to imię żeńskie.

# name = input("Podaj imię: ")

# if name.endswith('a') or name.endswith('A'): # Sprawdzamy, czy imię kończy się na małą lub wielką literę 'a'
#     print(f"{name} - Polish female name")
# else:
#     print("To nie jest imię żeńskie lub nie kończy się na literę 'a'.")

# ZADANIE 10_______________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza wiek psa w psie latach. Przez pierwsze dwa lata życie psa odpowiada 10,5 ludzkiego roku na każdy rok. 
# Po tym czasie każdy psi rok odpowiada 4 ludzkim latom.

# human_years = int(input("Wprowadź wiek psa w ludzkich latach: "))

# if human_years <= 2:
#     dog_years = human_years * 10.5
# else:
#     dog_years = 2 * 10.5 + (human_years - 2) * 4 

# print(f"Wiek psa w psich latach wynosi {int(dog_years)} lata.")

# ZADANIE 11_______________________________________________________________________________________________________________________________________________________________________
# Program komputerowy analizuje cenę produktu w sklepie internetowym. Jeśli cena produktu spadnie o co najmniej 10%, program wyświetli rekomendację zakupu:   
    # Buy the product!!
    # Product price reduced by 17%   
# Stwórz taki program. Aktualna i poprzednia cena produktu są zawarte w zmiennych. Przykładowy wynik:   
    # Current product price: 140.00
    # Previous product price: 200.00
    # Buy the product!!
    # Product price reduced by 30%

# current_price = 140.00  # Aktualna cena produktu
# previous_price = 200.00 # Poprzednia cena produktu

# discount = (previous_price - current_price) / previous_price * 100 # Obliczenie procentowego spadku ceny

# print(f"Current product price: {current_price:.2f}")
# print(f"Previous product price: {previous_price:.2f}")

# if discount >= 10: # Sprawdzenie, czy cena spadła o co najmniej 10%
#     print("Buy the product!!")
#     print(f"Product price reduced by {int(discount)}%")

# ZADANIE 12_______________________________________________________________________________________________________________________________________________________________________
# W jednym ze sklepów internetowych naliczany jest 25% rabat na każdy produkt zakupiony w liczbie większej niż dwa. 
# Napisz program, który oblicza kwotę do zapłaty. Wczytaj liczbę zakupionych produktów oraz cenę produktu z klawiatury.

# quantity = int(input("Number of products purchased: "))
# price = float(input("Product price: "))


# if quantity > 2:    # Sprawdzenie, czy liczba zakupionych produktów przekracza dwa
#     total_amount = (2 * price) + ((quantity - 2) * price * 0.75)    # Pierwsze dwa produkty są w pełnej cenie, a pozostałe ze zniżką 25% (płacimy 75% ceny)
# else:
#     total_amount = quantity * price    # Bez rabatu, jeśli zakupiono 2 lub mniej produktów

# print(f"Amount to pay: {total_amount:.2f}")

# ZADANIE 13_______________________________________________________________________________________________________________________________________________________________________
# Prędkość pojazdów na autostradach w Polsce wynosi co najmniej 40 km/h i nie więcej niż 140 km/h. 
# Napisz program, który wyświetla komunikat o przekroczeniu określonej prędkości samochodu odczytanej z klawiatury.

# speed_limit_min = 40
# speed_limit_max = 140

# car_speed = int(input("Enter car speed: "))

# if car_speed < speed_limit_min or car_speed > speed_limit_max:
#     print("Warning: invalid car speed!!")
# else:
#     print("Car speed is valid.")

# ZADANIE 14_______________________________________________________________________________________________________________________________________________________________________
# Influencer to osoba, która może wpływać na zachowanie innych ludzi. Influencer komunikuje się z innymi za pomocą portali społecznościowych. 
# Napisz program, który sprawdza, czy dana osoba jest dobrym influencerem, czyli czy posiada co najmniej dwa z następujących kont: Facebook, Twitter lub Instagram. 
# Użyj zmiennych logicznych: facebook, twitter, instagram, których wartość wskazuje, czy dana osoba posiada konto na portalu społecznościowym.

# facebook = True
# twitter = False
# instagram = True

# # Wyświetlenie statusu poszczególnych kont
# print(f"facebook = {facebook}")
# print(f"twitter = {twitter}")
# print(f"instagram = {instagram}")

# if (facebook and twitter) or (facebook and instagram) or (twitter and instagram):   # Sprawdzenie, czy użytkownik ma co najmniej dwa konta z wymienionych trzech
#     print("You are a good influencer!")
# else:
#     print("You are not a good influencer.")

# ZADANIE 15_______________________________________________________________________________________________________________________________________________________________________
# EAN-13 (European Article Number) to kod kreskowy służący do oznaczania towarów. Pierwsze 3 cyfry (590) zazwyczaj wskazują towary wyprodukowane w Polsce. 
# Napisz program, który sprawdza, czy wprowadzony z klawiatury numer EAN-13 składa się dokładnie z 13 znaków (cyfr). Wypisz komunikat, jeśli numer jest poprawny. 
# Dodatkowo, tylko wtedy, gdy numer artykułu jest poprawny, wyświetl komunikat, że produkt został wyprodukowany w Polsce.

# ean = input("Wprowadź numer artykułu EAN-13: ")

# if len(ean) == 13 and ean.isdigit():#  Sprawdzenie, czy długość kodu wynosi dokładnie 13 znaków oraz czy składa się wyłącznie z cyfr
#     print("Numer artykułu jest poprawny")
    
#     if ean[0:3] == "590":  # Dodatkowe sprawdzenie (tylko dla poprawnego numeru), czy kod zaczyna się od prefiksu "590" (Polska)
#         print("Artykuł wyprodukowany w Polsce")
# else:
#     print("Numer artykułu jest niepoprawny")

# ZADANIE 16_______________________________________________________________________________________________________________________________________________________________________
# Pralka pozwala na wypranie kurtki, co zajmuje 40 minut, bielizny, co zajmuje 70 minut, oraz butów, co zajmuje 20 minut. 
# Dodatkowo można zaprogramować dodatkowe płukanie (15 minut) oraz dodatkowe wirowanie (9 minut). Ustawienia pralki są zapisane w zmiennych. 
# Napisz program, który oblicza i wyświetla całkowity czas prania.

# total_washing_time = 0

# program = input('Wybierz program prania: (j) - kurtka, (u) - bielizna, (s) - buty: ')
# extra_rinse = input('Dodatkowe płukanie? (t/n): ')
# extra_spin = input('Dodatkowe wirowanie? (t/n): ')

# # Sprawdzenie czasu podstawowego programu prania
# if program == 'j':
#     total_washing_time += 40
# elif program == 'u':
#     total_washing_time += 70
# elif program == 's':
#     total_washing_time += 20

# # Dodanie czasu za dodatkowe płukanie (15 minut), jeśli wybrano 't'
# if extra_rinse.lower() == 't':
#     total_washing_time += 15

# # Dodanie czasu za dodatkowe wirowanie (9 minut), jeśli wybrano 't'
# if extra_spin.lower() == 't':
#     total_washing_time += 9

# print(f"Całkowity czas prania: {total_washing_time} minut")

# ZADANIE 17_______________________________________________________________________________________________________________________________________________________________________
# Napisz program, który umożliwia konwersję czasu z formatu 24-godzinnego na 12-godzinny. Czas w formacie 24-godzinnym (hh:mm) jest wczytywany z klawiatury. 

# time_24 = input("Wprowadź czas (format 24-godzinny hh:mm): ") # Pobieramy od użytkownika czas w formacie "hh:mm" jako tekst (string), np. "16:32"

# parts = time_24.split(":")# 2. Dzielimy wpisany tekst na dwie części w miejscu, gdzie znajduje się dwukropek (':') --> Metoda .split(":") tworzy listę, np. z "16:32" powstaje ["16", "32"]

# hours = int(parts[0]) # Wyciągamy pierwszą część (godziny) i zamieniamy ją z tekstu (string) na liczbę całkowitą (int), 
# minutes = parts[1]# Wyciągamy drugą część (minuty). Zostawiamy ją jako tekst, ponieważ minut nie musimy przeliczać,

# # Sprawdzamy, w jakim przedziale mieści się godzina, aby ustalić odpowiednik 12-godzinny oraz porę dnia (am/pm).
# if hours == 0:
#     # Jeśli jest północ (00:00), w systemie 12-godzinnym to godzina 12 w nocy (am)
#     hours_12 = 12
#     period = "am"
# elif hours < 12:
#     # Jeśli jest przed południem (od 01:00 do 11:59), godziny pozostają bez zmian (am)
#     hours_12 = hours
#     period = "am"
# elif hours == 12:
#     # Dokładnie w południe (12:00) to wciąż godzina 12, ale już po południu (pm)
#     hours_12 = 12
#     period = "pm"
# else:
#     # Dla godzin popołudniowych i wieczornych (od 13:00 do 23:59) 
#     # odejmujemy 12, aby uzyskać format 12-godzinny (np. 16 - 12 = 4), i oznaczamy jako pm
#     hours_12 = hours - 12
#     period = "pm"

# print(f"Czas w formacie 12-godzinnym: {hours_12}:{minutes}{period}")

# ZADANIE 18_______________________________________________________________________________________________________________________________________________________________________
# Niech $x$ i $y$ oznaczają współrzędne punktu na płaszczyźnie. Napisz program, który określa, w której ćwiartce układu współrzędnych 
# znajduje się punkt (x,y), na której osi leży, lub czy znajduje się w pozycji (0,0) układu współrzędnych. 

# x = float(input("Podaj współrzędną x: "))
# y = float(input("Podaj współrzędną y: "))

# if x == 0 and y == 0:
#     print(f"Punkt P({x}, {y}) znajduje się w początku układu współrzędnych (0,0)")

# elif x == 0: # Sprawdzenie, czy punkt leży na osi Y (x == 0, a y różne od 0)
#     print(f"Punkt P({x}, {y}) leży na osi Y")

# elif y == 0: # Sprawdzenie, czy punkt leży na osi X (y == 0, a x różne od 0)
#     print(f"Punkt P({x}, {y}) leży na osi X")

# elif x > 0 and y > 0: # Sprawdzenie pierwszej ćwiartki (x > 0, y > 0)
#     print(f"Punkt P({x}, {y}) znajduje się w pierwszej ćwiartce układu współrzędnych")

# elif x < 0 and y > 0: # Sprawdzenie drugiej ćwiartki (x < 0, y > 0)
#     print(f"Punkt P({x}, {y}) znajduje się w drugiej ćwiartce układu współrzędnych")

# elif x < 0 and y < 0: # Sprawdzenie trzeciej ćwiartki (x < 0, y < 0)
#     print(f"Punkt P({x}, {y}) znajduje się w trzeciej ćwiartce układu współrzędnych")

# else: # Jeżeli nie żadna z popszednich, to czwarta :D
#     print(f"Punkt P({x}, {y}) znajduje się w czwartej ćwiartce układu współrzędnych")

# ZADANIE 19_______________________________________________________________________________________________________________________________________________________________________
# Pytania zamknięte (tak-nie) są często używane w ankietach do oceny nastawienia ludzi do określonych idei lub przekonań. 
# Napisz program, który wyświetla ankietę składającą się z trzech pytań. Zapisz odpowiedzi w zmiennych typu logicznego. Następnie wyświetl wynik ankiety.

# q1_input = input("SURVEY Are you interested in computer science? (y/n): ")
# q2_input = input("Do you like playing computer games? (y/n): ")
# q3_input = input("Do you have an Instagram account? (y/n): ")

# # Konwersja odpowiedzi na zmienne logiczne (True, jeśli wpisano 'y', w przeciwnym razie False)
# interested_cs = q1_input.lower() == 'y'
# playing_games = q2_input.lower() == 'y'
# has_instagram = q3_input.lower() == 'y'

# print()
# print("SURVEY RESULTS")

# # Wyświetlanie wyników w formacie tekstowym Yes/No na podstawie zmiennych logicznych
# if interested_cs:
#     print("Interested in computer science: Yes")
# else:
#     print("Interested in computer science: No")

# if playing_games:
#     print("Playing computer games: Yes")
# else:
#     print("Playing computer games: No")

# if has_instagram:
#     print("Has an Instagram account: Yes")
# else:
#     print("Has an Instagram account: No")

# ZADANIE 20_______________________________________________________________________________________________________________________________________________________________________
# Program konwertujący liczbę dziesiętną na liczbę binarną przy użyciu pętli while

# decimal_number = int(input("Wprowadź liczbę dziesiętną: "))
# original_number = decimal_number

# binary_result = ""


# if decimal_number == 0: # Obsługa specjalnego przypadku dla liczby 0
#     binary_result = "0"
# else:

#     while decimal_number > 0:                           # Pętla wykonująca dzielenie przez 2, dopóki liczba (iloraz) jest większa od 0
#         remainder = decimal_number % 2                  # Obliczenie reszty z dzielenia przez 2
#         binary_result = str(remainder) + binary_result  # Doklejanie reszty na początek ciągu (ponieważ odczytujemy reszty od dołu do góry)
#         decimal_number = decimal_number // 2            # Podział całkowity liczby przez 2 w celu uzyskania nowego ilorazu

# print(f"{original_number}(10) = {binary_result}(2)")

# ZADANIE 21_______________________________________________________________________________________________________________________________________________________________________
# Dostępne są monety o nominałach 1, 2 i 5 złotych (PLN). 
# Napisz program przedstawiający dowolną kwotę (liczba naturalna) wczytaną z klawiatury przy użyciu jak najmniejszej liczby monet.

# amount = int(input("Wprowadź kwotę w PLN: "))
# original_amount = amount

# coins_5 = amount // 5   # Obliczenie liczby monet 5 zł (dzielenie całkowite)
# amount = amount % 5     # Reszta do wydania po odliczeniu monet 5 zł
# coins_2 = amount // 2   # Obliczenie liczby monet 2 zł z pozostałej kwoty
# amount = amount % 2     # Reszta do wydania po odliczeniu monet 2 zł
# coins_1 = amount        # Pozostała kwota to liczba monet 1 zł

# print(f"Kwota PLN {original_amount} w monetach:")
# print(f"Monety 5 PLN: {coins_5}")
# print(f"Monety 2 PLN: {coins_2}")
# print(f"Monety 1 PLN: {coins_1}")

# ZADANIE 22_______________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje liczby od 1 do 30. Jeśli liczba jest podzielna przez 3, program wypisuje słowo „THREE”. 
# Następnie, jeśli liczba jest podzielna przez 5, program wypisuje słowo „FIVE”. 
# Na koniec, jeśli liczba jest podzielna zarówno przez 3, jak i przez 5, program wypisuje słowo „BINGO”.

# for number in range(1, 31):  # Pętla przechodząca przez wszystkie liczby od 1 do 30
#     if number % 3 == 0 and number % 5 == 0:  # Sprawdzenie, czy liczba jest podzielna zarówno przez 3, jak i przez 5
#         print("BINGO", end=" ")
   
#     elif number % 3 == 0: # Sprawdzenie, czy liczba jest podzielna przez 3
#         print("THREE", end=" ")
    
#     elif number % 5 == 0: # Sprawdzenie, czy liczba jest podzielna przez 5
#         print("FIVE", end=" ")
    
#     else: # Jeśli liczba nie spełnia powyższych warunków, wypisujemy jej normalną wartość
#         print(number, end=" ")

# UWAGA: Warunek podzielności przez obie te liczby jednocześnie (zarówno przez 3, jak i przez 5, czyli przez 15) musimy sprawdzić na samym początku. 
# Gdybyśmy najpierw sprawdzali samą podzielność przez 3, liczba taka jak 15 wyświetliłaby się jako „THREE” zamiast „BINGO”.

# ZADANIE 23_______________________________________________________________________________________________________________________________________________________________________
# Napisz program, który tworzy tabelę mnożenia w zakresie od 1 do 10 dla dowolnej liczby wprowadzonej przez użytkownika.

# number = int(input("Wprowadź liczbę: "))

# # Pętla iterująca od 1 do 10 w celu wygenerowania kolejnych wierszy tabeli mnożenia
# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")

# ZADANIE 24_______________________________________________________________________________________________________________________________________________________________________
# Napisz program, który tworzy następujący wzór.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(1, 6): # rosnący wzór od 1 do 5 gwiazdek w wierszu
#     print("* " * i)

# for i in range(4, 0, -1): #  malejący wzór od 4 do 1 gwiazdki w wierszu
#     print("* " * i)

# ZADANIE 25_______________________________________________________________________________________________________________________________________________________________________
# Napisz program, który tworzy następujący wzór.
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# 88888888
# 999999999  

# for i in range(1, 10):
#     print(str(i) * i) # Wyświetlenie cyfry 'i' powtórzonej 'i' razy

# ZADANIE 26_______________________________________________________________________________________________________________________________________________________________________
# Karta płatnicza jest zabezpieczona czterocyfrowym kodem PIN (0805). Napisz program, który sprawdza, czy kod PIN wprowadzony w terminalu płatniczym jest poprawny.
# Użytkownik ma do dyspozycji maksymalnie trzy próby wprowadzenia kodu PIN. W przypadku trzech nieudanych prób karta zostaje zablokowana.

# correct_pin = "0805"
# attempts = 3

# while attempts > 0: # Pętla wykonująca się dopóki użytkownik ma dostępne próby
#     entered_pin = input("Wprowadź kod PIN: ")
    
#     if entered_pin == correct_pin:
#         print("Poprawny PIN. Dostęp przyznany!")
#         break
#     else:
#         print("Niepoprawny...")
#         attempts -= 1  # Zmniejszenie liczby pozostałych prób o 1

# if attempts == 0: # Jeśli wyczerpano wszystkie próby i nie wpisano poprawnego PIN-u
#     print("Przepraszamy, Twoja karta płatnicza została zablokowana.")

# ZADANIE 27_______________________________________________________________________________________________________________________________________________________________________
# Komputerowa klawiatura numeryczna ma układ klawiszy jak poniżej.                                                  7 8 9
# Dołączony kod programu drukuje klawiaturę komputera. Przeanalizuj program pod kątem uzyskanych wyników.           4 5 6
# Czy rozumiesz każdą instrukcję programu? Następnie zmodyfikuj kod programu, zastępując pętlę for pętlą while.     1 2 3

# for i in range(6, -1, -3): # Zewnętrzna pętla (sterowana zmienną i) odpowiada za kolejne wiersze klawiatury numerycznej i przyjmuje wartości: 6, 3 oraz 0.
#     for j in range(1, 4): # Wewnętrzna pętla (sterowana zmienną j) odpowiada za kolumny i wykonuje się trzykrotnie dla każdego wiersza, przyjmując wartości od 1 do 3.
#         print(f'{i + j}', end=' ') # Obliczanie wartości polega na dodaniu do siebie zmiennych i + j, co daje odpowiednie cyfry klawiatury w każdym wierszu (7 8 9, 4 5 6, 1 2 3).
#     print() # puste print() przenosi kursor do nowej linii po zakończeniu każdego wiersza.
# _________________________________________________________________________________

# i = 6 # Ustawiamy początkową wartość i na 6 (odpowiednik początku range(6, -1, -3))

# while i >= 0: # Zewnętrzna pętla działa tak długo, jak i jest większe lub równe 0

#     j = 1 # Dla każdego wiersza resetujemy j do wartości 1

#     while j < 4: # Wewnętrzna pętla działa dla j od 1 do 3 (zamiast range(1, 4))

#         print(f'{i + j}', end=' ')
#         j += 1  # Zwiększamy j o 1 w każdym kroku

#     print() # Przechodzimy do nowej linii po wypisaniu całego wiersza
#     i -= 3  # Zmniejszamy i o 3 w każdym kroku (odpowiednik skoku -3 w range)

# ZADANIE 28_______________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje pierwsze dwadzieścia wyrazów ciągu Fibonacciego. 
# Ciąg jest zdefiniowany następująco: pierwszy wyraz jest równy 0, drugi jest równy 1, a każdy kolejny wyraz jest sumą dwóch poprzednich.

# a = 0
# b = 1

# print("Pierwsze 20 wyrazów ciągu Fibonacciego:")

# for i in range(20): # Pętla wykonująca się 20 razy
#     print(a, end=" ") # Wypisujemy aktualny wyraz (a) z odstępem
    
#     a, b = b, a + b # Obliczamy kolejny wyraz jako sumę dwóch poprzednich
#                     # a = b
#                     # b = a + b
# print()

# ZADANIE 29_______________________________________________________________________________________________________________________________________________________________________
# Liczba naturalna większa niż 1 jest nazywana liczbą pierwszą, jeśli ma dokładnie dwa czynniki naturalne o wartościach 1 oraz ta liczba. 
# Napisz program, który znajduje N pierwszych liczb pierwszych. 
# Odczytaj wartość N z klawiatury. Używając instrukcji pętli, sprawdź, czy dana liczba jest podzielna tylko przez 1 i przez siebie. 

# n = int(input("Wprowadź liczbę N (ile liczb pierwszych wypisać): "))

# found_primes = 0  # licznik, który śledzi, ile liczb pierwszych już znaleźliśmy.
# current_number = 2  # liczba, którą w danym momencie sprawdzamy (zaczynamy od 2, bo to najmniejsza liczba pierwsza).

# print("Liczby pierwsze:", end=" ")

# while found_primes < n:
#     is_prime = True  # Zakładamy, że sprawdzana liczba jest pierwsza
    
#     # Sprawdzamy dzielniki od 2 do current_number -1
#     # Tutaj używamy tradycyjnego sprawdzenia mniejszego od current_number za pomocą pętli
#     divisor = 2
#     while divisor < current_number:
#         if current_number % divisor == 0:
#             is_prime = False  # Znaleziono dzielnik, więc to nie jest liczba pierwsza
#             break
#         divisor += 1
        
#     # Jeśli liczba jest pierwsza, wypisujemy ją i zwiększamy licznik znalezionych
#     if is_prime and current_number > 1:
#         print(current_number, end=" ")
#         found_primes += 1

#     current_number += 1 # Przechodzimy do sprawdzenia kolejnej liczby całkowitej
# print()

# ZADANIE 30_______________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje kupon loterii (liczby od 1 do 49) w formacie jak poniżej.
# 1 8 15 22 29 36 43
# 2 9 16 23 30 37 44
# 3 10 17 24 31 38 45
# 4 11 18 25 32 39 46
# 5 12 19 26 33 40 47
# 6 13 20 27 34 41 48
# 7 14 21 28 35 42 49

# for i in range(1, 8): # Pętla zewnętrzna odpowiada za kolejne wiersze (od 1 do 7)
#     for j in range(i, 50, 7): # Pętla wewnętrzna generuje liczby w danym wierszu, zaczynając od 'i' do 49 ze skokiem co 7
#         print(j, end=" ") # Wypisujemy liczby w tej samej linii, oddzielone spacją
#     print() # Przejście do nowej linii po zakończeniu całego wiersza

# ZADANIE 31_______________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje 20 losowych liczb całkowitych z zakresu od 5 do 10.

# import random

# print("Losowe liczby:", end=" ")

# for i in range(20):
    
#     random_number = random.randint(5, 10)
#     print(random_number, end=" ")

# print()