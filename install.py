import mysql.connector

print("Installing dependencies...")

print("Adding data...")

import mysql.connector

print("Installing dependencies...")

# Connect to MySQL server
try:
    connection = mysql.connector.connect(
        host="localhost",      
        user="root",           
        password="Heiskanen pass"  
    )
    cursor = connection.cursor()

    print("Adding data...")
    with open("populate.sql", "r") as sql_file:
        sql_commands = sql_file.read()

    # Execute SQL commands
    for command in sql_commands.split(";"):
        if command.strip():
            try:
                cursor.execute(command)
            except mysql.connector.Error as cmd_err:
                print(f"Command error: {cmd_err}")
                print(f"Failed SQL: {command}")

    connection.commit()  
    print("Database setup completed successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()

