# Moduł zawierający funkcje do wczytywania różnych typów danych z klawiatury


def input_string(message):  # Wczytuje i zwraca zwykły napis podany przez użytkownika
    text = input(message)
    return text

def input_integer(message): # Wczytuje napis i zamienia go na liczbę całkowitą (int)
    number = int(input(message))
    return number

def input_real(message):    # Wczytuje napis i zamienia go na liczbę rzeczywistą (float)
    real_number = float(input(message))
    return real_number


def input_boolean(message):     # Wczytuje odpowiedź 'y' lub 'n' i zwraca wartość logiczną True lub False
    answer = input(message).strip().lower() #.strip() usuwa ewentualne zbędne spacje
    if answer == "y":
        return True
    else:
        return False