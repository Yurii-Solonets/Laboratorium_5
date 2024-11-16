def powietanie (imię = "Użytkowniku", język ="polski"):
    if język == "polski":
        print(f"Cześć, {imię}")
    elif język == "angielski":
        print(f"Hello, {imię}")
    elif język == "niemiecki":
        print(f"Gutten Morgen, {imię}")
    else:
        print(f"Witaj, {imię}")

powietanie()

powietanie("Anna")

powietanie("Yurii", "angielski")

powietanie("Andrzej", "niemiecki")

powietanie("Sophie", "francuski")