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
def sentry():
    sum = 0.0
    count = 0
    x = input("Enter a number (negative to quit) >> ")
    while x >= 0:
        sum = sum + x
        count = count + 1
        x = input ("Enter a number (negative to quit) >>")
    print ("\nThe average of the numbers is", sum/count)

void1()