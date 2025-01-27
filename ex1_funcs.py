def max_three_ints(a, b, c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_arithmetic_sequence(list):
    if len(list) < 2:
        return False
    diff = list[1] - list[0]
    for i in range(1, len(list)):
        if list[i] - list[i-1] != diff:
            return False
    return True