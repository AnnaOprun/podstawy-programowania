# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Wyrażenia regularne (regex) to ciągi znaków definiujące wzorzec wyszukiwania. Służą do wyszukiwania, dopasowywania oraz przetwarzania tekstu. 
# Wyrażenia regularne zapewniają potężny sposób wykonywania złożonego przetwarzania tekstu, takiego jak wyszukiwanie określonych wzorców w napisie, 
# walidacja danych wejściowych, zastępowanie tekstu czy wydobywanie informacji z dużych ilości danych.

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
#   ...

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# kopiuj poniższy tekst do edytora internetowego Regex101:[https://regex101.com/](https://regex101.com/)  
#  Następnie dla każdego z poniższych podpunktów utwórz wzorzec, który identyfikuje fragmenty tekstu zgodnie z opisem w zadaniu:
    # Znajdź wszystkie daty w formacie „miesiąc dzień, rok” (np. „March 12, 1992”).
    # Zlokalizuj wszystkie numery telefonów w formacie „XXX-XXX-XXXX” (np. „555-123-4567”).Z
    # najdź wszystkie liczby zapisane z przecinkami jako separatorami tysięcy (np. „1,234”).
    # Zidentyfikuj wszystkie fragmenty zawierające imiona zaczynające się wielką literą (np. „Alice”, „John”, „Mike”).
    # Znajdź w tekście liczby całkowite (np. „30”).  

# 1. [A-Z][a-z]+ \d{1,2}, \d{4}  -->  szuka nazwy miesiąca zaczynającej się wielką literą [A-Z] z przynajmniej jedną małą literą [a-z]+, po której występuje spacja, jedno- lub dwucyfrowy numer dnia \d{1,2}, przecinek ze spacją oraz czterocyfrowy rok \d{4}
# 2. \d{3}-\d{3}-\d{4}           -->  dopasowuje dokładnie trzy cyfry, myślnik, trzy cyfry, kolejny myślnik oraz cztery cyfry, dzięki czemu znajduje numery telefonów
# 3. \d{1,3}(?:,\d{3})+          -->  zaczyna od jednej do trzech cyfr na początku liczby, a następnie wymaga jednego lub więcej powtórzeń grupy złożonej z przecinka i dokładnie trzech cyfr (zapis (?:...) oznacza grupę nieprzechwytującą, żeby edytor podświetlał całą liczbę w jednym kawałku
# 4. \b[A-Z][a-z]+\b             -->  wyłapuje pojedyncze słowa (ograniczone granicami słowa \b), które zaczynają się wielką literą i dalej mają małe litery, przy czym warto zwrócić uwagę, że taki prosty wzorzec złapie też nazwy miesięcy albo słowo na początku zdania, ponieważ wyrażenie regularne widzi tylko kształt liter, a nie znaczenie słowa w języku angielskim
# 5. \b\d+\b                     -->  wyszukuje dowolne samodzielne ciągi samych cyfr otoczone granicami słowa \b, dzięki czemu dopasuje pełne liczby całkowite takie jak 30, 12, 1992 czy 5, ale nie rozetnie numeru telefonu ani liczby z przecinkiem na przypadkowe kawałki w środku wyrazu

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Plik report.txt zawiera wiadomość e-mail z raportem zakupowym. Napisz program, który oblicza łączną kwotę wydanych pieniędzy.
# Wskazówka: aby otworzyć i odczytać plik tekstowy zawierający znaki specjalne (takie jak znak euro €), 
# musisz upewnić się, że plik jest odczytywany z użyciem odpowiedniego kodowania znaków. Najczęstszym kodowaniem w takich przypadkach jest UTF-8, 
# które obsługuje szeroki zakres znaków, w tym symbole specjalne.

# import re  # moduł wyrażeń regularnych

# email_file = "report.txt"  # nazwa pliku zawierającego raport zakupowy

# with open(email_file, "r", encoding="utf-8") as file:   # Otwieramy plik w trybie odczytu ('r') z kodowaniem UTF-8 i wczytujemy jego całą treść
#     email = file.read()  # przechowujemy treść wiadomości e-mail jako jeden napis

# pattern = r"\d+(?:[.,]\d+)?"    # Wzorzec dopasowujący kwoty z opcjonalną częścią ułamkową po kropce lub przecinku
# amounts = re.findall(pattern, email)    # Wyciągamy z treści wiadomości wszystkie pasujące fragmenty kwot

# # Sumujemy znalezione kwoty po zamianie przecinka na kropkę i konwersji na liczbę zmiennoprzecinkową
# total = 0.0  # akumulator przechowujący łączną wartość wydanych pieniędzy
# for amount in amounts:
#     normalized_amount = amount.replace(",", ".")  # ujednolicamy separator dziesiętny przed rzutowaniem na float
#     total += float(normalized_amount)  # dodajemy kolejną kwotę do łącznej sumy

# print(f"Łączna kwota wydanych pieniędzy: {total:.2f}")

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Wiele aplikacji wymaga utworzenia konta z nazwą użytkownika i hasłem, aby z nich korzystać. 
# Często aplikacje określają wymagania dotyczące nazwy użytkownika i hasła. 
# Napisz program, który sprawdza, czy nazwa użytkownika i hasło wprowadzone z klawiatury spełniają poniższe wymagania. Użyj wyrażeń regularnych.   
    # nazwa użytkownika ma długość co najmniej 6 znaków   
    # nazwa użytkownika zawiera wyłącznie małe litery
    # hasło ma długość co najmniej 8 znaków
    # hasło zawiera wyłącznie litery (małe i wielkie), cyfry oraz znak podkreślenia

# import re  # moduł do obsługi wyrażeń regularnych

# username = input("Podaj nazwę użytkownika: ") 
# password = input("Podaj hasło: ") 

# # Wzorzec wymaga co najmniej 6 małych liter od początku do końca napisu
# username_pattern = r"^[a-z]{6,}$"

# # Wzorzec wymaga co najmniej 8 znaków z zestawu liter, cyfr i podkreślenia od początku do końca napisu
# password_pattern = r"^[A-Za-z0-9_]{8,}$"

# # Sprawdzamy, czy wpisane wartości pasują w całości do określonych wzorców
# username_match = re.match(username_pattern, username)
# password_match = re.match(password_pattern, password)

# # Wypisujemy wynik weryfikacji po polsku w zależności od dopasowania obu wzorców
# if username_match and password_match:
#     print("Nazwa użytkownika oraz hasło są poprawne.")
# else:
#     print("Nazwa użytkownika lub hasło nie spełnia wymagań.")
