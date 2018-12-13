#!/usr/bin/env python3
# use random integer generator
from random import randint

# define a class for a regular player who does not cheat. underneath that
# we define the methods for the class (__init__ is housekeeping requirement,
# the rest are the ones we actually use
class Player:
  def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3): # do three rolls
      self.dice.append(randint(1,6)) # each roll is random number 1-6

  def get_dice(self):
    return self.dice

# define class for first kind of cheater. 
class Cheat_Swapper(Player):
  def cheat(self):
    self.dice[-1] = 6 # change third number in the list of rolls to 6

class Cheat_Loaded_Dice(Player):
  def cheat(self):
    i = 0
    while i < len(self.dice): # do this for each roll of the dice
      if self.dice[i] < 6: # if the random roll is less than six
        self.dice[i] += 1 # add one to the rolled number
      i += 1
