# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...
# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# W Pythonie konstrukcja __name__ == "__main__" jest powszechnie używana do sterowania wykonywaniem kodu w sytuacji, gdy plik Pythona jest uruchamiany bezpośrednio, 
# w odróżnieniu od sytuacji, gdy jest importowany jako moduł w innym pliku.
# Blok if __name__ == "__main__": zapewnia, że określone fragmenty kodu są wykonywane tylko wtedy, gdy plik jest uruchamiany bezpośrednio, a nie wtedy, gdy jest importowany. 
# Spójrz na poniższy przykład:

# def add(a, b):
#     return a + b    # Zwraca sumę dwóch liczb

# def subtract(a, b):
#     return a - b    # Zwraca różnicę dwóch liczb

# if __name__ == "__main__":  # Ten blok wykona się tylko wtedy, gdy skrypt jest uruchamiany bezpośrednio
#     x = 10
#     y = 5
#     print(f"Dodawanie: {add(x, y)}")
#     print(f"Odejmowanie: {subtract(x, y)}")

# Spróbuj używać tej konstrukcji w swoich przyszłych zadaniach, w których definiujesz funkcje.
#  Aby przetestować funkcję, umieść wywołania funkcji w bloku if __name__ == "__main__":, tak jak w powyższym przykładzie.   
# Jeśli chcesz, aby Twoje programy wyglądały naprawdę profesjonalnie, możesz również zdefiniować funkcję main(). 
# Definiowanie funkcji main() w większych lub bardziej złożonych programach jest uznawane za dobrą praktykę, ponieważ poprawia organizację i czytelność kodu. 
# To naprawdę bardzo proste. Zobacz przykład poniżej:   

# def add(a, b):
#     return a + b    # Zwraca sumę dwóch liczb

# def subtract(a, b):
#     return a - b    # Zwraca różnicę dwóch liczb

# def main():     # Ten blok wykona się tylko wtedy, gdy skrypt jest uruchamiany bezpośrednio
#     x = 10
#     y = 5
#     print(f"Dodawanie: {add(x, y)}")
#     print(f"Odejmowanie: {subtract(x, y)}")


# if __name__ == "__main__":
#     main()

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Każdy miesiąc roku kalendarzowego może być wyrażony swoją nazwą albo numerem wskazującym pozycję miesiąca w roku. 
# W osobnym module zdefiniuj funkcję month(n), która zwraca nazwę miesiąca na podstawie numeru miesiąca (wartości od 1 do 12). 
# Następnie napisz program wypisujący nazwę miesiąca o numerze 7. Zaimportuj moduł ze stworzoną funkcją

# Plik `months.py`

# import months # Program główny importujący moduł months i wypisujący nazwę miesiąca nr 7 oraz wczytanego numeru

# def main():
#     month_num_7 = 7
#     print(f"Nazwa miesiąca {month_num_7} to {months.month(month_num_7)}")

#     # Wczytanie numeru miesiąca z klawiatury i wypisanie jego nazwy jak w przykładzie
#     user_month = int(input("Podaj numer miesiąca: "))
#     print(f"Nazwa   miesiąca {user_month} to {months.month(user_month)}")

# if __name__ == "__main__":
#     main()

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Napisz program, który oblicza, ile razy podana litera występuje w dowolnym tekście. 
# Następnie utwórz program i sprawdź, ile razy litera 'e' występuje w poniższym tekście. 
# W osobnym module zdefiniuj funkcję wykonującą obliczenia.

# Plik `text_tools.py`

# import text_tools

# def main():
#     # Tekst analizowany w przykładzie z zadania
#     text = "You never get a second chance to make a first impression"
#     target_letter = "e"

#     # Wywołujemy funkcję z modułu text_tools
#     occurrences = text_tools.count_letter(text, target_letter)

#     # Wypisujemy tekst oraz wynik zliczania
#     print(text)
#     print(f"Liczba wystąpień litery '{target_letter}': {occurrences}")

