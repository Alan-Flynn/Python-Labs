##### bunco_proc.py #####
import random

#Create the empty list for what the dice rolls will be
player1_dice = []
player2_dice = []

#Makes the random operations to give random values to the first two dice rolls
for i in range(2):
  player1_dice.append(random.randint(1,6))
  player2_dice.append(random.randint(1,6))
from random import randint 

class Player:
  def __init__(self):
    self.dice = []
 
  def roll(self):
    self.dice = [] # clears current dice
    for i in range(2):
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice

#Defines both player1 and player2 both of the player class
player1 = Player()
player2 = Player()
 
player1.roll()
player2.roll()

def print_results():
  print("Player 1 rolled" + str(player1.get_dice()))
  print("Player 2 rolled" + str(player2.get_dice()))

#While the sum of the two values rolled doesn't equal 2 they can't both be 1s
while sum(player1.get_dice()) != 2 and sum(player2.get_dice()) != 2:
  print_results()
  print("Roll again")
  #This performs the roll operation again until one of the players win
  player1.roll()
  player2.roll()

#If the of the two values rolled for both are equal to each other and 2 then it is a draw 
if sum(player1.get_dice()) == sum(player2.get_dice()) and sum(player1.get_dice()) == 2:
  print_results()
  print("Draw!")
  player1.roll()
  player2.roll()

#If player1's values total 2 and player2's don't then they player 1 wins and the roll operation will not be performed again
elif sum(player1.get_dice()) == 2 and sum(player2.get_dice()) != 2:
  print_results()
  print("Player 1 wins")

#If player1's values total 1 and player2's don't then they player 2 wins and the roll operation will not be performed again 
elif sum(player2.get_dice()) == 2 and sum(player1.get_dice()) != 2:
  print_results()
  print("Player 2 wins")


##### player_class.py #####




