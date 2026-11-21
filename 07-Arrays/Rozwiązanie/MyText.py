def count_words(text):
    words = text.split()  # dzielimy tekst na listę słów względem białych znaków
    return len(words)  # zwracamy liczbę słów


# Zwraca tablicę słów uporządkowaną od najdłuższego do najkrótszego
def words_by_length_desc(text):
    words = text.split()  # pobieramy listę słów z tekstu
    # Sortujemy słowa malejąco według ich długości (przy równej długości zachowujemy kolejność)
    return sorted(words, key=len, reverse=True)


# Zwraca tablicę słów uporządkowaną alfabetycznie
def words_alphabetically(text):
    words = text.split()  # pobieramy listę słów z tekstu
    return sorted(words)  # sortujemy słowa rosnąco według porządku znakowego (alfabetycznego)