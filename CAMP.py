import random

def main():
          print("Welcome to the random number guesser, guess the chosen number between 1 and 10")
          answer = random.randint(1,10)
          tries = 4
          while (tries > 0):
                    guess = int(input("Guess a number: "))
                    if answer == guess:
                              print ("You got it!")
                              break
                    else:
                              if guess > answer:
                                        print ("Your guess is too high!")
                              else: print ("Your guess was too low")
                              tries = tries - 1
                              print("You have " + str(tries) + " tries left")
          if tries == 0:
                    print ("Game over! Try again!")
if __name__ == "__main__":
          main()
    
