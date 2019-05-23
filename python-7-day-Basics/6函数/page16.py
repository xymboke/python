import math
def circlearea(r):#计算圆面积的函数
    result = math.pi*r*r  #计算圆的面积
    return result #返回圆的面积
r=10
print('半径为',r,'的圆面积为:',circlearea(r))


r=10
result = lambda r:math.pi*r*r  #计算圆的面积的lambda表达式
print('半径为',r,'的圆面积为:',circlearea(r))
