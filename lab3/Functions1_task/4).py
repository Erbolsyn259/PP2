import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0 and n != i:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
primes = filter_prime(numbers)
print(primes)
