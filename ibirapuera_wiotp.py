import wiotp.sdk.application
import json
import random

myConfig = {
    "auth": {
        "key": "a-gv6isn-xehobeg6qr",
        "token": "Lzn&I7Id6oqqKwjDkA"
    },
	"mqtt": {
	    "port": 1883,
	    "transport": "tcp",
	    "cleanStart": False,
	    "sessionExpiry": 3600,
	    "keepAlive": 60
	}
}
client = wiotp.sdk.application.ApplicationClient(config=myConfig)

client.connect()

myDeviceType = 'db'
myDeviceId = 'db002'
#myData={'db': 56}

#client.publishEvent(myDeviceType, myDeviceId, "status", "json", myData)

def eventPublishCallback():
    'nada'
    #print("Device Publish Event done!!!")

def myEventCallback(event):
    str = "%s event '%s' received from device [%s]: %s"
    #print(str % (event.format, event.eventId, event.device, json.dumps(event.data)))

client.deviceEventCallback = myEventCallback
client.subscribeToDeviceEvents()

import time

with open("test.csv", "a") as myfile:
    while True:
        time.sleep(1)
        #myData={'temperature': {"value": float(input("temperature> ")), "type": "number"}}
        db = 30+int(70*random.random())
        print(db)
        myData={'noise': db}
        client.publishEvent(myDeviceType, myDeviceId, "stoic", "json", myData, 0, eventPublishCallback)
        myfile.write(str(db)+'\n')