# if __name__ == "__main__":
#     main()

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# W osobnym module zdefiniuj funkcję, która sprawdza, czy liczba mieści się w przedziale <x, y>. Funkcja zwraca wartość logiczną (True lub False).

# Plik `ranges.py`

# import ranges

# def main():
    
#     number = int(input("Podaj liczbę: "))   # Wczytujemy liczbę od użytkownika oraz definiujemy granice przedziału <2, 15>
#     x = 2
#     y = 15

#     is_inside = ranges.in_range(number, x, y)   # Wywołujemy funkcję zwracającą wartość logiczną True lub False

#     # Zamieniamy wartość logiczną na 'yes' lub 'no' zgodnie z przykładowym wynikiem
#     answer = "yes" if is_inside else "no"
#     print(f"Liczba {number} w przedziale <{x},{y}>: {answer}")

# if __name__ == "__main__":
#     main()

# ZADANIE 6________________________________________________________________________________________________________________________________________________________________________
# Numer karty kredytowej składa się z 16 cyfr. W osobnym module zdefiniuj funkcję hide(card_number), która maskuje numer karty. 
# Funkcja zwraca napis (ciąg znaków), w którym widoczne są tylko pierwsze dwie i ostatnie cztery cyfry numeru karty. Pozostałe cyfry numeru karty są zastąpione gwiazdką.
# Następnie utwórz program, który maskuje niektóre cyfry karty kredytowej. Zaimportuj moduł ze stworzoną funkcją. Na koniec wypisz numer karty kredytowej.

# Plik `card.py`

# import card

# def main():
#     card_number = "5212312312312390"
#     masked_number = card.hide(card_number)
#     print(f'f("{card_number}") returns "{masked_number}"')

# if __name__ == "__main__":
#     main()

# ZADANIE 7________________________________________________________________________________________________________________________________________________________________________
# Dwójkowy system liczbowy używa dwóch symboli do przedstawiania liczby: 0 oraz 1. Zdefiniuj funkcję f(binary_number), 
# która zwraca True, jeśli podany napis z cyfr jest poprawną liczbą binarną, albo False w przeciwnym razie.

# def f(binary_number):
    
#     if binary_number == "": # Pusty napis nie jest poprawną liczbą binarną
#         return False

#     for char in binary_number:  # Sprawdzamy każdy znak po kolei – wszystkie muszą być równe '0' lub '1'
#         if char != "0" and char != "1":
#             return False
#     return True

# def main():
#     test_1 = "101101"
#     test_2 = "1311a10100"
#     print(f'f("{test_1}") returns {f(test_1)}')
#     print(f'f("{test_2}") returns {f(test_2)}')

# if __name__ == "__main__":
#     main()

# ZADANIE 8________________________________________________________________________________________________________________________________________________________________________
# Automat sprzedający przyjmuje monety o nominałach 1, 2 oraz 5 zł. 
# Zdefiniuj funkcję f(amount_to_pay), która zwraca minimalną liczbę monet, jakich można użyć do opłacenia zakupionego produktu.

# def f(amount_to_pay):

#     # Zaczynamy od największego nominału (5 zł), aby użyć jak najmniej monet
#     coins_5 = amount_to_pay // 5    # mówi nam, ile pięciozłotówek zmieści się w całej kwocie
#     remaining = amount_to_pay % 5   # pokazuje, ile złotych zostało jeszcze do zapłacenia
#     # Przykładowo dla kwoty 23 zł mamy 23 // 5 = 4 monety po 5 zł (co daje 20 zł) i zostaje nam 23 % 5 = 3 zł

#     # Z pozostałej kwoty bierzemy jak najwięcej monet 2 zł
#     coins_2 = remaining // 2
#     remaining = remaining % 2

#     # Resztę kwoty (0 lub 1 zł) pokrywamy monetami 1 zł
#     coins_1 = remaining // 1

#     return coins_5 + coins_2 + coins_1

# def main():
#     print(f"f(23) returns {f(23)}")
#     print(f"f(8) returns {f(8)}")
#     print(f"f(2) returns {f(2)}")
#     print(f"f(0) returns {f(0)}")

