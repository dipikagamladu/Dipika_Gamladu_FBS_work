# Write a program to solve the following series:
# a.1!+2!+3!+4!+.....n!
# b.N+N^2+N^3+N^4....++N^N (here ^ means exponent)
# c.Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d.S=a+a2/2+a3/3+..... +a10/10
# e.x-x2/3+x3/5-x4/7+....to n terms

# a. 1! + 2! + 3! + ... + n!
def series_a(n):
    total = 0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total += fact
    return total


# b. N + N^2 + N^3 + ... + N^N
def series_b(N):
    total = 0
    for i in range(1, N + 1):
        total += N ** i
    return total


# c. Sum of a geometric series from 1 to n, common ratio = 2
def series_c(n):
    total = 0
    term = 1
    r = 2
    for i in range(n):
        total += term
        term *= r
    return total


# d. S = a + a^2/2 + a^3/3 + ... + a^10/10
def series_d(a):
    total = 0
    for i in range(1, 11):
        total += (a ** i) / i
    return total


# e. x - x^2/3 + x^3/5 - x^4/7 + ... to n terms
def series_e(x, n):
    total = 0
    denom = 1
    sign = 1
    for i in range(1, n + 1):
        total += sign * (x ** i) / denom
        denom += 2
        sign *= -1
    return total


if __name__ == "__main__":
    n = int(input("Enter n: "))
    print("a. 1!+2!+...+n! =", series_a(n))

    N = int(input("Enter N: "))
    print("b. N+N^2+...+N^N =", series_b(N))

    n2 = int(input("Enter n (number of terms) for geometric series: "))
    print("c. Geometric series sum (ratio=2) =", series_c(n2))

    a = float(input("Enter value of a: "))
    print("d. S = a+a2/2+...+a10/10 =", series_d(a))

    x = float(input("Enter value of x: "))
    n3 = int(input("Enter number of terms: "))
    print("e. x-x2/3+x3/5-... =", series_e(x, n3)) 