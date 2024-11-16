def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Podaj, który wyraz ciągu Fibonacciego chcesz obliczyć: "))

wynik = fibonacci(n)
print(f"{n}-ty wyraz ciągu Fibonacciego to: {wynik}")