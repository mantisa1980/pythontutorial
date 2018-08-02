# -*- coding: utf-8 -*-

'''
remove first line and test the result
'''

'''
this is a block comment
'''

# This is a line comment

while True:
    x = int(input('Please input age number\n'))
    if x < 0:
        print("Exit loop")
        break
    if x < 10:
        print ("Age is {}, you are kid".format(x))
    elif x  < 18:
        print ("Age is {}, you are teenager".format(x))
    elif x  < 30:
        print ("Age is {}, you are young man".format(x))
    elif x  < 45:
        print ("Age is {}, you are grown man".format(x))
    else:
        print ("Age is {}, you are old man".format(x))

times = 5
for i in range(0, times):
    print("times:{}".format(i))

print("Done")