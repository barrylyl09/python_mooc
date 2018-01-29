#encoding:utf-8

import math

def void1():
    n = input("How many numbers? ")
    sum = 0.0
    for i in range(n):
        x = input("Enter a number >>")
        sum = sum + x

    print ("\nThe average is", sum / n)

void1()