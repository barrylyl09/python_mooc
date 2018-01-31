ls#encoding:utf-8

import math

def main():

    print("Let us finds the solutions to a quadratic\n")
    a, b. c = input("Do enter the coefficients (a, b, c): \n")
    delta = b * b - 4 * a * c
    if delta < 0:
        print ("\nThe equation has no real roots!")
    elif delta == 0:
        x = -b / (2 * a)
        print ("\nThere is a double root at", x)
    else:
        print ("计算两个实方根")


main()