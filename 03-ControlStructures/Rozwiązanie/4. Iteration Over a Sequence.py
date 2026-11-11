# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...
# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Pętla for służy do iteracji po sekwencji i wykonywania bloku kodu dla każdego elementu w tej sekwencji.
# for item in sequence:
#     # blok kodu do wykonania

# city = 'Krakow'
# for char in city:
#     print(char)

# for i in range(5):
#     print(i)

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Poniższy program wypisuje zdanie „Practice makes perfect!” cztery razy. zmodyfikuj program, aby wypisywał ten tekst sześć razy. Następnie uruchom program.

# for i in range(6):
#     print('Practice makes perfect!')

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który wypisuje nazwę uczelni, na której studiujesz, z dodatkową spacją między znakami (dodaj spację pomiędzy każdym znakiem), np. book -> b o o k.

# university = 'Krakow University of Economics'
# university_expanded = ''    # Tworzymy pustą zmienną, do której będziemy dopisywać znaki ze spacjami

# for char in university:     # Pętla "for" przechodzi po kolei przez każdy pojedynczy znak w zmiennej "university"
#     university_expanded = university_expanded + char + ' ' # Do dotychczasowego ciągu dopisujemy aktualny znak oraz dodatkową spację

# print(university)
# print(university_expanded)

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# Szyfr Cezara (znany również jako kod Cezara) to jedna z najprostszych i najstarszych technik szyfrowania. Nazwa pochodzi od Juliusza Cezara, 
# który rzekomo używał go do tajnej komunikacji ze swoimi generałami. Szyfr ten polega na przesunięciu każdej litery w tekście o określoną liczbę pozycji w alfabecie.
# Napisz program, który szyfruje tekst za pomocą Szyfru Cezara, przesuwając każdą literę w alfabecie o jedną pozycję w prawo.

# plain_text = 'The early bird catches the worm'
# encrypted_text = ''

# for char in plain_text:
   
#     code = ord(char)    # Odczytanie kodu ASCII znaku za pomocą funkcji ord()
#     code = code + 1     # Dodanie jedynki do kodu znaku (przesunięcie o 1 w prawo)
    
#     encrypted_char = chr(code)   # Zamiana nowego kodu z powrotem na znak za pomocą funkcji chr()
#     encrypted_text = encrypted_text + encrypted_char # Dodanie zaszyfrowanego znaku do tekstu zaszyfrowanego

# print(f"Tekst jawny: {plain_text}")
# print(f"Tekst zaszyfrowany: {encrypted_text}")

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Poniższy program oblicza sumę liczb całkowitych w przedziale [1,5]. Wprowadź w programie następujące zmiany: zsumuj liczby od 5 do 10 | użyj operatora += w wyrażeniu sum=sum+i

# sum = 0

# for i in range(5, 11): # range(5, 11) generuje liczby od 5 do 10 włącznie (główny koniec jest pomijany)
#     sum += i

# print(f"Suma wynosi {sum}")

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza sumę liczb parzystych w przedziale [1,10].

# sum = 0

# for i in range(1, 11):
#     if not i % 2 == 0:
#         continue
#     sum += i

# print(f"Suma liczb parzystych w przedziale <1,10> wynosi {sum}")

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza wartości następujących ułamków: 1/2, 1/3, ..., 1/10.

# for i in range(1, 11):
#     print(f"1/{i} = {1 / i}")