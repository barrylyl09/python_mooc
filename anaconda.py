#encoding:utf-8

'''
#encoding:utf-8 写在程序开头，可以使用中文注释
'''

import turtle

# turtle：外部库 绘制图像

def drawSnake(rad, angle, len, neckrad):
    for i in  range(len):
        turtle.circle(rad, angle)
        turtle.circle(-rad, angle)
    turtle.circle(rad, angle/2)
    turtle.fd(rad)
    turtle.circle(neckrad+1, 180)
    turtle.fd(rad *2/3)

def main():
    turtle.setup(3000, 1000, 0, 0)  #绘制一个 width:3000 hight：1000 的矩形
    pythonsize = 80
    turtle.pensize(pythonsize)      #绘制线粗细为：30
    turtle.pencolor("blue")         #绘制的颜色为：蓝色
    turtle.seth(-40)                #往坐标抽 -
    drawSnake(40,80,5,pythonsize/2) #

main()