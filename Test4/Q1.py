#Write a function which we parameter and print the factors of a given number

def factors(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

factors(12)
