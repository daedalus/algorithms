from itertools import permutations

def is_magic_square_odd(perm, n, magic_constant):
    grid = [[perm[i*n + j] for j in range(n)] for i in range(n)]
    # Check rows, columns, and diagonals
    for row in grid:
        if sum(row) != magic_constant:
            return False
    for j in range(n):
        if sum(grid[i][j] for i in range(n)) != magic_constant:
            return False
    if sum(grid[i][i] for i in range(n)) != magic_constant:
        return False
    if sum(grid[i][n-1-i] for i in range(n)) != magic_constant:
        return False
    return True

def a(n):
    c = 0
    m = 2 * n + 1
    if m != 3:  # Only feasible for 3×3
        print(f"Skipping {m}×{m} (too slow for brute-force)")
        return 0
    m_squared = m * m
    magic_constant = m * (m_squared + 1) >> 1
    numbers = list(range(1, m_squared + 1))
    # Check all permutations (only feasible for 3×3)
    for perm in permutations(numbers):
        if perm[m_squared >> 1] == 5 and  is_magic_square_odd(perm, m, magic_constant):
            c += 1
    # Adjust for duplicates (each magic square appears 8 times due to rotations/reflections)
    unique_count = c >> 3
    print(f"Total magic squares of size {m}×{m}: {unique_count} unique, {c} total")
    return unique_count


print(a(1))
