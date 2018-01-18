#encoding:utf-8


import math
import random

'''
蒙特卡洛（Monte Carlo）方法,又称随机抽样或统计试验方法。当所求解的问题是某种事件出现的概率，或某随机变量的期望值时，可以通过某种“试验”的方法求解。

简单说，蒙特卡洛是利用随机试验求解问题的方法。

python circlePi.py > MonteCarlo.txt  保存结果进指定文件

'''

from random import random
from math import sqrt

from  time import clock

DARTS = 1200

hits = 0

clock()

for i in  range(1,DARTS):
    x, y = random(), random()

    dist = sqrt(x**2 + y**2)

    if dist <= 1.0:
        hits = hits + 1

pi = 4 * (hits/DARTS)
print("Pi的值是 %s" % pi)
print("程序运行时间是 %-5.5ss" % clock())