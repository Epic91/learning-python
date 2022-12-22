from math import factorial


def find_factorial_by_looping(n):
    if n < 0:
        return 0
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial = factorial * i
            return factorial
        
print(find_factorial_by_looping(5)) # => 120

# RECURSIVE SOLUTION:
def find_factorial_recursive(n):
    if n == 1:
        return 1
    else:
        return n * find_factorial_recursive(n - 1)

print(find_factorial_recursive(5))
"""
find_factorial_recursive(5)
    = 5 * factorial(4)
    = 5 * (4 * factorial(3))
    = 5 * (4 * (3 * factorial(2)))
    = 5 * (4 * (3 * (2 * factorial(1))))
    = 5 * (4 * (3 * (2 * (1 * factorial(0)))))
    = 5 * (4 * (3 * (2 * (1 * 1))))
    = 5 * (4 * (3 * (2 * 1)))
    = 5 * (4 * (3 * 2))
    = 5 * (4 * 6)
    = 5 * 24
    = 120
"""