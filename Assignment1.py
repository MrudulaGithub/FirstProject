with open("C:\Users\mrudu\Desktop\sdet1.txt","r") as my_file:
    line = 0
    for i in my_file:
        if i > line:
            print len(i)
            print "%s" % i
        line += 1


