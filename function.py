import math
def counter(x):
    base = 1 + x ** 2
    expression = countexpr(x)
    return math.log(expression, base)
def countexpr(x):
    numerator = countnumerator(x)
    denumerator = countdenumerator(x)
    return numerator / denumerator
def countnumerator(x):
    power = 1 / (math.sin(x) + 1)
    return math.exp(power)
def countdenumerator(x):
    top = 5 * (x ** 15) + 4
    bot = 4 * (x ** 15)
    return top / bot
points = [1, 10, 1000]
points = list (map (counter, points))
points = list (map (str, points))
points = ' '.join(points)
print (points)
