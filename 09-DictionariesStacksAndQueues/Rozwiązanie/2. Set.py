# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
# Zbiór to nieuporządkowana kolekcja unikalnych elementów. Zbiory są przydatne wtedy, gdy chcesz przechowywać kolekcję elementów i mieć pewność, że nie ma w niej duplikatów. 
# W przeciwieństwie do list czy tablic zbiory nie zachowują kolejności elementów i nie można odwoływać się do ich elementów po indeksie. 
# Obsługują szybkie sprawdzanie przynależności, sumę, część wspólną, różnicę oraz inne operacje na zbiorach.

# Przykładowe operacje na zbiorach w Pythonie: część wspólna, suma, różnica, różnica symetryczna oraz podzbiór

# set_a = {1, 2, 3, 4}  # pierwszy zbiór liczb całkowitych
# set_b = {3, 4, 5, 6}  # drugi zbiór liczb całkowitych

# print("Część wspólna (A & B):", set_a & set_b)  # elementy występujące w obu zbiorach: {3, 4}
# print("Suma (A | B):", set_a | set_b)  # wszystkie unikalne elementy z obu zbiorów: {1, 2, 3, 4, 5, 6}
# print("Różnica (A - B):", set_a - set_b)  # elementy z set_a, których nie ma w set_b: {1, 2}
# print("Różnica symetryczna (A ^ B):", set_a ^ set_b)  # elementy występujące tylko w jednym ze zbiorów: {1, 2, 5, 6}

# small_set = {1, 2}  # zbiór będący podzbiorem set_a
# print("Czy small_set jest podzbiorem set_a?", small_set.issubset(set_a))  # zwraca True

# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Poniższy program usuwa zduplikowane adresy e-mail. Uzupełnij i uruchom program.

# emails = ["john@example.com", "jane@example.com", "john@example.com", "alex@example.com"]  # lista zawierająca powtarzający się adres
# unique_emails = set(emails)  # konwertujemy listę na zbiór, aby automatycznie usunąć duplikaty

# print("Unikalne adresy e-mail:")
# for email in unique_emails:  # wypisujemy każdy unikalny adres e-mail po polsku
#     print(email)

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Poniższy program wskazuje studentów, którzy są nieobecni. Uzupełnij i uruchom program.

# all_students = {"Alice", "John", "Sara", "Bob"}  # zbiór wszystkich studentów
# attended_students = {"Alice", "Bob"}  # zbiór studentów obecnych na zajęciach

# absent_students = all_students - attended_students  # elementy z all_students, których brakuje w attended_students

# print("Nieobecni studenci:")
# for student in absent_students:  # wypisujemy każdego nieobecnego studenta po polsku
#     print(student)

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Poniższy program wyszukuje spam wśród odebranych wiadomości e-mail. Uzupełnij program tak, aby wyświetlał te odebrane adresy e-mail, które znajdują się na liście spamu.

# emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}  # odebrane adresy e-mail
# spam_list = {"spam1@example.com", "spam2@example.com"}  # znane adresy spamowe

# spam_emails = emails_received & spam_list  # część wspólna: adresy obecne jednocześnie w obu zbiorach

# print("Wykryte adresy spamowe:")
# for email in spam_emails:  # wypisujemy każdy dopasowany adres po polsku
#     print(email)

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Dwie listy kontaktów pobrane z bazy danych zawierają adresy e-mail. Napisz program, który łączy te listy i jednocześnie usuwa duplikaty.

# contacts_A = {"john@example.com", "alice@example.com", "bob@example.com"}  # pierwszy zbiór adresów e-mail
# contacts_B = {"bob@example.com", "michael@example.com", "sara@example.com"}  # drugi zbiór adresów e-mail

# merged_contacts = contacts_A | contacts_B  # suma zbiorów: łączy oba zbiory bez powtarzania 'bob@example.com'

# print("Połączone unikalne kontakty:")
# for contact in merged_contacts:  # wypisujemy każdy unikalny adres e-mail po polsku
#     print(contact)

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# W systemie operacyjnym każdy użytkownik ma pewne uprawnienia. Użytkownik chce wykonać określoną akcję, która wymaga konkretnych uprawnień. 
# Napisz program, który sprawdza, czy użytkownik posiada wymagane uprawnienia.

# required_permissions = {"read", "write", "execute"}  # zbiór uprawnień wymaganych do wykonania akcji
# user_permissions = {"read", "write"}  # zbiór uprawnień posiadanych przez użytkownika

# has_permissions = required_permissions.issubset(user_permissions)  # sprawdza, czy wymagane uprawnienia mieszczą się w uprawnieniach użytkownika

# if has_permissions:  # wypisujemy czytelny komunikat po polsku w zależności od wyniku sprawdzenia
#     print("Użytkownik posiada wszystkie wymagane uprawnienia.")
# else:
#     print("Użytkownik nie posiada wszystkich wymaganych uprawnień.")