import math 
def polysum(s,n):
    '''
    this function takes two arguments 
    s side length of polygon
    n number of sides 
    return sum of area a
    and square of
    perimeter p
    rounded to fourth decimal number
    '''
    a=(.25*math.pow(s,2))/(math.tan(math.pi/n)
    p=s*n
    return round(a+pow(p,2),4)

