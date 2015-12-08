#!/usr/bin/python

import Queue
import threading
import scrollphat
import time

exitFlag = 0
queueLock = threading.Lock()
messageQueue = Queue.Queue(10)
threads = []

matrix_length = 11

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
            if 'text' in data:
                scrollText(data['text'])
            if 'spriteName' in data:
                displaySpriteFromName(data['spriteName'])
            if 'sprite' in data:
                displaySprite(data['sprite'])
        else:
            queueLock.release()
        time.sleep(1)


def scrollText(text):
    print("Displaying text: " + text)
    # Write the text to the display, the extra space is to make scrolling look better.
    length = scrollphat.write_string(text + "  ")
    for i in range(length - matrix_length):
        scrollphat.scroll()
        time.sleep(0.1)
    scrollphat.clear()

def displaySpriteFromName(spriteName):
    print("Displaying sprite from name: "  + spriteName)

def displaySprite(sprite):
    print("Displaying Sprite: %s"  % sprite)

def startThread():
    thread = displayThread(1, "displayThread-1", messageQueue)
    thread.start()
    threads.append(thread)

def stopThreads():
    global exitFlag
    print "Asked to stop threads."
    exitFlag = 1
    for thread in threads:
        thread.join()
    print "All Threads finished."

def addMessage(data):
    queueLock.acquire()
    messageQueue.put(data)
    queueLock.release()
