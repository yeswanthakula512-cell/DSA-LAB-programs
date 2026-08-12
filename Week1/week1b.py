def compound_interest(p, n):
    if n == 0:
        return 1
    else:
        return p * compound_interest(p, n - 1)

p = int(input("Enter principal value: "))
n = int(input("Enter number of years: "))

print("Result:", compound_interest(p, n))
