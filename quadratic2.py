#encoding:utf-8

import math
def main():
    print ("This program finds the real solutions to a quadratic. \n")
    try:
        a, b, c = input("Please enter the cofficients (a, b, c): \n")
        discRoot = math.sqrt(b * b - 4 * a * c)
        root1 = (-b + discRoot) / (2 * a)
        