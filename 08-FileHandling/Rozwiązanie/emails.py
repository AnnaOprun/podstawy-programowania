import re  # moduł wyrażeń regularnych

EMAIL_FILE = "email.txt"  # nazwa pliku wejściowego z surową wiadomością e-mail

# Pomocnicza funkcja wczytująca całą zawartość pliku email.txt z kodowaniem UTF-8
def _read_email_content():
    with open(EMAIL_FILE, "r", encoding="utf-8") as file:  # otwieramy plik z kodowaniem UTF-8 do odczytu
        return file.read()  # zwracamy pełny tekst wiadomości jako jeden napis

# Funkcja zwracająca adres e-mail nadawcy z nagłówka From
def email_sender():
    content = _read_email_content()  # pobieramy treść wiadomości e-mail
    match = re.search(r"(?m)^From:.*?([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})", content)  # szukamy adresu w linii From
    return match.group(1) if match else ""  # zwracamy dopasowany adres lub pusty napis, gdy brak dopasowania

# Funkcja zwracająca adres e-mail odbiorcy z nagłówka To
def email_recipient():
    content = _read_email_content()  # pobieramy treść wiadomości e-mail
    match = re.search(r"(?m)^To:.*?([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,})", content)  # szukamy adresu w linii To
    return match.group(1) if match else ""  # zwracamy dopasowany adres lub pusty napis, gdy brak dopasowania

# Funkcja zwracająca temat wiadomości e-mail z nagłówka Subject
def email_subject():
    content = _read_email_content()  # pobieramy treść wiadomości e-mail
    match = re.search(r"(?m)^Subject:\s*(.*)$", content)  # pobieramy resztę linii po słowie Subject:
    return match.group(1).strip() if match else ""  # usuwamy zbędne białe znaki z brzegów tematu

# Funkcja zwracająca treść wiadomości e-mail znajdującą się po pustej linii oddzielającej nagłówki
def email_body():
    content = _read_email_content()  # pobieramy treść wiadomości e-mail
    match = re.search(r"\r?\n\r?\n(.*)$", content, re.DOTALL)  # dopasowujemy wszystko po pustym wierszu (także wiele linii)
    return match.group(1).strip() if match else ""  # zwracamy treść wiadomości bez skrajnych pustych znaków