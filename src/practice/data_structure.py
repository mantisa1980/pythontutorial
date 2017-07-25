# -*- coding: utf-8 -*-

def test_dictionary():
    print "test dictionary"
    D = {'x':1, 'y':2 }
    D['z'] = 3

    D.pop('x')
    #D.pop('z')
    D.pop('x1',None)
    
    for k in D.keys():
        print k, D[k]
    
    print "-------"
    
    for k,v in D.iteritems():
        print k,v

def test_list():
    print "test list"
    l = [1,2,3, 'xyz']
    l.append(4)
    l.remove('xyz')
    print "l=", l

def test_tuple():
    print "test tuple"
    x = (1,2,3,)
    print x, x[2]

if __name__ == '__main__':
    test_dictionary()
    test_list()
    test_tuple()

