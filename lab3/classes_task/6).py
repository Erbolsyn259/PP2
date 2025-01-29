is_prime = lambda x: x > 1 and all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))

numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16]

prime_numbers = list(filter(is_prime, numbers))

print("Prime numbers in the list:", prime_numbers)
