import turtle
import math

def buildroad(old, new):
    x, y = old[0], old[1]
    a, b = new[0], new[1]
    vecx, vecy = a - x, b - y
    length = math.sqrt(vecx ** 2 + vecy ** 2)
    if vecx >= 0 and vecy >= 0:
       angle = math.atan(vecy / vecx)
       return [0, angle, length]
    elif vecx < 0 and vecy >= 0:
       angle = math.atan(vecy / abs (vecx))
       return [1, angle, length]
    elif vecx < 0 and vecy < 0:
         angle = math.atan(abs (vecx) / abs (vecy))
         return [2, angle, length]
    else:
         angle = math.atan(vecx / abs (vecy))
         return [3, angle, length]


def completestep(road):
    if road[0] == 0:
       turtle.left(road[1])
       turtle.forward(road[2])
       turtle.right(road[1])
    elif road[0] == 1:
       turtle.left(math.pi / 2 + road[1])
       turtle.forward(road[2])
       turtle.right(math.pi / 2 + road[1])
    elif road[0] == 2:
       turtle.right(math.pi / 2 + road[1])
       turtle.forward(road[2])
       turtle.left(math.pi / 2 + road[1])
    else:
       turtle.right(road[1])
       turtle.forward(road[2])
       turtle.left( road[1])
        
def equation(xequation, yequation, step):
  i = 0
  while True:
       tmpx = xequation.replace('@', str (i))
       tmpy = yequation.replace('@', str (i))
       x, y = eval (tmpx), eval (tmpy)
       i += step
       tmpx, tmpy = xequation.replace('@', str (i)), yequation.replace('@', str (i))
       newx, newy = eval (tmpx), eval (tmpy)
       completestep(buildroad([x,y], [newx, newy]))

turtle.radians()
equation("100 * math.cos(@ * math.pi / 180)","100 * math.sin(@ * math.pi / 180)", 1)
       




      
       
    
