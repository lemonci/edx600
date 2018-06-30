def polysum(n, s):
    import math
    tan = math.tan
    pi = math.pi
    area = (0.25*n*s*s)/(tan(pi/n))
    perimeter = n * s
    sum = area + perimeter * perimeter
    return float("{0:.4f}".format(sum))
