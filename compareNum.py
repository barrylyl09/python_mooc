#encoding:utf-8

'''

比较数值 三个数
1. 通盘比较 (将每一个值与其他所有值比较以确定最大值)
2. 决策树  (决策树方法可以避免冗余的比较)
3. 顺序处理 （逐个扫描每个值，保留最大者）

'''

import math

# 1. 通盘比较
def void1():
    print ("Please enter three digits!")
    a, b, c = input("Please enter digits:(a, b, c) \n")
    # print 'a = ' + str(a) ： 打印测试

    if a >= b and a >= c:
        max = 'a'
    elif b >= a and b >= c:
        max = 'b'
    else:
        max = 'c'

    print '最大数值是：' + str(max)

# 2. 决策树
def void2():
    print ("Please enter three digits!")
    a, b, c = input("Please enter digits:(a, b, c) \n")

    if a >= b:
        if a >= c:
            max = 'a'
    else:
        if b >= c:
            max = 'b'
        else:
            max = 'c'

    print '最大数值是：' + str(max)

# 3. 顺序处理
def void3():
    print ("Please enter three digits!")
    a, b, c = input("Please enter digits:(a, b, c) \n")

    temp = a
    max = 'a'
    if b > temp:
        max = 'b'
    if c > temp:
        max = 'c'

    print '最大数值是：' + str(max)


void3()