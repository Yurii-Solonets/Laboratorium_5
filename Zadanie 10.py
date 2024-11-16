def wspólne_elementy(seq1, seq2):
    zbiór1 = set(seq1)
    zbiór2 = set(seq2)
    wspólne = zbiór1 & zbiór2
    return list(wspólne)

seq1 = [1, 2, 3, 4, 5]
seq2 = [4, 5, 6, 7, 8]
wynik = wspólne_elementy(seq1, seq2)
print("Wspólne elementy: ", wynik)