import sqlite3

# connect to the database
conn = sqlite3.connect('library.db')
c = conn.cursor()

# display menu options
print("1. Add a new member")
print("2. Add a new book")

# get user choice from command line input
choice = input("Enter your choice: ")

if choice == "1":
    # get member details from command line input
    name = input("Enter member name: ")
    email = input("Enter member email: ")
    
    # insert the new member into the Members table
    c.execute("INSERT INTO Members (name, email) VALUES (?, ?)", (name, email))
    conn.commit()
    
    # print confirmation message
    print("Member added successfully.")
    
elif choice == "2":
    # get book details from command line input
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    
    # insert the new book into the Books table
    c.execute("INSERT INTO Books (title, author) VALUES (?, ?)", (title, author))
    conn.commit()
    
    # print confirmation message
    print("Book added successfully.")
    
else:
    print("Invalid choice. Please try again.")

# close the database connection
conn.close()