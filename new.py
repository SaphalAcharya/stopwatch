import time
import sys

#  lowercase inputs.
# the steps are: type s to  start stopwatch, Type f to  stop stopwatch and Type c to calculate time passed.

start = input('Start stopwatch? s/n: ')
if start == "s":
    startTime = time.time()
else:
    print("program closed")
    sys.exit() 


finish = input("Stop? f/n: ")
if finish == "f":
    finishTime = time.time()
else:
    print("program closed")
    sys.exit()


calculate = input("Calculate? s/f: ")
if calculate == "c":
    print("Time passed =", (finishTime - startTime), "seconds.")
else:
    print("program closed")
    sys.exit()