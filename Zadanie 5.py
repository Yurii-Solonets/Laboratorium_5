def oblicz_bmi(waga, wzrost):
    bmi = waga/(wzrost ** 2)

    if bmi < 16:
        kategoria = "Wygłodzenie"
    elif 16 <= bmi < 17:
        kategoria = "Wychudzenie"
    elif 17<= bmi < 18.5:
        kategoria = "Niedowaga"
    elif 18 <= bmi < 25:
        kategoria = "Pożądana masa ciała"
    elif 25 <= bmi < 30:
        kategoria = "Nadeaga"
    elif 30 <= bmi < 35:
        kategoria = "Otyłość 1 stopnia"
    elif 35 <= bmi < 40:
        kategoria = "Otyłość 2 stopnia"
    else:
        kategoria = "Otyłość 3 stopnia"

    return bmi, kategoria

waga = float(input("Podaj swoją wagę w kg: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))
bmi, kategoria = oblicz_bmi(waga, wzrost)

print(f"Twoje BMI wynosi: {bmi:.2f}")
print(f"Jesteś w kategorii: {kategoria}")