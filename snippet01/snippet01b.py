#!/usr/bin/env python3

def getlastip(x):
    y = x + 10
    if y > 255:
      return(False)
    else:
      return(y)

def main():
    startaddr = str()
    print("This program reserves a block of 10 IP addresses\n")
    print("Enter a starting IP address")
    startaddr = input()
    startaddr = startaddr.split(".")
    print(startaddr)
    firstip = int(startaddr[3])
    lastip = getlastip(firstip)
    lastaddr = startaddr
    lastaddr