# if __name__ == "__main__":
#     main()

# ZADANIE 9________________________________________________________________________________________________________________________________________________________________________
# Utwórz funkcję f(number, even), która oblicza sumę cyfr liczby. Gdy wartość parametru even wynosi True, funkcja zwraca sumę cyfr parzystych. 
# Gdy wartość parametru even wynosi False, funkcja zwraca sumę cyfr nieparzystych.

# def f(number, even):
#     total = 0

#     # Przechodzimy po każdej cyfrze liczby zamienionej na napis
#     for char in str(number):
#         digit = int(char)

#         # Sprawdzamy parzystość cyfry oraz decydujemy, czy dodać ją do sumy
#         if even and digit % 2 == 0:
#             total += digit
#         elif not even and digit % 2 != 0:
#             total += digit

#     return total

# def main():
#     print(f"f(3124,True) returns {f(3124, True)}")
#     print(f"f(3124,False) returns {f(3124, False)}")
#     print(f"f(20576,False) returns {f(20576, False)}")
#     print(f"f(20576,True) returns {f(20576, True)}")
#     print(f"f(13115,True) returns {f(13115, True)}")

# if __name__ == "__main__":
#     main()

# ZADANIE 10________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję f(x,y), która zwraca liczbę ujemnych liczb parzystych w przedziale <x,y>.

# def f(x, y):
#     count = 0

#     # Przeglądamy wszystkie liczby całkowite od x do y włącznie (stąd y + 1 w range)
#     for number in range(x, y + 1):
#         # Liczba musi być jednocześnie ujemna (< 0) oraz parzysta (% 2 == 0)
#         if number < 0 and number % 2 == 0:
#             count += 1
#     return count

# def main():
#     print(f"f(-7,8) returns {f(-7, 8)}")
#     print(f"f(-1,11) returns {f(-1, 11)}")

# if __name__ == "__main__":
#     main()

# ZADANIE 11________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję f(n1,n2,n3), która zwraca True, jeśli co najmniej jedna z liczb n1,n2,n3 jest ujemna, albo False w przeciwnym razie.

# def f(n1, n2, n3):
#     # Zwraca True, jeśli choć jedna z trzech liczb jest mniejsza od zera
#     return n1 < 0 or n2 < 0 or n3 < 0

# def main():
#     print(f"f(11,6,-4) returns {f(11, 6, -4)}")
#     print(f"f(5,4,14) returns {f(5, 4, 14)}")

# if __name__ == "__main__":
#     main()

# ZADANIE 12________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję f(n), która zwraca napis złożony z n gwiazdek oddzielonych znakiem ukośnika /.

# def f(n):
#     # Jeśli n jest mniejsze lub równe zero, zwracamy pusty napis
#     if n <= 0:
#         return ""

#     # Tworzymy n gwiazdek i łączymy je znakiem '/'
#     return "/".join(["*"] * n) 
#     # Dzięki temu nie musimy martwić się o żaden zbędny ukośnik na początku ani na końcu napisu, bo metoda join wstawia separator wyłącznie między kolejne elementy/

# def main():
#     print(f'f(4) returns "{f(4)}"')
#     print(f'f(1) returns "{f(1)}"')

# if __name__ == "__main__":
#     main()

# ZADANIE 13________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję f(n), która zwraca liczby od 1 do n w postaci jednego napisu.

# def f(n):
#     result = ""

#     # Przechodzimy po liczbach od 1 do n włącznie i doklejamy każdą jako tekst
#     for number in range(1, n + 1):
#         result += str(number)
#     return result

# def main():
#     print(f'f(11) returns "{f(11)}"')
#     print(f'f(4) returns "{f(4)}"')

# if __name__ == "__main__":
#     main()

# ZADANIE 14________________________________________________________________________________________________________________________________________________________________________
# Podane są dwie liczby oraz operator. Zdefiniuj funkcję f(number1,number2,operator), która zwraca wynik działania arytmetycznego. Dostępne operatory to +, -, *, %, **

