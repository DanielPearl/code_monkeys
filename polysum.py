from math import tan, pi

def polysum(n,s):
    """ Calculates the sum of the area and square of the perimeter of a polygon
    n : number of sides
    s : length of each side
    """
    area = (0.25 * n * (s ** 2)) / (tan(pi / n)) #area of polygon
    perimeter = n * s #perimeter of polygon
    return round(area + (perimeter ** 2),4)
