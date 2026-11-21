def count_letter(text, letter):

    count = 0   # Licznik wystąpień szukanej litery

    for char in text:   # Przechodzimy po każdym znaku w przekazanym tekście
        if char == letter:
            count += 1

    return count    # Zwracamy łączną liczbę znalezionych wystąpień
