
def cm_to_m(cm):
    # Przelicza centymetry na metry
    return cm / 100


def m_to_cm(m):
    # Przelicza metry na centymetry
    return m * 100


def cm_to_inches(cm):
    # Przelicza centymetry na cale (1 cal = 2.54 cm)
    return cm / 2.54


def feet_and_inches_to_cm(feet, inches):
    # Przelicza stopy i cale na centymetry (1 stopa = 12 cali, 1 cal = 2.54 cm)
    total_inches = feet * 12 + inches
    return total_inches * 2.54


if __name__ == "__main__":
    # Testy uruchamiane wyłącznie przy bezpośrednim uruchomieniu pliku converters.py
    print(f"100 cm = {cm_to_m(100)} m")
    print(f"2 m = {m_to_cm(2)} cm")
    print(f"25.4 cm = {cm_to_inches(25.4)} in")
    print(f"5 ft 10 in = {feet_and_inches_to_cm(5, 10):.2f} cm")