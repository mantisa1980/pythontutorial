def bar(i):  # another name pointing to same memory
    #print "bar 1", id(i)
    i+= 1
    #print "bar 2", id(i)
    return i

def qux(x):
    x.append(999)
    return x
