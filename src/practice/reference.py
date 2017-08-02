'''
reference practice
'''
def bar(i): 
    i+= 1
    return i

def qux(x):
    x.append(4)
    return x

# immutable objects
x = 123
print "before bar:x={}, id(x)={}".format(x, id(x))
y = bar(x)
print "after bar:x={}, y={},id(x)={}, id(y)={}".format(x,y,id(x),id(y))
print "id(x)==id(123)? {} , id(y)==id(124)? {}".format(id(x)==id(123), id(y)==id(124))
print "x is123? {} , y is 124? {}".format(x is 123, y is 124)

# mutable objects
a = [1,2,3]
b = qux(a)
print "a={},b={}".format(a , b)

c = [1,2,3,4]
print "a == c ? {}; a is c ? {}".format(a==c, a is c)
