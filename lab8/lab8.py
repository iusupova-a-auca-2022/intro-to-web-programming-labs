def square(a):
    return a * a

print(square(5))


def sum_of_num(*numbers):
    return sum(numbers)

print(sum_of_num(5, 2, 13, 8, 9))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(12))


def prime(b):
    if b <= 3:
        return True

    for i in range(4, b):
        if b % i == 0:
            return False

    return True

print(prime(10))
print(prime(7))
print(prime(1))
print(prime(12))