# def f(number1, number2, operator):
#     # Wybieramy odpowiednie działanie arytmetyczne w zależności od przekazanego operatora
#     if operator == "+":
#         return number1 + number2
#     elif operator == "-":
#         return number1 - number2
#     elif operator == "*":
#         return number1 * number2
#     elif operator == "%":
#         return number1 % number2
#     elif operator == "**":
#         return number1 ** number2
#     else:
#         return None

# def main():
#     print(f'f(2,3, "+") returns {f(2, 3, "+")}')
#     print(f'f(2,3, "%") returns {f(2, 3, "%")}')
#     print(f'f(2,3, "**") returns {f(2, 3, "**")}')
#     print(f'f(2,3, "*") returns {f(2, 3, "*")}')
#     print(f'f(2,3, "-") returns {f(2, 3, "-")}')

# if __name__ == "__main__":
#     main()

# ZADANIE 15________________________________________________________________________________________________________________________________________________________________________
# Urządzenie w drzwiach rejestruje osoby wchodzące do pokoju i wychodzące z niego. Znak + oznacza osobę wchodzącą do pokoju, a znak - oznacza osobę wychodzącą z pokoju. 
# Zdefiniuj funkcję f(detector), która zwraca True, jeśli w pokoju przebywały w tym samym czasie co najmniej 3 osoby, albo False w przeciwnym razie.

# def f(detector):
#     # Aktualna liczba osób przebywających w pokoju w danym momencie
#     people_in_room = 0

#     # Śledzimy kolejne zdarzenia wejścia ('+') i wyjścia ('-')
#     for event in detector:
#         if event == "+":
#             people_in_room += 1
#         elif event == "-":
#             people_in_room -= 1

#         if people_in_room >= 3:
#             return True

#     return False

# def main():
#     print(f'f("+-+++-+---") returns {f("+-+++-+---")}')
#     print(f'f("+--+-+-+-") returns {f("+--+-+-+-")}')
#     print(f'f("+-++-+-") returns {f("+-++-+-")}')
#     print(f'f("+-++-+-+---") returns {f("+-++-+-+---")}')

# if __name__ == "__main__":
#     main()

# ZADANIE 16________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję f(n), która zwraca n-tą wartość ciągu Fibonacciego. 
# Ciąg jest zdefiniowany w następujący sposób: pierwsza wartość ciągu to 0, druga wartość to 1. Każda kolejna wartość jest sumą dwóch poprzednich.

# def f(n):
#     # Pierwszy wyraz ciągu (n == 1) to 0, a drugi (n == 2) to 1
#     if n <= 0:
#         return None
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1

#     # Przechowujemy dwa poprzednie wyrazy ciągu
#     prev2 = 0
#     prev1 = 1

#     # Obliczamy kolejne wyrazy od trzeciego aż do n-tego
#     for _ in range(3, n + 1):
#         current = prev1 + prev2
#         prev2 = prev1
#         prev1 = current

#     return prev1

# def main():
#     print(f"f(5) returns {f(5)}")
#     print(f"f(9) returns {f(9)}")

# if __name__ == "__main__":
#     main()

# ZADANIE 17________________________________________________________________________________________________________________________________________________________________________
# Palindrom to wyrażenie, które brzmi tak samo czytane od tyłu. Zdefiniuj funkcję f(palindrome), która zwraca True, jeśli wyrażenie jest palindromem, albo False w przeciwnym razie.

# def f(palindrome):
#     # Odwracamy napis za pomocą wycinka [::-1] i porównujemy z oryginałem
#     return palindrome == palindrome[::-1]

# def main():
#     print(f'f("radar") returns {f("radar")}')
#     print(f'f("12-11-21") returns {f("12-11-21")}')
#     print(f'f("book") returns {f("book")}')

# if __name__ == "__main__":
#     main()

