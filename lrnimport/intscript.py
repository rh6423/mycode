#!/usr/bin/env python3
from subprocess import call
#import subprocess
call(["ip", "link", "show", "up"])
print("This program will check your interfaces")
interface = input("Enter an interface, like ens3:\n")
call(["ip", "addr", "show", "dev", interface])
call(["ip", "route", "show", "dev", interface])
