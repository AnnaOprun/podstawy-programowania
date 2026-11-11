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
