import displayThread
import time

startThread()
nameList = ["One", "Two", "Three", "Four", "Five"]
for word in nameList:
    addMessage(word)

time.sleep(10)
stopThreads()

print "Done."
