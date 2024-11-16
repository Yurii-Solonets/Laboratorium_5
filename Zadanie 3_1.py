def powietanie():
    imię = input("Podaj imię: ")
    język = input("Podaj język: ")
    if język == "polski":
        print(f"Cześć, {imię}")
    elif język == "andielski":
        print(f"Hello, {imię}")
    elif język == "niemiecki":
        print(f"Gutten Morgen, {imię}")
    else:
        print(f"Witaj, {imię}")

powietanie()