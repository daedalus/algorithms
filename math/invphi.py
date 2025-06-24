from sympy import divisors, isprime
def invphi(n):
    if n == 1: return [1, 2]
    primes, prime_powers = [x for d in divisors(n) if isprime(x:=(d + 1))], []
    for p in primes:
        lst = [(1,1)]
        m, phi = p, p - 1
        while n % phi == 0:
            lst.append((m, phi))
            m *= p
            phi *= p
        prime_powers.append(lst)
    dp = {1: {1}}
    for lst in prime_powers:
        new_dp = {}
        for phi_old, m_set in dp.items():
            for m_fac, phi_fac in lst:
                if n % (phi_new := phi_old * phi_fac)  == 0:
                    new_dp.setdefault(phi_new, set()).update(m * m_fac for m in m_set)
        dp = new_dp
    return sorted(dp.get(n, []))
