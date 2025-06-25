def poly_eval(poly, x):
    """Evaluate polynomial given by list of coefficients at x"""
    result = 0
    for coeff in reversed(poly):
        result = result * x + coeff
    return result

def poly_derivative(poly):
    """Return the derivative of a polynomial given as list of coefficients"""
    return [i * poly[i] for i in range(1, len(poly))]

def hensel_lift_numeric(poly, a, p, k):
    """
    Lift root `a` of f(x) ≡ 0 mod p to a root modulo p^k using Hensel's lemma.
    
    Parameters:
        poly: list of integer coefficients [a0, a1, ..., an] representing a0 + a1*x + ... + an*x^n
        p: prime number
        a: initial root mod p
        k: target power of p to lift to
    
    Returns:
        The lifted root mod p^k
    """
    root = a
    deriv = poly_derivative(poly)
    p_i = 1

    for i in range(1, k):
        p_i *= p
        f_val = poly_eval(poly, root)
        f_der = poly_eval(deriv, root)
        if f_der % p == 0:
            raise ValueError("Derivative zero mod p, Hensel's lemma does not apply")

        # Solve: f(a) + f'(a) * t * p^i ≡ 0 mod p^{i+1}
        # Let t = -f(a)/p^i * (f'(a)^{-1} mod p)
        
        t = (-f_val // p_i) % p
        t = (t * pow(f_der, -1, p)) % p
        root += (t * p_i) 
    
    return root % (p_i*p)

f = [-2, 0, 1]
p = 7
a = 3 
k = 2

root = hensel_lift_numeric(f, a, p, k)
print(f"Lifted root mod {p**k} is", root)
print("f(root) mod p^k =", poly_eval(f, root) % (p ** k))
