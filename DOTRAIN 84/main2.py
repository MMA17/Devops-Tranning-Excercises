import sys
import time


def exception(type, value, traceback):
    print("Type: " + str(type))
    print("Value: " + str(value))
    print("Traceback: " + str(traceback))


sys.excepthook = exception


while True:
    print("testing...")
    time.sleep(1)
