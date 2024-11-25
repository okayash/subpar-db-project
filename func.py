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

# --------------------- login ---------------------
# login
def login():
  sign_in = False
  while not sign_in:
    username = input("username: ")
    mycursor.execute("SELECT * FROM Users WHERE username = (%s)", (username,)) # select usernames matching inputs
    user = mycursor.fetchone()

    if not user:
      print(f"username {username} not found.")
      continue
  
    attempts = 0  
    while attempts < 5:
      password = input("password: ")

      if user[2] == password: # check stored passwords
        print("successfully logged in!")
        sign_in = True # user has successfully signed in
        return (user[0])
        break
    
      else:
        print("Incorrect password")
        attempts += 1
    
    print("Login attempts exceeded. Exiting.")
    return None


# --------------------- queries ---------------------


# print user's perfume list
def print_user_perfume(username):
   print(f"\n{username}'s perfumes:\nname		rating")
   mycursor.execute("SELECT fname, rating FROM Fragrance WHERE username = (%s)", (username,))
   for x in mycursor:
     print(x)

def print_global_perfumes():
  print(f"\nAll perfumes in database:\n")
  mycursor.execute("SELECT Distinct fname FROM Fragrance")
  for x in mycursor:
    print(x)  

# search perfumes , need to join frag and perf_details
def search_perfumes(username):
  search = input("Search a perfume by name: \n")
  mycursor.execute("SELECT * FROM Fragrance WHERE fname = (%s) AND username = (%s)", (search,username,))
  matches = mycursor.fetchone()
  if matches:
    for x in mycursor:
      print(x)
  
  else:
    print("No results found")

# insertion
# perfume insertion
def insert_perfume(username):
  print("You are inserting a perfume: ")
  name = input("Enter perfume name: ")
  mycursor.execute("SELECT * FROM Fragrance WHERE fname = (%s) AND username = (%s)", (name,username,))  
  existing_perfume = mycursor.fetchone()
  if existing_perfume:
    print("Perfume already exists!\n")
    return
  
  try:
    sql = "INSERT INTO Fragrance (fname, username) VALUES (%s, %s)"
    values = (name, username)
    mycursor.execute(sql, values)
    db_connection.commit()
    print(f"Fragrance successfully created with name: \n{name}\nAdd additional details using the modify perfume option.")

  except mysql.connector.Error as err:
    print(f"An error occurred: {err}")

# perfumer insertion
def insert_perfumer():
  print("You are inserting a perfumer: ")
  name = input("Name of Perfumer:\n")
  mycursor.execute("SELECT * FROM Perfumer WHERE pfname = (%s)", (name,))
  existing_perfumer = mycursor.fetchone()
  if existing_perfumer:
    print("Perfumer already exists")
    return
 
  company = input("Enter a company name: \n")
  
  try:
    sql = "INSERT INTO Perfumer (pfname, pcompany) VALUES (%s, %s)"
    values = (name, company)
    mycursor.execute(sql, values)
    db_connection.commit()
    print(f"\nPerfumer added into database with Name: {name} and Company: {company}\n")

  except mysql.connector.Error as err:
    print(f"An error occurred: {err}")


# deletion

# perfume deletion
def remove_perfume(username):
  print("You are a removing a perfume")
  name = input("Name of perfume to delete:\n")
  mycursor.execute("SELECT * FROM Fragrance WHERE fname = (%s) AND username = (%s)", (name,username,))
  remv_perfume = mycursor.fetchone()
  
  if remv_perfume:
    try: 
      sql = "DELETE FROM Fragrance WHERE fname = (%s) AND username = (%s)"
      values = (name, username)
      mycursor.execute(sql, values)
      db_connection.commit()
      print(f"{name} has been removed.\n")

    except mysql.connector.Error as err:
      print(f"An error occurred: {err}")

  else:
    print("Nothing to delete")
    return

# modify

# perfume modification
def edit_perfume():
  print("Edit Perfume:")
  perf_search = input("Which perfume would you like to edit?")
  # user enters perfume name
  mycursor.execute("SELECT * FROM Fragrance WHERE fname = (%s) AND username = (%s)", (perf_search, username))
  perfume_instance = mycursor.fetchone()

  if perfume_instance:
    print(f"Editing perfume: {perf_search}\nSelect a detail to edit: \n1. Edit Rating\n2. Edit Base Note\n3. Edit Family\n4. Cancel")
    option = input("Enter option number: ")
    if option == '1':
      new_rating = input("Enter new rating (1-5): ")
      mycursor.execute("UPDATE Fragrance SET rating = (%s) WHERE fname = (%s) AND username = (%s)", (new_rating, perf_search, username))
      db_connection.commit()
      print(f"Rating for {perf_search} updated to {new_rating}.")

    elif option == '2':
      new_base_note = input("Enter new base note: ")
      mycursor.execute("UPDATE PerfumeDetails SET base_note = (%s) WHERE fname = (%s)", (new_base_note, perf_search))
      db_connection.commit()
      print(f"Base note for {perf_search} updated to {new_base_note}.")

    elif option == '3':
      new_family = input("Enter new family: ")
      mycursor.execute("UPDATE PerfumeDetails SET family = (%s) WHERE fname = (%s)", (new_family, perf_search))
      db_connection.commit()
      print(f"Family for {perf_search} updated to {new_family}.")

    elif option == '4':
      print("Edit cancelled.")
  else:
    print(f"Perfume {perf_search} not found in your collection.")
    #check if exists in user's collection
  # menu of details to edit

