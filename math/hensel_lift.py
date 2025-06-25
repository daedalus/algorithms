def poly_eval(poly, x_val):
    """Evaluate polynomial at x using Horner's method."""
    result = 0
    for coeff in reversed(poly):
        result = result * x_val + coeff
    return result


def poly_derivative(poly):
    """Compute derivative coefficients of polynomial."""
    return [i * poly[i] for i in range(1, len(poly))]


def poly_divmod(dividend, divisor, p):
    """Perform polynomial division over integers mod p. Return (quotient, remainder)."""
    out = list(dividend)
    m, n = len(dividend), len(divisor)
    quotient = [0] * (m - n + 1)
    divisor_lead_inv = pow(divisor[-1], -1, p)
    for i in range(m - n, -1, -1):
        coeff = out[i + n - 1] * divisor_lead_inv % p
        quotient[i] = coeff
        for j in range(n):
            out[i + j] = (out[i + j] - coeff * divisor[j]) % p
    remainder = out[:n - 1] if n > 1 else []
    return quotient, remainder


def factor_poly_mod_p(poly, p):
    """Factor polynomial mod p into linear factors (roots)."""
    roots = find_roots_mod_p(poly, p)
    linear_factors = []
    for r in roots:
        linear_factors.append([(-r) % p, 1])  # (x - r) ≡ x + (-r) mod p
    return linear_factors


def find_roots_mod_p(poly, p):
    """Find roots of polynomial mod p by brute-force."""
    roots = []
    for x in range(p):
        if poly_eval(poly, x) % p == 0:
            roots.append(x)
    return roots


def lift_root_with_factoring(f_coeffs, p, k):
    """
    Factor f mod p to find linear roots, then lift each to mod p^k.

    Args:
        f_coeffs: List[int] - polynomial coefficients [a0, ..., an]
        p: prime modulus
        k: exponent

    Returns:
        List[int]: lifted roots mod p^k
    """
    linear_factors = factor_poly_mod_p(f_coeffs, p)
    print(f_coeffs, linear_factors)
    roots = []
    for factor in linear_factors:
        root = (-factor[0]) % p
        try:
            lifted = hensel_lift(f_coeffs, root, p, k)
            roots.append(lifted)
        except ValueError:
            pass  # Skip roots where derivative is zero mod p
    return roots


def hensel_lift(poly, root, p, k):
    """
    Lift a root of f(x) ≡ 0 (mod p) to a root modulo p^k via Hensel's lemma.

    Args:
        poly: list of ints, coefficients [a0, a1, ..., an] for f(x)
        root: initial solution mod p
        p: prime modulus
        k: exponent for target modulus p^k

    Returns:
        int: lifted root modulo p^k
    """
    if poly_eval(poly, root) % p != 0:
        raise ValueError(f"{root} is not a root mod {p}")

    deriv = poly_derivative(poly)
    modulus = p
    current_root = root

    for _ in range(1, k):
        f_val = poly_eval(poly, current_root)
        f_der = poly_eval(deriv, current_root)

        if f_der % p == 0:
            raise ValueError("f'(root) ≡ 0 mod p; Hensel lifting fails")

        if f_val % modulus != 0:
            raise ValueError("f(x) not divisible by current modulus; lifting fails")

        delta = (-f_val // modulus) % p
        inv_der = pow(f_der, -1, p)
        t = (delta * inv_der) % p

        current_root += t * modulus
        modulus *= p

    return current_root % modulus


if __name__ == '__main__':
    # Example: f(x) = x^2 - 2 over mod 7, lift to mod 49
    f = [-2, 0, 1]  # x^2 - 2
    p = 7
    k = 2

    roots = lift_root_with_factoring(f, p, k)
    print(f"Lifted roots mod {p**k}: {roots}")
    for r in roots:
        print(f"f({r}) mod {p**k} =", poly_eval(f, r) % (p**k))
