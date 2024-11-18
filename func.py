
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

# display perfumes
def display_perf():
  print("Options: \n1. View entire collection\n2. Search by scent name\n3. Search by family")
  # add options for search by scent, family, creator, notes, rating


# option menu
def options(firstname):
  print(f'Welcome {firstname};\n Select an option: \n1. View your collection\n2. Add/Remove scents\n3. Check your statistics')
  

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
      options(user[0]) # call option menu
    else: 
      print("incorrect password")
  else:
    print("username not found.")


# menu
def menu():
  if(sign_in == False):
    menuSelect = int(input("menu options:\n1. login \n2. new account\n"))
    if menuSelect == 1:
      login()
    elif menuSelect == 2:
        print("in progress oop")
    else:
      print("Please select a valid option.")
      menu()
# add error handling maybe?
