import lib.foo
import time
from lib.foo import bar

t = time.time()
for i in range(0,10000000):
    #lib.foo.bar()
    bar()

print time.time()-t

