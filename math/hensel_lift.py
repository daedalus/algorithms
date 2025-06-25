def poly_eval(poly, x):
    """Evaluate polynomial at x using Horner's method."""
    result = 0
    for coeff in reversed(poly):
        result = result * x + coeff
    return result


def poly_derivative(poly):
    """Compute derivative coefficients of polynomial."""
    return [i * poly[i] for i in range(1, len(poly))]


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
    # Validate initial root
    if poly_eval(poly, root) % p != 0:
        raise ValueError(f"{root} is not a root mod {p}")

    deriv = poly_derivative(poly)
    modulus = p
    current_root = root

    for exp in range(1, k):
        # Evaluate f and f' at current root
        f_val = poly_eval(poly, current_root)
        f_der = poly_eval(deriv, current_root)

        if f_der % p == 0:
            raise ValueError("f'(root) ≡ 0 mod p; Hensel lifting fails")

        # Compute correction term t
        # f_val + f_der * t * p^exp ≡ 0 (mod p^(exp+1))
        delta = (-f_val // modulus) % p
        inv_der = pow(f_der, -1, p)
        t = (delta * inv_der) % p

        # Update root and modulus
        current_root += t * modulus
        modulus *= p

    return current_root % modulus


if __name__ == '__main__':
    # Example: f(x) = x^2 - 2, root mod 7 is 3, lift to mod 49
    f = [-2, 0, 1]
    p = 7
    a = 3
    k = 2
    r = hensel_lift(f, a, p, k)
    print(f"Lifted root mod {p**k} is {r}")
    print("Verification:", poly_eval(f, r) % (p**k) == 0)
