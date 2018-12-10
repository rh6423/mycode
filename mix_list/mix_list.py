#!/usr/bin/env python3

# populate a list
my_list = [ "192.168.0.5", 5060, "UP" ]
# print the IP
print ("The first item in the list (IP): " + my_list[0] )
# print the port (type it from integer to string)
print ("The second item in the list (port): " + str(my_list[1]) )
# print the state
print ("The last item in the list (state): " + my_list[2] )

new_list = [5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

print ("When I " + new_list[5] + " from " + new_list[4] + " to " + new_list[3] + " on ports " + new_list[1] + ", " + str(new_list[0]) + ", or " + str(new_list[2]) + ", it never works.")
