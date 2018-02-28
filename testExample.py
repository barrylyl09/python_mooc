#encoding:utf-8



def void1():
    print 'i like to use the Internet for:'
    for item in ['e-mail', 'net-surfing', 'homework', 'chat']:
        print item,
    print

'''
print 默认换行，使用 "," 可以改变这种行为

1. ➜  python_mooc git:(master) ✗ python testExample.py
i like to use the Internet for:
e-mail
net-surfing
homework
chat
2. ➜  python_mooc git:(master) ✗ python testExample.py
i like to use the Internet for:
e-mail net-surfing homework chat

'''

def void2():
    while True:
        reply = input('Enter text:')
        print reply
        if reply == 'stop':
            break
        elif not reply.isdigit():
            print ('Bad!' * 8)
            print reply
        else:
            num = int(reply)
            if num < 20:
                print ('low')
            else:
                numb = num ** 2 # ** 根运算
                print (numb)
                print 'numb = ' + str(numb)
        print ('Bye')


def void3():
    while True:
        reply = input('Enter text: ')
        print 'reply = ' + str(reply)
        if reply == "stop":
            break
        try:
            # 如果 try 内代码块 报错 ，就执行 except 中代码块
            # try 语句是用于在 Python 脚本中捕捉和恢复异常（错误）的。这通常是程序中自行检查错误的方法之一。
            num = int(reply)
            print 'num = ' + str(num)

        except:
            print ('Bad!' * 3)
        else:
            numb = int(reply) ** 2
            print (numb)
            print 'numb = ' + str(numb)

    print ('Bye')









