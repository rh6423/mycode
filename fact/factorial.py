#!/usr/bin/env python
# Initialize an integer variable
f = 1
# collect input as integer
x = int(input("Enter a number: "))

for i in range(1, x+1):
  f = f * i
print(str(x) + '! = ' + str(f))
