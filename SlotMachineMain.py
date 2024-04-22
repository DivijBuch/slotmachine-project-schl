#imports
from colorama import Fore #creates colour
import pyfiglet #ascii art 
import random  #random module
import time #allows code to wait for a bit

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
  elif symbols.count(3) == 2 and symbols.count(4) == 1:
    return 51
  elif symbols.count(2) == 2 and symbols.count(4) == 1:
    return 51
  elif symbols.count(1) == 2 and symbols.count(4) == 1:
    return 101
  elif symbols.count(2) == 3 :
    return 50
  elif symbols.count(3) == 3:
    return 50
  elif symbols.count(1) == 3:
    return 1000
  elif symbols.count(1) == 2:
    return 100
  elif symbols.count(4) == 3:
    return 500
  elif symbols.count(4) == 2:
    return 50
  elif symbols.count(2) == 2:
    return 50
  elif symbols.count(3) == 2:
    return 50
  elif symbols.count(4) == 1:
    return 1
  else:
    return 0


def main():
  global Coins
  if Coins < 5:
    print(Fore.RED + "you don't have enough money. PLEASE LEAVE")
  else:
    while True:
      liketoSpin = str.upper(input("Would you like to spin(yes or no): "))
      if liketoSpin == "YES":
        print(30*"-")
        Coins = Coins - 5
        print(f'£5 was taken away you now have £{Coins}')
        symbols = rollSymbols()
        earnings = calculateEarnings(symbols)
        displayRoll(symbols)
        time.sleep(1)
        print(f'You earnt £{earnings}')
        Coins = Coins + earnings
        time.sleep(1)
        print(f'You know have £{Coins}')
        print(30*"-")
        main()
        break


      elif liketoSpin == "NO":
        #not finished
        while True:
          cashOut = str.upper(input("Would you like to cash out(yes or no): "))
          if cashOut == "YES":
            name = str(input("What is your name: "))
            highscores = open("highscore.txt","a")
            highscores.write(f'{name}: {Coins} \n')
            highscores.close()
            print("Your score has been saved")
            time.sleep(1)
            print(f'You earnt £{Coins}')
            time.sleep(1)
            print("Thank you for playing Divij's Slot Machine. See you again soon!")
            time.sleep(1)
            break
          elif cashOut == "NO":
            print(f'You earnt £{Coins} but did not want to cash out')
            time.sleep(1)
            print("Thank you for playing Divij's Slot Machine. See you again soon!")
            time.sleep(1)
            break
          else:
            print("Please enter yes or no")

        break
      else:
        print("Please enter yes or no")


#intro
asciiText("Welcome to the Slot Machine")
print(Fore.WHITE + "-"*30)
time.sleep(1)
print(Fore.GREEN + "Game enjoyed best in full screen")
time.sleep(1)
print("Each spin costs 5 coins")
time.sleep(1)
print("Made by Divij")
time.sleep(1)
print(Fore.RED + "HIGH SCORES")
print("-"*30)
highscores = open("highscore.txt", "rt")
print(highscores.read())
highscores.close()
#calls main function
main()
