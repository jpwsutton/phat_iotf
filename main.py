import displayThread
import time

displayThread.startThread()
nameList = ["One", "Two", "Three", "Four", "Five"]
for word in nameList:
    displayThread.addMessage(word)

time.sleep(10)
displayThread.stopThreads()

print "Done."
