#encoding:utf-8

'''
#encoding:utf-8 写在程序开头，可以使用中文注释
'''

import turtle

# turtle：外部库 绘制图像

def drawSnake(rad, angle, len, neckrad):

    '''
    :param rad:描述圆形轨迹半径的位置，正数：turtle 左侧    负数：turtle 右侧
    :param angle: 表示 turtle 沿着圆形爬行的弧度值
    :param len:
    :param neckrad:
    :return:

    turtle.circle->让 turtle 沿着圆形轨迹爬行
    turtle.fd()函数也可称为 turtle.forward()函数 ->表示 turtle 向前直线爬行移动，它有个参数表示爬行的距离

    '''

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
    turtle.pensize(pythonsize)      #运行轨迹宽度：30
    turtle.pencolor("blue")         #运行轨迹颜色为：蓝色
    turtle.seth(180)                #turtle 启动时的运行的方向 ：角度值 （北：90 南：270 西：180 东：0）负数代表相反方向
    drawSnake(40,80,1,pythonsize/2) #调用 drawSnake函数

main()

