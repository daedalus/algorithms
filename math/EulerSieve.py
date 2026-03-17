def euler_sieve(n):
    primes = []
    spf = [0] * (n + 1)

    for i in range(2, n + 1):

        if spf[i] == 0:
            spf[i] = i
            primes.append(i)

        for p in primes:
            x = p * i
            if x > n:
                break

            spf[x] = p

            if p == spf[i]:
                break

    return primes, spf