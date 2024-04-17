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
symbolsSigns = ["🔔","🍒","🍌","💲","💀"]
#set coins value 
Coins = 100

#functions 
def asciiText(text):
  #creates ascii text
  result = pyfiglet.figlet_format(text)
  print(Fore.RED+ result)


def displayRoll(symbols):
  for i in range(len(symbols)):
    if symbols[i] == 5:
      time.sleep(1)
      print(symbolsSigns[4])
    elif symbols[i] == 4:
      time.sleep(1)
      print(symbolsSigns[3])
    elif symbols[i] == 3:
      time.sleep(1)
      print(symbolsSigns[2])
    elif symbols[i] == 2:
      time.sleep(1)
      print(symbolsSigns[1])
    elif symbols[i] == 1:
      time.sleep(1)
      print(symbolsSigns[0])

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
  else:
    while True:
      liketoSpin = str.upper(input(Fore.WHITE + "Would you like to spin(yes or no): "))
      if liketoSpin == "YES":
        #code for like to spin
        print("PLAYER WOULD LIKE TO SPIN")
        break
      elif liketoSpin == "NO":
        #player would not like to spin
        while True:
          cashOut = str.upper(input("Would you like to cash out(yes or no): "))
        break
      else:
        print("Please enter yes or no")    
      
    
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