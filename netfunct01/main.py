#!/usr/bin/env python3

# function to push commands
def commandpush(devicecmd): # devicecmd==list 
    for coffeetime in devicecmd.keys():
        # print blank line at start of block
        print()
        # print message with name of device
        print('Handshaking. .. ... connecting with ' + coffeetime )
        # we'll learn to write code that connects to devices here
        for mycmds in devicecmd[coffeetime]:
            print('Attempting to sending command --> ' + mycmds )
            # we'll learn to write code that sends cmds to device here

def devicereboot(devtoreboot): # devtoreboot = ipaddress list
    print()
    print('Starting reboots...')
    for device in devtoreboot:
        print('connecting to', device)
        print('REBOOTING NOW!\n')

### Start our script
# populate work2do with dictionary list of devices and commands
work2do = {"10.1.0.1":["interface eth1/2", "no shut"], "10.2.0.1":["interface eth1/1", "shutdown"], "10.3.0.1":["interface eth1/5", "no shutdown"]} # data that replaces data stored in file

# populate rebootlist with some IPs
rebootlist = ['1.2.3.4', '5.6.7.8', '9.10.11.12']

print("Welcome to the network device command pusher") # welcome message

## get data set
print("\nData set found\n") # replace with function call that reads in data from file

## run 
commandpush(work2do) # call function to push commands to devices
devicereboot(rebootlist) # call function to reboot devices
