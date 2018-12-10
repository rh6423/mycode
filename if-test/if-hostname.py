#!/usr/bin/env python3
# Ask user for a hostname
hostname = input('Please input a host name: ')
# check whether the hostname provided is a variation of mtg (case insensitive)
# if it is, reassure the user about their config
if hostname.lower() == 'mtg':
  print('the hostname was found to be mtg')
  print('hostname matches expected configuration')
# tell the user the show's over
print('Exiting the script')
