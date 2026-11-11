# ZADANIE 1______________________________________________________________________________________________________________

# +   -->  dodawanie liczb lub łączenie tekstów. 
# *   -->  mnożenie liczb lub powielanie tekstów (np. "A" * 3 da "AAA").
# **  -->  potęgowanie (np. 2 ** 3 to $2^3$).   
# /   -->  dzielenie rzeczywiste (zawsze daje wynik z częścią dziesiętną). 
# //  -->  dzielenie całkowite (odrzuca resztę po przecinku).
# %   -->  reszta z dzielenia (modulo).
# >   -->  sprawdza, czy lewa strona jest większa od prawej (zwraca True/False).
# <=  -->  sprawdza, czy lewa strona jest mniejsza lub równa prawej.

# ZADANIE 2______________________________________________________________________________________________________________
# Policz, ile operatorów (znaków operacji) i argumentów (wartości/liczb) znajduje się w każdym wyrażeniu. 
# Następnie oblicz ich wartości (najpierw samodzielnie, a potem sprawdź w trybie interaktywnym).

# 1)  3 * 2 + 1
#     - Argumenty: 3 (3, 2, 1)
#     - Operatowy: 2 (*, +)
#     - Wynik: 7

# 2)  5 + 10 * 5
#     - Argumenty: 3 (5, 10, 5)
#     - Operatowy: 2 (+, *)
#     - Wynik: 55

# 3)  4 + 4 / 2 ** 2
#     - Argumenty: 4 (4, 4, 2, 2)
#     - Operatowy: 3 (+, /, **)
#     - Wynik: 5.0

# 4)  4 % 3 % 2 % 1
#     - Argumenty: 4 (4, 3, 2, 1)
#     - Operatowy: 3 trzykrotne (%)
#     - Wynik: 0 

# 5)  1 + 2 % 3 ** 4 * 5
#     - Argumenty: 5 (1, 2, 3, 4, 5)
#     - Operatowy: 4 (+, %, **, *)
#     - Wynik: 11

# 6)  True != False
#     - Argumenty: 2 (True, False)
#     - Operatowy: 1 (!=)
#     - Wynik: True (bo jest różna od fałszu)

# ZADANIE 3______________________________________________________________________________________________________________
# Określ, jaki typ danych reprezentują poniższe wartości. 
# Następnie sprawdź swoje odpowiedzi w trybie interaktywnym, używając wbudowanej funkcji type(wartość).

# >>> type(50)                                  --> liczba całkowita
# <class 'int'>

# >>> type(149.17)                              --> liczba zmiennoprzecinkowa
# <class 'float'>

# >>> type(4 * 7)                               --> wynik mnożenia liczb całkowitych to int
# <class 'int'>

# >>> type(4.0 * 7)                             --> wynik mnożenia z udziałem float daje float
# <class 'float'>

# >>> type("Krakow University of Economics")    --> tekst
# <class 'str'>

# >>> type(True)                                --> wartość logiczna
# <class 'bool'>

# >>> type(2 > 5)                               --> wynik porównania (False) to bool
# <class 'bool'>
