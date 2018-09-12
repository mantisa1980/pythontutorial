'''
fix the path import error
command reference:
export PYTHONPATH=xxxxx
export PYTHONPATH=$(pwd)/..
'''
from lib.foo import bar

#import sys
#print sys.path  # uncomment to see import paths

y = bar(123)
print "y=", y

'''
fix auto package include error
'''
from lib.subpackage import *
submodule1.submodule1_func()
submodule2.submodule2_func()

print "done"
