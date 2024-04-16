#imports
from colorama import Fore #creates colour
import pyfiglet #ascii art 
import random  #random module
import time #allows code to wait for a bit
import sys #exits code

#notes
#🔔= 1
#🍒= 2
#🍌= 3 
#💲= 4
#💀= 5

#set coins value 
Coins = 100

#functions 
def asciiText(text):
  #creates ascii text
  result = pyfiglet.figlet_format(text)
  print(Fore.RED+ result)

def rollSymbols():
  #rolls random symbols
  symbolsGiven = [random.randint(1,5),random.randint(1,5),random.randint(1,5)]
  return symbolsGiven

def calculateEarnings(symbols):
  #calculates what the player has earnt
  if symbols.count(5) == 1:
    return 0 
  elif symbols.count(2) == 3 or symbols.count(3) == 3:
    return 50
  elif symbols.count(1) == 3:
    return 1000
  elif symbols.count(1) == 2:
    return 100
  elif symbols.count(1) == 2 and symbols.count(4) == 1:
    return 101
  elif symbols.count(4) == 3:
    return 500
  elif symbols.count(4) == 2:
    return 50
  elif symbols.count(2) == 2 or symbols.count(3) == 2:
    return 50
  elif symbols.count(2) == 2 and symbols.count(4) == 1:
    return 51
  elif symbols.count(3) == 2 and symbols.count(4) == 1:
    return 51
  elif symbols.count(4) == 1:
    return 1

def main():
  #main game
  if Coins < 5:
    print(Fore.RED + "You do not have enough money please leave")
    
    
#intro
asciiText("Welcome to the Slot Machine")
print(Fore.WHITE + "-"*30)
print(Fore.GREEN + "Game enjoyed best in full screen")
print("Each spin costs 5 coins")
print("Made by Divij")
print(Fore.RED + "HIGH SCORES")
print("-"*30)
highscores = open("highscores.txt", "rt")
print(highscores.read())
highscores.close()
#calls main function
main()