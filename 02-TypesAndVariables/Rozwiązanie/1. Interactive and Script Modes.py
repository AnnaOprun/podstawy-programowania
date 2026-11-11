# ZADANIE 1______________________________________________________________________________________________________________
# To zadanie nie wymaga pisania skryptu w pliku, lecz zapoznanie się z trybem interaktywnym Pythona. 
# Należy otworzyć terminal (np. PowerShell), uruchomić powłokę Pythona za pomocą polecenia (python) 
# i upewnić się, że widzisz znak zachęty >>>.

# ZADANIE 2______________________________________________________________________________________________________________

# PS C:\WINDOWS\System32> python
# Python 3.13.14 (tags/v3.13.14:fd17997, Jun 10 2026, 13:03:48) [MSC v.1944 64 bit (AMD64)] on win32
# Type "help", "copyright", "credits" or "license" for more information.
# >>> 7+4
# 11
# >>> (30+10)/2
# 20.0
# >>> 2**3
# 8
# >>> 7>2
# True
# >>> r=4
# >>> area=3.14159*r*r                          --> Oblicza pole koła ze wzoru pi * r^2 i zapisuje w zmiennej 'area'
# >>> area
# 50.26544
# >>> round(area, 2)                            --> Zaokrągla wartość zmiennej 'area' do 2 miejsc po przecinku
# 50.27
# >>> first_name="Anna"
# >>> last_name="Brown"
# >>> full_name=first_name+' '+last_name  
# >>> full_name
# 'Anna Brown'
# >>> print(full_name)
# Anna Brown
# >>> len(full_name)                            --> Sprawdza długość tekstu (! łącznie ze spacją !)
# 10
# >>> a=5
# >>> h=4
# >>> triangle_area=(a*h)/2                     --> Oblicza pole trójkąta ze wzoru (a * h) / 2
# >>> print(triangle_area)
# 10.0
# >>> mean_val=(7+12+31)/3                      --> Oblicza średnią arytmetyczną z trzech liczb
# >>> print(round(mean_val,2))                  --> Zaokrągla i wypisuje wynik średniej do 2 miejsc po przecinku
# 16.67
# >>> exit() 

# ZADANIE 3______________________________________________________________________________________________________________
# BMI Calculator

# height = input('Enter your height in cm: ')
# weight = input('Enter your weight in kg: ')

# height = int(height)
# weight = int(weight)

# bmi = weight / (height/100)**2
# bmi = round(bmi, 2)

# print('Your BMI is', bmi)
# print('Check on the Internet if your BMI is ok!!')

# ZADANIE 4______________________________________________________________________________________________________________
# Program symulujący pięciokrotny rzut kością do gry.

# import random

# print("Symulator rzucania kością")

# for i in range(5):                            --> pętla, która powtórzy się 5 razy (dla każdego rzutu kością).
#     dice_roll = random.randint(1, 6)          --> losuje liczbę CAŁKOWITĄ z zakresu od 1 do 6
#     print(dice_roll, end=" ")
