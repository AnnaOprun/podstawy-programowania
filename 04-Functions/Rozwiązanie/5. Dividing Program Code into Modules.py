# ZADANIE 1________________________________________________________________________________________________________________________________________________________________________
#   ...
# ZADANIE 2________________________________________________________________________________________________________________________________________________________________________
# Plik converters.py definiuje dwie funkcje do przeliczania jednostek długości (cm-->m oraz m-->cm). 
# Plik test_converters.py używa tych funkcji do przeliczania wartości.   
# Zdefiniuj w pliku converters.py następujące funkcje, które pozwalają:
                            # przeliczać centymetry na cale   
                            # przeliczać stopy i cale na centymetry   
# Następnie uzupełnij główny program, aby przetestować dodane funkcje.   

# ZADANIE 3________________________________________________________________________________________________________________________________________________________________________
# Jak pamiętasz, funkcja input() pozwala wczytać z klawiatury wyłącznie napis (string). 
# W module keyboard.py zdefiniuj własne funkcje, które pozwalają wczytywać inne typy danych z klawiatury:   
#                                input_string(), która zwraca napis wprowadzony z klawiatury   
#                                input_integer(), która zwraca liczbę całkowitą wprowadzoną z klawiatury   
#                                input_real(), która zwraca liczbę rzeczywistą wprowadzoną z klawiatury   
#                                input_boolean(), która zwraca wartość logiczną w zależności od wciśniętego klawisza y/n   
# Następnie napisz program, który pozwala wprowadzić i wypisać dane pracownika. Ze względu na ochronę danych osobowych możesz decydować, 
# czy informacja o wynagrodzeniu pracownika zostanie wypisana.

# import keyboard  # własny moduł zdefiniowany w tym samym folderze

# # Wczytanie danych pracownika z klawiatury
# first_name = keyboard.input_string("Podaj imię: ")
# last_name = keyboard.input_string("Podaj nazwisko: ")
# age = keyboard.input_integer("Podaj wiek: ")
# salary = keyboard.input_real("Podaj wynagrodzenie: ")
# is_salary_hidden = keyboard.input_boolean("Ukryć wynagrodzenie? (y/n): ") #zwraca True -> y | False -> n

# # Wypisanie rekordu pracownika
# print("REKORD DANYCH")
# print("=============")
# print("Imię:", first_name)
# print("Nazwisko:", last_name)
# print("Wiek:", age)
# if not is_salary_hidden:
#     print("Wynagrodzenie:", salary)

# ZADANIE 4________________________________________________________________________________________________________________________________________________________________________
# Poniższy program rysuje kwadrat o określonej długości boku za pomocą modułu turtle.   
# Zapisz program w pliku draw_figures.py. Następnie uruchom program. 
# Dalej zmień program tak, aby kwadrat był rysowany za pomocą funkcji draw_square(length), której jedynym parametrem jest długość boku kwadratu. 
# Umieść zdefiniowaną funkcję w osobnym module figures.py. Na koniec uruchom program ponownie. 

# import turtle  # narzędzia do rysowania grafiki na ekranie
# import figures  # nasz własny moduł

# window = turtle.Screen() # otwiera nowe okienko graficzne
# window.bgcolor("lightgreen")

# side_length = 100 # Długość boku kwadratu

# # Wywołanie funkcji rysującej kwadrat zdefiniowanej w module figures
# figures.draw_square(side_length)

# # Utrzymanie okna otwartego aż do jego zamknięcia przez użytkownika
# window.mainloop() # okno programu pozostaje otwarte i nasłuchuje zdarzeń (na przykład kliknięcia krzyżyka zamknięcia), zamiast zamknąć się błyskawicznie tuż po narysowaniu kwadratu.

# ZADANIE 5________________________________________________________________________________________________________________________________________________________________________
# W module figures.py dodaj następujące definicje funkcji:   

#           draw_trangle(length) do rysowania trójkąta równobocznego / równoramiennego  
#           draw_rectangle(lenght_a, lenght_b) do rysowania prostokąta o bokach a i b 
  
# Następnie napisz program, który rysuje każdą z figur (kwadrat, trójkąt, prostokąt) dwukrotnie, w różnych miejscach. 
# Aby narysować figurę w innym miejscu, skorzystaj z poniższych informacji:

#           pen.penup(): Podnosi pisak, dzięki czemu żółw może się poruszać bez rysowania.   
#           pen.goto(-100, 100): Przesuwa żółwia do współrzędnych (-100, 100). Możesz zmienić te wartości, aby przesunąć żółwia w dowolne miejsce na ekranie.   
#           pen.pendown(): Opuszcza pisak, aby ponownie zacząć rysować. 
   
# Używając penup() oraz pendown(), możesz kontrolować, kiedy żółw rysuje na ekranie, i swobodnie przenosić go w dowolne miejsce.

# Program rysujący kwadrat, trójkąt oraz prostokąt dwukrotnie w różnych miejscach

# import figures
# import turtle

# # Konfiguracja okna rysowania
# window = turtle.Screen()
# window.bgcolor("lightpink")

# # Tworzenie żółwia rysującego
# pen = turtle.Turtle()
# pen.speed(5)


# def move_to(x, y):
#     # Podnosi pisak, przenosi żółwia w nowe miejsce i opuszcza pisak
#     pen.penup()
#     pen.goto(x, y)
#     pen.pendown()

# # Rysowanie figur - pierwszy zestaw miejsc
# move_to(-220, 120)
# figures.draw_square(70, pen)

# move_to(-40, 120)
# figures.draw_trangle(80, pen)

# move_to(120, 120)
# figures.draw_rectangle(100, 50, pen)

# # Rysowanie figur - drugi zestaw miejsc
# move_to(-220, -100)
# figures.draw_square(50, pen)

# move_to(-40, -100)
# figures.draw_trangle(60, pen)

# move_to(120, -100)
# figures.draw_rectangle(80, 110, pen)

# # Ukrycie żółwia i zakończenie programu
# pen.hideturtle()
# window.mainloop()