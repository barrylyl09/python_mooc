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
    turtle.pensize(pythonsize)      #运行轨迹宽度：30
    turtle.pencolor("blue")         #运行轨迹颜色为：蓝色
    turtle.seth(180)                #turtle 启动时的运行的方向 ：角度值 （北：90 南：270 西：180 东：0）负数代表相反方向
    drawSnake(40,80,5,pythonsize/2) #调用 drawSnake函数

main()

'''
val = input("请输入带温度表示符号的温度值（例如：32C）:")

if val[-1] in ['C','c']:
    f = 1.8 * float(val[0:-1]) + 32
    print("转换后的温度为: %.2fF"%f)
elif val[-1] in ['F','f']:
    c = (float(val[0:-1]) - 32) / 1.8
    print("转换后的温度为：%.2fC"%c)
else:
    print("输入有误")

'''