#!/usr/bin/env python3
import netifaces

def gimmieip(iface):
    print('IP :', end='')
    print((netifaces.ifaddresses(iface)[netifaces.AF_INET][0]['addr']))

def gimmiemac(iface):
    print('MAC :', end='')
    print((netifaces.ifaddresses(iface)[netifaces.AF_LINK][0]['addr']))

def main():
    print(netifaces.interfaces())
    for i in netifaces.interfaces():
        print('\n**************Details of Interface - ' + i + ' *********************')
        try:
            print('MAC :', end='')
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK][0]['addr']))
            print('IP :', end='')
            print((netifaces.ifaddresses(i)[netifaces.AF_INET][0]['addr']))
        except:
            print('Could not collect adapter information')
    myinterface = input('Input an interface to get an IP: ')
    gimmieip(myinterface)
    
    myinterface = input('Input an interface to get a MAC: ')
    gimmiemac(myinterface)
main()
