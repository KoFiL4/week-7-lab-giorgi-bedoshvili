def x1(z9):
    if z9 == 1:
        return 1
    else:
        return z9 * x1(z9 - 1)

print(x1(5))  # Output: 120
