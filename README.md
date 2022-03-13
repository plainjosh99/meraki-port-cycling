# Meraki-Port-Cycling
 This is a Python3 script for cycling switch ports of a Meraki switch using the Meraki API for Python.
 </br>
## How it works
* It scans the device serial(s) matching those in the *device_serials.txt* file.
* All the ports in that switch that have the tag written in the *tag.txt* file will be cycled.
<br/>
I made it it like this so that I could target specific ports on a switch.


## Requirements
* Python3
* Python package: meraki
* Meraki tag
* Meraki API key
* Meraki device serial(s)

## Caveats
* You will need to create a folder called "logs" in the directory "cycle ports".
* Only works with one tag; modify to your needs if you want a script for multiple tags.

## How to use
1.  Assign a tag to your switch ports in the Meraki dashboard; write this in *tag.txt*
2.  Get the serial number(s) of your Meraki switches; write them in *device_serials.txt*, one serial per line
3.  Attain your API Key in Meraki also
4.  You can assign your API Key to an environmental variable or place it directly into the script, your choice: <br/> ```API_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'```
5.  Assuming you have Python3 installed and the meraki package installed, you can now run *cycle_ports.py* 
6.  Expect a handshake record in the working directory and log(s) for the cycling inside the "logs" folder (see Caveats)
