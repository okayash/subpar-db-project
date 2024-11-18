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
# perfumer insertion

# deletion

# perfume deletion
# perfumer deletion

# modify

# perfume modification
def edit_perfume():
  print("Edit Perfume:")
  # user enters perfume name
    #check if exists in user's collection
  # menu of details to edit


# perfumer modification


# user statistics
def user_statistics():
  print("Below is a list of your usage and rating statistics: \n")


# display perfumes
def display_perf():
  print("Options: \n1. View entire collection\n2. View Search Options")
  # add options for search by scent, family, creator, notes, rating


# option menu
def options(username):
  print(f'Welcome {username};\n Select an option: \n1. View your collection\n2. Add/Remove scents\n3. Check your statistics')

# create a new user
def adduser():
  valid_user = False
  print("Create the following user:\n")
  while (valid_user != True):
    username = input("Username: ")
    mycursor.execute("SELECT * FROM Users WHERE username = (%s)", (username,))
    user = mycursor.fetchone()
    if user:
      print("Invalid username")
    else:
      valid_user = True

  while len(password) < 10:
    password = input("Password: ")    
   
  first_name = input("First name: ")
  print(f"User: {username} successfully created with details: \n{username}\n{password}\n{first_name}")
   
    

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
