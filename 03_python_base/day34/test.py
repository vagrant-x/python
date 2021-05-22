import threading
import sys
print(sys.path)

import 线程死锁 as ss

a = threading.Lock()
b = threading.Lock()
t = ss.MyThread(a, b)
t.start()