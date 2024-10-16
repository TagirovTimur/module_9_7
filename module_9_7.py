
def is_prime(func):
    def wrapper(*args):
        is_primes = True
        result_fanc = func(*args)
        for i in range(2, result_fanc):
            if result_fanc % i == 0:
                is_primes = False
        if is_primes:
            print("Простое")
        else:
            print("Составное")
        return result_fanc
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

result = sum_three(2, 3, 6)
print(result)
