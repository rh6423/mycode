#!/usr/bin/env python3
loginfail = 0
# open log file for reading
keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi','r')
keystone_file_lines = keystone_file.readlines()
for i in range(len(keystone_file_lines)):
    if "- - - - -] Authorization failed" in keystone_file_lines[i]:
        loginfail = loginfail + 1
print("The number of failed login attempts is " + str(loginfail))
