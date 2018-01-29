#encoding:utf-8


import math

def test():
    sum = 0
    number = 0
    while number < 20:
        number += 1
        sum += number
        if sum > 100:
            break

    print ("The number is", number)
    print ("The sum is",sum)


def testContinue():
    for num in range(2,10):
        if num % 2 == 0:
            print ("Found an even number", num)
            continue
        print ("Found a number ", num)


def testElse():
    for n in range(2,10):
        if x in range(2,n):
            if n % x == 0:
                print (n, 'equals',x,'*', n//x)
                break

        else:
            # loop fell through without finding a factor
            print (n,'is a prime number')



test()