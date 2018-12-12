#!/usr/bin/env python3
# create list of parameter names/keys
paramlist = ['OS_AUTH_URL', 'OS_IDENTITIY_API_VERSION', 'OS_PROJECT_NAME', 'OS_PROJECT_DOMAIN_NAME', 'OS_USERNAME', 'OS_USER_DOMAIN_NAME']

# open csv file to read
sourcefile = open('csv_users.txt', 'r')

# open file to write
configfile = open('brokenstack.conf', 'w')
# iterate through lines in sourcefile
for line in sourcefile.readlines():
    paramvalue = [line.split(",")]
    for i in range(0,6):
        print(i)
        print(paramlist[i])
        value=paramvalue.index(i)
        print(value)
        configfile.write("export " + str(paramlist[i]) + "=" + str(paramvalue[i]) + "\n")
# close the files
configfile.close()
sourcefile.close()
