import sys
import time
import scrollphat
import displayThread
import sprite

try:
    import ibmiotf.application
    import ibmiotf.device
except:
    print("Could not find the IBM IoTF library")
    sys.exit()

matrix_length = 11
shutdown_flag = False

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
    elif cmd.command == "text":
        displayThread.addMessage({'text' : cmd.data})
    elif cmd.command == "sprite":
        displayThread.addMessage({'sprite' : cmd.data})
    elif cmd.command == "spriteName":
        displayThread.addMessage({'spriteName' : cmd.data})


# Start the display thread and send the startup messages
displayThread.startThread()
startupMsg = {'text' : 'Hello World!'}
startupSprite = {'sprite' : sprite.face_chibbi_happy}
displayThread.addMessage(startupMsg)
displayThread.addMessage(startupSprite)


# Connect to IoTF
try:
    options = ibmiotf.device.ParseConfigFile("device.cfg")
    client = ibmiotf.device.Client(options)
    client.commandCallback = commandCallback
    client.connect()
except Exception as e:
    print("Could not connect: %s" % str(e))
    sys.exit()

# Send 'Connected' Message to display
displayThread.addMessage({'text' : 'Connected.'})



while True:
    if shutdown_flag is True:
        print("Shutdown Flag detected, goodbye")
        displayThread.addMessage({'text' : 'Goodbye!'})
        displayThread.stopThreads();
        client.disconnect()
        sys.exit(0)
    else:
        time.sleep(1)
