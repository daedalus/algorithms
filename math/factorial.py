def fac(n):
    if n == 0: return 1
    return fac(n-1)*n
print(fac(12))

def fac(n):
    def _fac2(L):
        if L == []: return 1
        if (l:= len(L)) == 1: return L[0]
        mid = l >> 1
        a,b = L[:mid],L[mid:]
        return _fac2(a) * _fac2(b)
    return _fac2(list(range(1,n+1)))
print(fac(12))

