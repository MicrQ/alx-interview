#!/usr/bin/python3
""" prime game """


def sieve_of_eratosthenes(max_n):
    primes = [True] * (max_n + 1)
    primes[0] = primes[1] = False
    p = 2
    while (p * p <= max_n):
        if primes[p]:
            for i in range(p * p, max_n + 1, p):
                primes[i] = False
        p += 1
    prime_list = []
    for p in range(2, max_n + 1):
        if primes[p]:
            prime_list.append(p)
    return prime_list


def isWinner(x, nums):
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_used = [False] * (n + 1)
        prime_count = 0

        for prime in primes:
            if prime > n:
                break
            if not primes_used[prime]:
                prime_count += 1
                for multiple in range(prime, n + 1, prime):
                    primes_used[multiple] = True

        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
