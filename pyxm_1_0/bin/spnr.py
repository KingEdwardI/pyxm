import itertools
import threading
import time
import sys

"""
super simple animation to indicate that progress is happening

'''
from spnr import ldr

ldr.start()
# Really Long process here
time.sleep(10)
done=True
'''

"""

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rDownloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

ldr = threading.Thread(target=animate)