# user statistics
def user_statistics():
  print("Below is a list of possible usage and rating statistics to view: \n")
  # most commonly used notes
  # avg rating by base note
  
  print(f"Your most common base note is: \n")
  
  print("Your average rating: ")
  mycursor.execute("""
        SELECT fname, AVG(rating) as avg_rating
        FROM Fragrance
        WHERE username = (%s)
        GROUP BY fname""", (username,))
  results = mycursor.fetchall()

  print("Average rating for each perfume in your collection:")
  for x in results:
    print(f"{x[0]}: {x[1]:.2f}")

def perfume_statistics():
  print("Below is a list of your collection statistics: \n")
  # most commonly used base note
  mycursor.execute(""" SELECT base_note, 
  
        """, (username))
  common_bnote = mycursor.fetchone()
  if common_bnote:
    print(f"Your most commonly used base note was: {common_bnte[0]}")
  else: 
    print(f"You do not have any commonly used base notes.")
  # most commonly used family
  mycursor.execute("""
        SELECT family, COUNT(*) as count
        FROM Perfume_Details
        JOIN Fragrance ON Perfume_Details.fname = Fragrance.fname
        WHERE Fragrance.username = %s
        GROUP BY family
        ORDER BY count DESC
        """, (username,))
  common_fam = mycursor.fetchone()
  if common_fam:
    print(f"Your most commonly used family is: {common_fam[0]}")
  else:
    print(f"You do not have any commonly used families.")
 
def global_statistics():
  # shows global stats for a perfume
  search_perfume = input("Enter the name of a perfume to view global usage statistics\n")
  # then display avg rating (mostly positive, mostly negative, mixed)
 
  mycursor.execute("""
        SELECT AVG(rating) as avg_rating
        FROM Fragrance
        WHERE fname = (%s)""", (search_perfume,))
  result = mycursor.fetchone()

  if result:
    print(f"Global average rating for {search_perfume}: {result[0]:.2f}")
    if result[0] > 5:
       print("Mostly positive")
    elif result[0] == 5:
       print("Mixed ratings")
    else:
       print("Mostly negative")
    print("Owned by: ")
    
    mycursor.execute("""
        SELECT username
        FROM Fragrance
        WHERE fname = (%s)
    """, (search_perfume,))
    owners = mycursor.fetchall()
    for x in owners:
      print(f"- {x[0]}")
      
  else:
    print(f"No global data found for {search_perfume}.")
  

# display perfumes
def display_perf(username):
  display_options = int(input("Options: \n1. View your entire collection\n2. View Search Options\n3. View all perfumes in database:\n"))
  # add options for search by scent, family, creator, notes, rating, line
  while display_options not in [1,2,3]:
    display_options = int(input("Please select a valid input: "))
  
  match display_options:
    case 1:
      print(f"Displaying perfumes for {username}")
      print_user_perfume(username)
    case 2:
      search_perfumes(username)
    case 3:
      print("Displaying all perfumes in database")
      print_global_perfumes()

# display a list of all perfumers
def perfumer_data():
  mycursor.execute("SELECT Distinct pfname FROM Perfumer")
  for x in mycursor:
    print(x)

# --------------------- user menus ---------------------
# option menu
def options(username):
  # get first name of user
  mycursor.execute("SELECT * FROM Users WHERE username = (%s)", (username,)) # select usernames matching inputs
  user = mycursor.fetchone()

  option = int(input(f'\nWelcome {user[3]};\n Select an option: \n1. View your collection\n2. Add/Remove scents\n3. Check your statistics\n4.Check statistics among users\n'))
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
        insert_perfume(username)
      elif(details_options == 2):
        modify_perfume()
      elif(details_options == 3):
        remove_perfume(username)
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

      return username

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
       newuser = adduser()
       return newuser
    else:
      print("Please select a valid option.")
      menu()

# add error handling maybe?


def sign_out():
  print("signing user out...")
