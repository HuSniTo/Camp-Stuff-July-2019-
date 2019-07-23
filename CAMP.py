import random

def main():
          print ("This is a simple calculator that can help you with addition.")
          num1 = float(input("Enter your first number: "))
          num2 = float(input("Enter your second number: "))
          solution1 = num1 + num2
          print ("Answer: " + str(solution1))
          if solution1 < 50:
                    print ("That's a pretty small number!")
          else:
                    print ("That's a large number!")
          
if __name__ == "__main__":
          main()
    
