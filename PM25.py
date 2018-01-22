#encoding:utf-8


def main():
    PM = input("What is today's PM2.5? Please input:\n")
    print 'PM = '+str(PM)
    #打印相应的提醒
    if PM > 75:
        print ("Unhealthy. Be careful!")
    if PM < 35:
        print ("Good. Go running!")


main()