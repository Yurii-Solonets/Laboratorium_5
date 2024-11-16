import math

def oblicz_pole_trójkąta (a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Boki muszą być dodatnimi"
    if a + b <= c or a + c <= b or c <= a:
        return "Podane boki nie mogą tworzyć trójkąta."

    s = (a + b + c) / 2

    pole = math.sqrt(s * (s - a) * (s - b) * (s - c))

    return pole

try:
    a = float(input("Podaj długość boku a: "))
    b = float(input("Podaj długość boku b: "))
    c = float(input("Podaj długość boku c: "))

    pole = oblicz_pole_trójkąta(a, b, c)

    print(f"Pole trójkąta wynosi: {pole}")
except ValueError:
    print("Wprowadzona wartość nie jest poprawna")