# 

import func

def main():
  username = func.menu()
  exit = '0'

  while exit != 'x':
    if username:
      func.options(username)
    
    exit = input("Would you like to continue? a. Press 'x' to quit program, or any other key to continue managing your collectiom.\n")
   
  print("Program exited")
   
  # add a while loop that terminates after ?? then signs out
if __name__ == "__main__":
    main()

