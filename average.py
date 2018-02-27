#encoding:utf-8

import math

# 求平均值

# for循环求解
def void1():
    n = input("How many numbers? ")
    sum = 0.0
    for i in range(n):
        x = input("Enter a number >>")
        sum = sum + x

    print ("\nThe average is", sum / n)

# 无线循环 （while）
def void2():
    i = 0
    while i <= 10:
        print (i)
        i = i + 1
        

# 哨兵循环
def sentry1():
    sum = 0.0
    count = 0
    x = input("Enter a number (negative to quit) >> ")
    while x >= 0:
        sum = sum + x
        count = count + 1
        x = input ("Enter a number (negative to quit) >>")
    print ("\nThe average of the numbers is", sum/count)


def sentry2():
    sum = 0.0
    count = 0
    xStr = input("Enter a number (<Enter> to quit) >>")
    while xstr != "":
        x = xstr
        sum = sum + x
        count = count + 1
        xStr = input("Enter a number (<Enter> to quit) >>")
    print ("\nThe average of the numbers is", sum / count)

# 文件循环代码 for
def sentry3():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    sum = 0
    count = 0
    for line in infile:
        sum = sum + eval(line)
        count = count + 1
    print ("\nThe average of the numbers is", sum / count)

# 文件循环代码 while
def sentry4():
    fileName = input("What file are the numbers in? ")
    infile = open(fileName, 'r')
    sum = 0.0
    count = 0
    line = infile.readline()
    whie line != "":
        sum = sum + line
        count = count + 1
        line = infile.readline()

    print ("\nThe average of the numbers is ",sum / count)

'''

def <name>(<parameters>):
    <body>

'''


void1()