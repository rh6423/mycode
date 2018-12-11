#!/usr/bin/env python3
# initialize counter
round = 0
# start an infinite loop
while(True):
  round = round + 1
  print('Finish the movie title, "Monty Python\'s The Life of _____"')
  answer = input()
  lcanswer = answer.lower()
  if (lcanswer == "brian"):
    print('Correct')
    break
  elif (lcanswer == "shrubbery"):
    print('You gave the super secret answer')
    break
  elif (round == 3):
    print('Sorry, the answer was Brian')
    break
  else:
    print('Sorry, try again')

