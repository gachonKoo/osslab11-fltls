import geo.utils as utils

a, b = 3, 4
c = utils.pythagoras(a, b)
print('c =', c)

r = 10
area = utils.circle(r)
print('area =', area)
import math

def pythagoras(a, b):
    c = math.sqrt(a**2 + b**2)
    return c

def circle(r):
    area = math.pi * r**2
    return area
__all__ = ['pythagoras', 'circle']
