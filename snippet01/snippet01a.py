#!/usr/bin/env python3
# open file for reading
myfile = open("txtfile.txt", "r")
# read one line as a string
lines = myfile.readline()
# convert string to list without return on the end
wordlist = lines.strip("\n").split(" ")
# join list items with tabs in between
wordlist = "\t".join(wordlist)
# print the output
print(wordlist)
# close the file
myfile.close()
