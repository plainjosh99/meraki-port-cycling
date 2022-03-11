import meraki
import requests
import json
from datetime import datetime

API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
dashboard = meraki.DashboardAPI(API_KEY)
payload = None
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": API_KEY
}
dt = datetime.now().strftime("%Y_%m_%d-%I.%M.%S.%p")
divider = "\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n"

#FUNCTIONS
def getresponse(serialnumber):
    url = "https://api.meraki.com/api/v1/devices/{}/switch/ports".format(serialnumber)
    response = requests.request('GET', url, headers=headers, data = payload)
    refined = json.loads(response.text)
    if 'errors' in refined:
        print("Could not establish a good API handshake with device serial ({})".format(serialnumber))
        logFile.write("\nCould not establish a good API handshake with device serial ({}).\n".format(serialnumber))
        logFile.write(divider)
    else:
        switch = dashboard.devices.getDevice(serial)
        name = switch['name']
        logFile.write("\nDevice {}, with serial {} found.".format(name, serialnumber))
        findRebootTag(refined, serialnumber)

def findRebootTag(goodresponse, serialnumber):
    ports = []
    for device in goodresponse:
        if tag in device['tags']:
            print(device)
            ports.append(str(device['portId']))
        else:
            pass
    print(ports)
    logFile.write("\nDevice serial: {}.\tPorts tagged with {}: {}".format(serialnumber, tag, ports))
    cycle(ports, serialnumber)

def cycle(ports, serialnumber):
    if ports:
        for port_number in ports:
            print("Port number: " + port_number)
        #cycleAll = dashboard.switch.cycleDeviceSwitchPorts(serialnumber, ports) #<--Leave commented if testing
        logFile.write("\nCycling ports {} for device serial {}.\n".format(ports, serialnumber))
        logFile.write(divider)
    else:
        print("No ports tagged with {} found for device serial ({})".format(tag, serialnumber))
        logFile.write("\nNo ports tagged with {} found for device serial ({}).\n".format(tag, serialnumber))
        logFile.write(divider)

#MAIN RUN
tagFile = open("tag.txt", "r")
tag = tagFile.read()
tagFile.close()
logFile = open("logs\{}.txt".format(dt), "w")
logFile.write("Log: Meraki API via Python custom script\n")
with open("device_serials.txt") as txtfile:
    serialtxt = txtfile.read().splitlines()
    for serial in serialtxt:
        if serial:
            getresponse(serial)
        else:
            pass
    logFile.close()