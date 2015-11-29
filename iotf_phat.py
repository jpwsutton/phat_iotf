import sys
import time
try:
    import ibmiotf.application
    import ibmiotf.device
except:
    print("Could not find the IBM IoTF library")
    sys.exit()
    
shutdown_flag = False


def myAppEventCallback(event):
    print("Received live data from %s (%s) sent at %s: hello%s x=%s" % (event.deviceId, event.deviceType, event.timestamp.strftime("%H:%M:%S"), data['hello'], data['x']))

def processCommand(data):
  print("New Data: %s" % data)

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
        processCommand(cmd.data)
  
try:
    options = ibmiotf.device.ParseConfigFile("device.cfg")
    client = ibmiotf.device.Client(options)
    client.commandCallback = commandCallback
    client.connect()
except Exception as e:
    print("Could not connect: %s" % str(e))
    sys.exit()
    
while True:
    if shutdown_flag is True:
        print("Shutdown Flag detected, goodbye")
        client.disconnect()
        sys.exit(0)
    else:
        time.sleep(2)
print("IoTF pHat Controller")

