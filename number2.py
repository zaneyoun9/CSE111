import cmath
def quadratic(a, b, c): 
    return ((-1 * b) + cmath.sqrt(b**2 - (4 * a * c))) / (2 * a)
print(quadratic(22, 66, 9))
print(quadratic(9, 1, 4))