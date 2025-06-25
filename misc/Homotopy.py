from typing import Callable

# Define a type for functions A -> B
Function = Callable[[int], int]

# Define a homotopy between two functions f, g: A → B
# A homotopy H is a function that assigns to each x a path from f(x) to g(x)
class Homotopy:
    """
    This class simulates a homotopy between two functions f and g over integers.
    
    Caveat:
        This is only a discrete and finite approximation of homotopy.
        True homotopy in Homotopy Type Theory involves continuous paths and higher
        identity types in type-theoretic or topological spaces.
        This model only checks pointwise equality on a fixed finite domain.
    """
    def __init__(self, f: Function, g: Function):
        self.f = f
        self.g = g
    
    def is_homotopy(self) -> bool:
        for x in range(10):  # Check for x in a small domain
            if self.f(x) != self.g(x):
                print(f"Not equal at x = {x}: {self.f(x)} != {self.g(x)}")
                return False
        return True
    
    def path(self, x: int) -> str:
        return f"Path from {self.f(x)} to {self.g(x)} at x={x}"

# Example: Two functions that are pointwise equal (homotopic)
def f(x): return 2 * x
def g(x): return x + x

H = Homotopy(f, g)

print("Are f and g homotopic?", H.is_homotopy())
for x in range(5):
    print(H.path(x))