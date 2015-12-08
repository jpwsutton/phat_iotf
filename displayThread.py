#!/usr/bin/python

import Queue
import threading
import time

exitFlag = 0
queueLock = threading.Lock()
messageQueue = Queue.Queue(10)
threads = []

class displayThread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q

    def run(self):
        print "Starting " + self.name
        standby_process(self.name, self.q)
        print "Exiting " + self.name

def standby_process(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not q.empty():
            data = q.get()
            queueLock.release()
            print "%s processing %s" % (threadName, data)
        else:
            queueLock.release()
        time.sleep(1)


def startThread():
    thread = displayThread(1, "displayThread-1", messageQueue)
    thread.start()
    threads.append(thread)

def stopThreads():
    exitFlag = 1
    for t in threads:
        t.join()
    print "All Threads finished."

def addMessage(data):
    queueLock.acquire()
    messageQueue.put(data)
    queueLock.release()
