#!/bin/python3
import random
import time

start = input ("Start? (Y/N)")

if start == 'N':
  print ("You selected N, the coin flip will not start!")
elif start == 'Y':
  print ("You selected Y, the coin flip will now start!")
  time.sleep (1)
  print ("It's fliping!")
  time.sleep (2)
  def flip():
      result = random.randint(1,2)
  
      if result == 1:
          print ("The result is Heads!")
      else:
          print ("The result is Tails!")

  for x in range(0, 1):
      flip()
