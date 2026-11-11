# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...
# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Pętla while wykonuje blok kodu tak długo, jak określony warunek jest prawdziwy (True).
# while condition:
#     # blok kodu do wykonania

# count = 0
# while count < 5:
#     print(count) # --> 0 1 2 3 4
#     count += 1  

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje powitanie.
 
# name = '' 

# while name == '': # Program wypisujący powitanie na podstawie podanego imienia
#     name = input('Podaj swoje imię: ')

# print(f'Witaj {name}')

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Poniższy program to prosta gra w zgadywanie liczb. Przeanalizuj kod programu, a następnie uzupełnij go.

# import random

# number_to_guess = random.randint(1, 100)
# user_guess = 0

# print("Zgadnij liczbę z zakresu od 1 do 100!")

# while user_guess != number_to_guess:
#     user_guess = int(input("Podaj swoją propozycję: "))

#     if user_guess < number_to_guess:
#         print("Za mało! Spróbuj ponownie.")
#     elif user_guess > number_to_guess:
#         print("Za dużo! Spróbuj ponownie.")
#     else:
#         print("Gratulacje! Odgadłeś właściwą liczbę.")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Poniższy program sumuje liczby wprowadzane przez użytkownika, dopóki nie wprowadzi on 0. Zmodyfikuj program tak, aby obliczał również średnią arytmetyczną tych liczb.

# total_sum = 0
# count = 0

# while True:
#     number = int(input("Podaj liczbę (0 kończy działanie): "))
    
#     if number == 0:
#         break  # Wyjście z pętli po wprowadzeniu 0
    
#     total_sum += number
#     count += 1

# if count > 0:
#     arithmetic_mean = total_sum / count
#     print(f"Suma całkowita liczb wynosi: {total_sum}")
#     print(f"Średnia arytmetyczna wynosi: {arithmetic_mean}")
# else:
#     print("Nie podano żadnych liczb.")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Poniższy program oblicza sumę liczb parzystych od 1 do podanej liczby N za pomocą pętli for. Zmodyfikuj program i zastąp instrukcję for instrukcją while.

# N = 10
# sum_even = 0
# i = 1

# while i <= N:
#     if i % 2 == 0:
#         sum_even += i
#     i += 1

# print(f"Suma liczb parzystych od 1 do {N} wynosi: {sum_even}")

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Program timer.py pobiera liczbę od użytkownika i odlicza w dół do zera. 
# Zmodyfikuj program tak, aby ostatnie pięć sekund odliczania było wypisywane słownie, tj. five, four, three, two, one.

# import time

# seconds = int(input("Podaj liczbę sekund do odliczenia: "))

# while seconds > 0:
#     if seconds == 5:
#         print("five")
#     elif seconds == 4:
#         print("four")
#     elif seconds == 3:
#         print("three")
#     elif seconds == 2:
#         print("two")
#     elif seconds == 1:
#         print("one")
#     else:
#         print(seconds)
    
#     time.sleep(1)  # Odczekanie 1 sekundy
#     seconds -= 1

# print("Czas minął!")

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Program atm.py symuluje prosty bankomat, w którym użytkownik może wpłacać, wypłacać pieniądze lub sprawdzać saldo. 
# Przeanalizuj kod programu, a następnie go uruchom. Następnie dodaj do programu dwie kolejne funkcje:  Sprawdzenie PIN-u | Zmiana PIN-u

# PIN powinien składać się dokładnie z 4 cyfr. Aby sprawdzić, czy łańcuch tekstowy zawiera wyłącznie cyfry, możesz użyć metody isdigit(). 
# Metoda ta zwraca wartość True, jeśli wszystkie znaki w ciągu są cyframi, a w przeciwnym razie False:


balance = 1000  # Początkowe saldo konta
pin = '1111'    # Początkowy 4-cyfrowy kod PIN
pin_entered = False  # Flaga określająca, czy użytkownik pomyślnie podał PIN

# Etap weryfikacji PIN-u przed przyznaniem dostępu do menu (maksymalnie 3 próby)
for attempt in range(3):
    entered_pin = input("Podaj 4-cyfrowy PIN: ")
    if entered_pin == pin:
        pin_entered = True
        break  # Przerwij pętlę prób, jeśli PIN jest poprawny
    else:
        print("Niepoprawny PIN.")

# Jeśli po 3 próbach PIN nie został poprawnie podany, blokujemy dostęp
if not pin_entered:
    print("Przekroczono liczbę prób. Karta została zablokowana.")
else:
    # Główna pętla programu bankomatu
    while True:
        print()
        print("Menu bankomatu:")
        print("1. Sprawdź saldo")
        print("2. Wpłać środki")
        print("3. Wypłać środki")
        print("4. Zmień PIN")
        print("5. Wyjdź")

        # Pobranie wyboru użytkownika z klawiatury
        choice = input("Wybierz opcję (1-5): ")
        print()

        # Opcja 1: Wyświetlenie aktualnego salda
        if choice == '1':
            print(f"Twoje aktualne saldo wynosi: €{balance}")
            
        # Opcja 2: Wpłata pieniędzy na konto
        elif choice == '2':
            amount = float(input("Podaj kwotę do wpłaty: "))
            balance += amount
            print(f"Wpłacono €{amount}. Nowe saldo: €{balance}")
            
        # Opcja 3: Wpłata/wypłata pieniędzy z konta (z sprawdzeniem stanu środków)
        elif choice == '3':
            amount = float(input("Podaj kwotę do wypłaty: "))
            if amount <= balance:
                balance -= amount
                print(f"Wpłacono/Wypłacono €{amount}. Nowe saldo: €{balance}")
            else:
                print("Niewystarczające środki na koncie.")
                
        # Opcja 4: Zmiana kodu PIN
        elif choice == '4':
            old_pin = input("Podaj stary PIN: ")
            if old_pin == pin:
                new_pin = input("Podaj nowy 4-cyfrowy PIN: ")
                # Sprawdzamy czy nowy PIN ma długość 4 znaków i składa się wyłącznie z cyfr
                if len(new_pin) == 4 and new_pin.isdigit():
                    pin = new_pin
                    print("PIN został pomyślnie zmieniony.")
                else:
                    print("Nowy PIN musi składać się dokładnie z 4 cyfr.")
            else:
                print("Stary PIN jest niepoprawny.")
                
        # Opcja 5: Wyjście z programu
        elif choice == '5':
            print("Trwa zamykanie... Dziękujemy za skorzystanie z bankomatu!")
            break  # Wyjście z pętli while
            
        # Obsługa niepoprawnego wyboru z menu
        else:
            print("Niepoprawna opcja. Spróbuj ponownie.")