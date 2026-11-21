
import converters


def main():
    print("### Testowanie funkcji z modułu converters ###")
    print(f"175 cm to {converters.cm_to_m(175)} m")
    print(f"1.75 m to {converters.m_to_cm(1.75)} cm")
    print(f"50.8 cm to {converters.cm_to_inches(50.8)} cali")
    print(f"6 stóp i 2 cale to {converters.feet_and_inches_to_cm(6, 2):.2f} cm")


if __name__ == "__main__":
    main()