# ZADANIE 18________________________________________________________________________________________________________________________________________________________________________
# Zdanie to uporządkowana grupa słów oddzielonych spacjami. Zdefiniuj funkcję f(sentence), która zwraca zdanie z usuniętymi spacjami.

# def f(sentence):
#     # Zamieniamy każdą spację na pusty napis
#     return sentence.replace(" ", "")

# def main():
#     s1 = "integrated development environment"
#     s2 = "A programming language is a system of notation for writing computer programs"
#     print(f'f("{s1}") returns "{f(s1)}"')
#     print(f'f("{s2}") returns "{f(s2)}"')

# if __name__ == "__main__":
#     main()

# ZADANIE 19________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję f(number), która zwraca sumę powtarzających się cyfr w liczbie.

# def f(number):
#     digits = str(number)
#     total = 0

#     # Jeśli dana cyfra występuje w napisie więcej niż raz, wliczamy ją do sumy
#     for digit in digits:
#         if digits.count(digit) > 1:
#             total += int(digit)
#     return total

# def main():
#     print(f"f(1027) returns {f(1027)}")
#     print(f"f(230335) returns {f(230335)}")
#     print(f"f(513553007) returns {f(513553007)}")

# if __name__ == "__main__":
#     main()

# ZADANIE 20________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję f(n), która zwraca n-tą liczbę pierwszą. Liczba pierwsza to liczba naturalna większa od 1, podzielna przez 1 oraz samą siebie.

# def is_prime(num):
#     # Liczby mniejsze niż 2 (0, 1 oraz ujemne) nie są liczbami pierwszymi
#     if num < 2:
#         return False

#     # Sprawdzamy, czy istnieje jakikolwiek dzielnik od 2 aż do pierwiastka z num
#     for divisor in range(2, int(num ** 0.5) + 1):
#         if num % divisor == 0:
#             return False
#     return True

# def f(n):
#     # Jeśli n jest niepoprawne (np. 0 lub liczba ujemna), zwracamy None
#     if n <= 0:
#         return None

#     count = 0
#     candidate = 1

#     # Przechodzimy przez kolejne liczby całkowite i zliczamy liczby pierwsze
#     while count < n:
#         candidate += 1
#         if is_prime(candidate):
#             count += 1

#     return candidate

# def main():
#     print(f"f(1) returns {f(1)}")
#     print(f"f(5) returns {f(5)}")

# if __name__ == "__main__":
#     main()

# ZADANIE 21________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję f(number1,number2,number3), która zwraca różnicę między największą a najmniejszą z liczb.

# def f(number1, number2, number3):
#     # Wyznaczamy największą i najmniejszą z trzech podanych liczb
#     largest = max(number1, number2, number3)
#     smallest = min(number1, number2, number3)

#     # Zwracamy różnicę (rozpiętość) między nimi
#     return largest - smallest

# def main():
#     print(f"f(7,4,9) returns {f(7, 4, 9)}")
#     print(f"f(2,12,8) returns {f(2, 12, 8)}")

# if __name__ == "__main__":
#     main()

# ZADANIE 22________________________________________________________________________________________________________________________________________________________________________
# Tekst zawiera dowolną liczbę słów. Zdefiniuj funkcję f(name), która zwraca akronim (pierwsze litery wszystkich słów).

# def f(name):
#     # Dzielimy napis na osobne słowa po spacjach
#     words = name.split()
#     acronym = ""

#     # Bierzemy pierwszy znak każdego słowa i doklejamy do wyniku
#     for word in words:
#         acronym += word[0]
#     return acronym

# def main():
#     print(f'f("Internet of Things") returns "{f("Internet of Things")}"')
#     print(f'f("For Your Information") returns "{f("For Your Information")}"')
#     print(f'f("Python") returns "{f("Python")}"')

# if __name__ == "__main__":
#     main()

# ZADANIE 23________________________________________________________________________________________________________________________________________________________________________
# Poprawne hasło powinno składać się z co najmniej sześciu znaków oraz każdy znak powinien występować w haśle tylko raz. Zdefiniuj funkcję f(password), która zwraca True, jeśli hasło jest poprawne, albo False w przeciwnym razie.

