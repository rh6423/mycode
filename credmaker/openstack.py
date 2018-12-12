#!/usr/bin/env python3
# create list of parameter names/keys
paramlist = ['OS_AUTH_URL', 'OS_IDENTITIY_API_VERSION', 'OS_PROJECT_NAME', 'OS_PROJECT_DOMAIN_NAME', 'OS_USERNAME', 'OS_USER_DOMAIN_NAME', 'OS_PASSWORD']

# open file to write
#configfile = open('~/mycode/credmaker/brokenstack.conf', 'w')
configfile = open('brokenstack.conf', 'w')
# tell user how to input
print("Please enter each parameter enclosed in brackets - <value>")
# iterate through the list for input
for parameter in paramlist:
#    print("Value for " + parameter + "? ")
    paramvalue = input("Value for " + parameter + "? ")
    configfile.write("export " + parameter + "=" + paramvalue + "\n")
# close the file
configfile.close()
