def hide(card_number):
    card = str(card_number)  # Zamieniamy na napis na wypadek przekazania liczby

    # Pobieramy pierwsze dwa znaki oraz ostatnie cztery znaki
    first_two = card[:2]
    last_four = card[-4:]

    masked_middle = "*" * (len(card) - 6)  # Pozostałe cyfry w środku zastępujemy gwiazdkami '*'

    return first_two + masked_middle + last_four