# def f(password):
#     # Warunek 1: hasło musi mieć co najmniej 6 znaków
#     if len(password) < 6:
#         return False

#     # Warunek 2: każdy znak w haśle może wystąpić tylko jeden raz
#     for char in password:
#         if password.count(char) > 1:
#             return False

#     return True

# def main():
#     print(f'f("ax15") returns {f("ax15")}')
#     print(f'f("book123") returns {f("book123")}')
#     print(f'f("A2water3") returns {f("A2water3")}')
#     print(f'f("qwerty") returns {f("qwerty")}')
#     print(f'f("") returns {f("")}')

# if __name__ == "__main__":
#     main()

# ZADANIE 24________________________________________________________________________________________________________________________________________________________________________
# Wyrażenie zawiera operatory dodawania i odejmowania liczb jednocyfrowych. Zdefiniuj funkcję f(expression), która zwraca wartość tego wyrażenia.

# def f(expression):
#     # Jeśli wyrażenie jest puste, zwracamy 0
#     if expression == "":
#         return 0

#     # Pierwszy znak to zawsze początkowa cyfra
#     result = int(expression[0])

#     # Przechodzimy przez kolejne pary: znak działania ('+' lub '-') oraz kolejna cyfra
#     for i in range(1, len(expression), 2):
#         operator = expression[i]
#         digit = int(expression[i + 1])

#         if operator == "+":
#             result += digit
#         elif operator == "-":
#             result -= digit

#     return result

# def main():
#     print(f'f("2+3") returns {f("2+3")}')
#     print(f'f("3+8+1") returns {f("3+8+1")}')
#     print(f'f("2+3-4+5-0") returns {f("2+3-4+5-0")}')

# if __name__ == "__main__":
#     main()

# ZADANIE 25________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję f(x,y), która zwraca sumę liczb z przedziału <x,y> podzielnych całkowicie przez 2 i 3 oraz niepodzielnych przez 4

# def f(x, y):
#     total = 0

#     # Przeglądamy wszystkie liczby całkowite od x do y włącznie (stąd y + 1 w range)
#     for number in range(x, y + 1):
#         # Liczba musi być podzielna przez 2 i przez 3, a jednocześnie niepodzielna przez 4
#         if number % 2 == 0 and number % 3 == 0 and number % 4 != 0:
#             total += number
#     return total

# def main():
#     print(f"f(1,20) returns {f(1, 20)}")
#     print(f"f(10,30) returns {f(10, 30)}")

# if __name__ == "__main__":
#     main()

# ZADANIE 26________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję f(text), która zwraca podany tekst ze wszystkimi znakami oddzielonymi znakiem łącznika (-).

# def f(text):
#     # Łączymy kolejne znaki napisu za pomocą łącznika '-'
#     return "-".join(text)

# def main():
#     print(f'f("Univesity") returns "{f("Univesity")}"')
#     print(f'f("UE") returns "{f("UE")}"')
#     print(f'f("x") returns "{f("x")}"')
#     print(f'f("") returns "{f("")}"')

# if __name__ == "__main__":
#     main()

# ZADANIE 27________________________________________________________________________________________________________________________________________________________________________
# Produkty są oznaczane specjalnym kodem składającym się z 3 cyfr oraz czwartej cyfry kontrolnej. 
# Czwarta cyfra jest wyznaczana poprzez obliczenie reszty z dzielenia sumy pierwszych trzech cyfr przez 7. 
# Zdefiniuj funkcję f(product_code), która zwraca True, jeśli kod produktu jest poprawny, albo False w przeciwnym razie.

# def f(product_code):
#     # Pobieramy pierwsze trzy cyfry oraz czwartą cyfrę kontrolną jako liczby całkowite
#     first_digit = int(product_code[0])
#     second_digit = int(product_code[1])
#     third_digit = int(product_code[2])
#     control_digit = int(product_code[3])

