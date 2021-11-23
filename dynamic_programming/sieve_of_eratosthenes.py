def sieve_of_eratosthenes(end: int, start: int = 2) -> list[int]:
    """compute all primes between certain bounds
    :param end: upper bound for primes
    :param start: lower bound for primes
    :return: list of all primes between start and end
    """
    prime = [True for _ in range(end + 1)]
    p = 2
    while p * p <= end:
        if prime[p]:
            for i in range(p * p, end + 1, p):
                prime[i] = False
        p += 1
    return [index for index, p in enumerate(prime) if p and index >= start]


def is_prime(number: int) -> bool:
    """check if number is prime"""
    return number in sieve_of_eratosthenes(number, number)
