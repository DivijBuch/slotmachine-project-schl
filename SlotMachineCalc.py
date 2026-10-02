import random  #random module
import cProfile
#notes
#Bell= 1
#Cherry= 2
#Bannana= 3 
#Money= 4
#Skull= 5
symbolsSigns = ["Bell","Cherry","Bannana","Money","Skull"]
#set coins value 
Coins = 100



def displayRoll(symbols):
  for i in range(len(symbols)):
    if symbols[i] == 5:
      print(symbolsSigns[4])
    elif symbols[i] == 4:
      print(symbolsSigns[3])
    elif symbols[i] == 3:
      print(symbolsSigns[2])
    elif symbols[i] == 2:
      print(symbolsSigns[1])
    elif symbols[i] == 1:
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
    print("You don't have enough money. PLEASE LEAVE")
  else:
    while True:
      liketoSpin = str.upper(input("Would you like to spin(yes or no): "))
      if liketoSpin == "YES":
        Coins = Coins - 5
        print('£5 was taken away you now have £' , Coins)
        symbols = rollSymbols()
        earnings = calculateEarnings(symbols)
        displayRoll(symbols)
        print('You earnt £' , earnings)
        Coins = Coins + earnings
        print('You know have £' , Coins)
        print(10*"-")
        main()
        break


      elif liketoSpin == "NO":
        #not finished
        while True:
          cashOut = str.upper(input("Would you like to cash out(yes or no): "))
          if cashOut == "YES":
            name = str(input("What is your name: "))
            print("Your score has been saved")
            print('You earnt £' , Coins)
            print("Thank you for playing Divij's Slot Machine.")
            print("See you again soon!")
            break
          elif cashOut == "NO":
            print('You earnt £' , Coins, " but did not want to cash out")
            print("Thank you for playing Divij's Slot Machine")
            print("See you again soon!")
            break
          else:
            print("Please enter yes or no")

        break
      else:
        print("Please enter yes or no")


#intro
print("Welcome to the Slot Machine")
print("Game enjoyed best in full screen")
print("Each spin costs 5 coins")
print("Made by Divij")
cProfile.run('main()', sort='ncalls') # sorting by number of calls