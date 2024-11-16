def odwróć_string(tekst):
    return tekst[::-1]

tekst = input("Podak tekst do odwrócenia: ")
odwrócony = odwróć_string(tekst)
print(f"Odwrócony tekst: {odwrócony}")