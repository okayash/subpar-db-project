# query functions

import mysql.connector

# connect details here
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Heiskanen pass",
    database="perfumedb"
)


mycursor = db_connection.cursor()
sign_in = False


# login
def login():
  username = input("username: ")
  mycursor.execute("SELECT * FROM Users WHERE username = (%s)", (username,)) # select usernames matching inputs
  user = mycursor.fetchone()

  if user:
    password = input("password: ")

    if user[2] == password: # check stored passwords
      print("successfully logged in!")
      sign_in = True # user has successfully signed in
      return user[3]

    else:
      print("incorrect password")
      login()
  else:
    print(f"username {username} not found.")
    login()


# insertion
# perfume insertion
def insert_perfume():
  print("You are inserting a perfume: ")

# perfumer insertion
def insert_perfumer():
  print("You are inserting a perfumer: ")

# deletion

# perfume deletion
def remove_perfume():
  print("You are a removing a perfume")

# modify

# perfume modification
def edit_perfume():
  print("Edit Perfume:")
  perf_search = input("Which perfume would you like to edit?")
  # user enters perfume name
    #check if exists in user's collection
  # menu of details to edit

# user statistics
def user_statistics():
  print("Below is a list of possible usage and rating statistics to view: \n")
  # most commonly used notes
  # avg rating by base note


def perfume_statistics():
  print("Below is a list of your collection statistics: \n")
  # show perfumes in each line

def global_statistics():
  # shows global stats for a perfume
  search_perfume = input("Enter the name of a perfume to view global usage statistics")
  # then display avg rating (mostly positive, mostly negative, mixed)
  
  # print all users who own this perfume
  

# display perfumes
def display_perf(username):
  display_options = int(input("Options: \n1. View your entire collection\n2. View Search Options\n3. View all perfumes in database:\n"))
  # add options for search by scent, family, creator, notes, rating, line
  while display_options not in [1,2,3]:
    display_options = int(input("Please select a valid input: "))
  
  match display_options:
    case 1:
      print(f"Displaying perfumes for {username}")
    case 2:
      print("Call search function here")
    case 3:
      print("Displaying all perfumes in database")


# option menu
def options(username):
  option = int(input(f'Welcome {username};\n Select an option: \n1. View your collection\n2. Add/Remove scents\n3. Check your statistics\n4.Check statistics among users\n'))
  while option not in [1,2,3,4]:
    print("Please select one of the options.\n")
    option = int(input("Selection:\n"))

  match option:
    case 1:  
      display_perf(username)
    case 2:
      details_options = int(input("Here, you can select to\n1. Add a scent\n2. Modify an existing scent\n3. Remove a scent:\n"))
      while(details_options < 1 or details_options > 3):
        details_options = int(input("Please select a valid option:\n"))
 
      if(details_options == 1):
        insert_perfume()
      elif(details_options == 2):
        modify_perfume()
      elif(details_options == 3):
        remove_perfume()
    case 3:
      perfume_statistics()
    case 4:
      global_statistics()
      

# create a new user
def adduser():
  valid_user = False
  valid_password = False

  print("Create the following user:\n")
  while not valid_user:
    username = input("Username: ")
    mycursor.execute("SELECT * FROM Users WHERE username = (%s)", (username,))
    user = mycursor.fetchone()
    if user:
      print("Invalid username")
    else:
      valid_user = True

  while not (valid_password):
    password = input("\nPassword (10 characters or more): ")    
    if(len(password) < 10):
      print("Invalid password\n")
    else:
      valid_password = True

      first_name = input("First name: ")

  try:
      sql = "INSERT INTO Users (username, password, first_name) VALUES (%s, %s, %s)"
      values = (username, password, first_name)
      mycursor.execute(sql, values)
      db_connection.commit()
      print(f"User: {username} successfully created with credentials: \nUsername: {username}\nFirst Name: {first_name}")
  
  except mysql.connector.Error as err:
      print(f"An error occurred: {err}")   
    

# menu
def menu():
  if(sign_in == False):
    menuSelect = int(input("menu options:\n1. login \n2. new account\n"))
    if menuSelect == 1:
      user = login()
      return user
    elif menuSelect == 2:
        adduser()
    else:
      print("Please select a valid option.")
      menu()

# add error handling maybe?


def sign_out():
  print("signing user out...")