#     # Suma pierwszych trzech cyfr modulo 7 powinna być równa cyfrze kontrolnej
#     expected_control = (first_digit + second_digit + third_digit) % 7

#     return expected_control == control_digit

# def main():
#     print(f'f("1082") returns {f("1082")}')
#     print(f'f("2035") returns {f("2035")}')
#     print(f'f("1114") returns {f("1114")}')
#     print(f'f("7071") returns {f("7071")}')

# if __name__ == "__main__":
#     main()

# ZADANIE 28________________________________________________________________________________________________________________________________________________________________________
# Ciąg cyfr zawiera liczbę oczek wyrzuconych kostką do gry. Zdefiniuj funkcję f(dice), która zwraca liczbę określającą oczka wyrzucone najwięcej razy pod rząd.

# def f(dice):
#     if not dice:
#         return None

#     best_digit = dice[0]
#     best_streak = 1

#     current_digit = dice[0]
#     current_streak = 1

#     # Przechodzimy przez kolejne znaki począwszy od drugiego
#     for digit in dice[1:]:
#         if digit == current_digit:
#             current_streak += 1
#         else:
#             current_digit = digit
#             current_streak = 1

#         # Aktualizujemy rekord, jeśli bieżąca seria jest dłuższa od dotychczasowej najlepszej
#         if current_streak > best_streak:
#             best_streak = current_streak
#             best_digit = current_digit
#     return int(best_digit)

# def main():
#     print(f'f("5233165554211") returns {f("5233165554211")}')
#     print(f'f("2133") returns {f("2133")}')

# if __name__ == "__main__":
#     main()

# ZADANIE 29________________________________________________________________________________________________________________________________________________________________________
# Poniższa funkcja oblicza silnię rekurencyjnie. Spróbuj przeanalizować tę funkcję. 
# Czy rozumiesz, jak ona działa? Następnie napisz program i użyj tej funkcji, aby obliczyć wartość silni dla n = 5.

# def factorial(n):
#     # Przypadek bazowy rekurencji: silnia z 0 oraz z 1 wynosi 1
#     if n == 0 or n == 1:
#         return 1

#     # Krok rekurencyjny: n! = n * (n - 1)!
#     if n > 1:
#         return n * factorial(n - 1)

# def main():
#     n = 5
#     result = factorial(n)
#     print(f"Factorial of {n} is {result}")

# if __name__ == "__main__":
#     main()

# ZADANIE 30________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję sum_natural(n), która dla podanej liczby naturalnej n oblicza sumę wszystkich liczb naturalnych od 1 do n. 
# Zastosuj rekurencję. Następnie utwórz program, który oblicza sumę liczb naturalnych w przedziale <1,10>.

# def sum_natural(n):
#     # Przypadek bazowy: dla n == 1 suma liczb od 1 do 1 wynosi po prostu 1
#     if n <= 1:
#         return n

#     # Krok rekurencyjny: suma liczb od 1 do n to n plus suma liczb od 1 do (n - 1)
#     return n + sum_natural(n - 1) # suma wszystkich liczb od 1 do n to po prostu bieżące n dodane do sumy wszystkich liczb od 1 do n - 1

# def main():
#     n = 10
#     total = sum_natural(n)
#     print(f"Sum of natural numbers in <1,{n}> is {total}")

# if __name__ == "__main__":
#     main()

# ZADANIE 31________________________________________________________________________________________________________________________________________________________________________
# Zdefiniuj funkcję power(x, n), która oblicza x**n. Zastosuj rekurencję. Następnie oblicz 5**3.

# def power(x, n):
#     # Przypadek bazowy: dowolna liczba podniesiona do potęgi 0 wynosi 1
#     if n == 0:
#         return 1

#     # Krok rekurencyjny: x^n = x * x^(n - 1)
#     return x * power(x, n - 1)

# def main():
#     base = 5
#     exponent = 3
#     result = power(base, exponent)
#     print(f"{base}^{exponent} = {result}")

# if __name__ == "__main__":
#     main()