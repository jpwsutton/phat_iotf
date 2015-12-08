import sys
import time
import scrollphat
from Queue import Queue
from threading import thread



try:
    import ibmiotf.application
    import ibmiotf.device
except:
    print("Could not find the IBM IoTF library")
    sys.exit()

matrix_length = 11
shutdown_flag = False

myQueue = Queue()

def displayThread(i, q):
    """This is the worker thread function.
    It processes items in the queue one after
    another. This thread will go in an 
    infinite loop and only exit with the main
    thread ends.
    """
    while True:
        


def myAppEventCallback(event):
    print("Received live data from %s (%s) sent at %s: hello%s x=%s" % (event.deviceId, event.deviceType, event.timestamp.strftime("%H:%M:%S"), data['hello'], data['x']))

def processCommand(data):
  print("New Data: %s" % data)


def scrollText(data):
    scrollphat.clear()
    length = scrollphat.write_string(data['message'] + " ")
    scrollcount = int(data['scrollcount'])
    for i in range(scrollcount):
        for x in range(length - matrix_length):
            scrollphat.scroll()
            time.sleep(0.1)
    scrollphat.clear()

def commandCallback(cmd):
    if cmd.command == "shutdown":
        if 'shutdown' not in cmd.data:
            print("Error incorrect shutdown command")
        else:
            if cmd.data['shutdown'] is True:
                print("Shutdown received, goodbye!")
                global shutdown_flag
                shutdown_flag = True
    elif cmd.command == "scroll":
        scrollText(cmd.data)
    elif cmd.command == "clear":
        scrollphat.clear()
  
try:
    options = ibmiotf.device.ParseConfigFile("device.cfg")
    client = ibmiotf.device.Client(options)
    client.commandCallback = commandCallback
    client.connect()
except Exception as e:
    print("Could not connect: %s" % str(e))
    sys.exit()

length = scrollphat.write_string("Connected")
for x in range(length - matrix_length):
    scrollphat.scroll()
    time.sleep(0.1)

q = Queue.Queue()
    
while True:
    if shutdown_flag is True:
        print("Shutdown Flag detected, goodbye")
        client.disconnect()
        sys.exit(0)
    else:
        time.sleep(2)
print("IoTF pHat Controller")

