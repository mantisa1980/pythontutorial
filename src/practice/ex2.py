from lib.foo import bar

'''
fix the import path error
command reference:
export PYTHONPATH=xxxxx

'''
#import sys
#print sys.path  # uncomment to see import paths

y = bar(123)
print y
print "done"

