# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

import random
import math

def name_to_number(name):
        
    if name == "rock":
      player_number = 0
      return player_number
    elif name == "Spock":
      player_number = 1
      return player_number
    elif name == "paper":
      player_number = 2
      return player_number
    elif name == "lizard":
      player_number = 3
      return player_number
    elif name == "scissors":
      player_number = 4
      return player_number
    else:
      return "This is not a correct choice"

def number_to_name(number):
   
    if number == 0:
      comp_choice = "rock"
      return comp_choice
    elif number == 1:
      comp_choice = "Spock"
      return comp_choice
    elif number == 2:
      comp_choice = "paper"
      return comp_choice
    elif number == 3:
      comp_choice = "lizard"
      return comp_choice
    elif number == 4:
      comp_choice = "scissors"
      return comp_choice
    else:
      return "This is not a correct choice"
def rpsls(player_choice): 
    print " "
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice  
    
    difference = (player_number - comp_number) % 5
    
    
    if (difference == 1) or (difference == 2): 
        print "Player wins!"
    elif (difference == 3) or (difference == 4):
        print "Computer wins!"
    
    elif difference == 0:
        print "Player and computer tie!"
    else:
        print "You have selected an incorrect choice!" 
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")


