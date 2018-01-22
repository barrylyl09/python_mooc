#encoding:utf-8


def main():
    # PM = eval(input("What is today's PM2.5?"))
    PM = 23
    print ('PM = %s',PM)
    #打印相应的提醒
    if PM > 75:
        print ("Unhealthy. Be careful!")
    if PM < 35:
        print ("Good. Go running!")


main()