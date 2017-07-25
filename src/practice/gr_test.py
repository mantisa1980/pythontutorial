from greenlet import greenlet

'''
# main greenlet ----- gr1
                |
                |
                ----- gr2 

execution comes back to parent when greenlet dies
'''             

def test1():
    print "1-1"
    gr2.switch()
    print "1-2"

def test2():
    print "2-1"
    gr1.switch()
    print "2-2" # not executed

gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
print "main done"


