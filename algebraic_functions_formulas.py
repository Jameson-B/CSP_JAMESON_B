# Jameson Bultez, Algebraic Functions and Formulas Python

import math

def linear(a, x, h, k):
    f = a(x-h) + k
    return f

def quadratic(a, x, h ,k):
    f = a(x-h)**2 + k
    return f

def cubic(a, x, h ,k):
    f = a(x-h)**3 + k
    return f

def any_degree(n, a, x, h, k):
    f = a(x-h)**n + k

def absolute(a, x, h, k):
    f = a*abs(x-h) + k

def exponential(a, b, x, h ,k):
    f = a*b**(x-h) + k
    return f

def reciprocal(a, x, h, k):
    f = a / (x-h) + k
    return f

def circle_area_decimal(r):
    a = math.pi*r**2
    return a

print(circle_area_decimal(6))

def circle_area_exact(r):
    a = str(r**2) + "pi"
    return a

print(circle_area_exact(6))

def quadratic_formula_decimal(a, b, c):
    try:
        x = (-b + math.sqrt(b**2 - 4*a*c))/2*a
        y = (-b - math.sqrt(b**2 - 4*a*c))/2*a
    except ValueError:
        return "Solution is not a real number."    
    return x, y

print(quadratic_formula_decimal(4, -10, 4))


