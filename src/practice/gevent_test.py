import gevent
from gevent import monkey;monkey.patch_all()
import time

def ping(no):
    print "ping ", no
    time.sleep(1)

coroutines = []
for i in xrange(10):
    coroutines.append(gevent.spawn(ping, i))

print "main joining"
for i in coroutines:
    i.join()

