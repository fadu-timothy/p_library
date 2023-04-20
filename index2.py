import sqlite3

# connect to the database
conn = sqlite3.connect('library2.db')
c = conn.cursor()

while True:
    # display menu options
    print("\nLIBRARY MENU")
    print("1. Add a new member")
    print("2. Add a new book")
    print("3. List members")
    print("4. List books")
    print("0. Quit")

    # get user choice from command line input
    choice = input("\nEnter your choice: ")

    if choice == "1":
        # get member details from command line input
        name = input("Enter member name: ")
        email = input("Enter member email: ")

        # insert the new member into the Members table
        try:
          c.execute("INSERT INTO Members (name, email) VALUES (?, ?)", (name, email))
          conn.commit()

          # print confirmation message
          print("Member added successfully.")
        except sqlite3.IntegrityError:
          print("Error: Email address already exists.")

    elif choice == "2":
        # get book details from command line input
        title = input("Enter book title: ")
        author = input("Enter book author: ")

        # insert the new book into the Books table
        c.execute("INSERT INTO Books (title, author) VALUES (?, ?)", (title, author))
        conn.commit()

        # print confirmation message
        print("Book added successfully.")

    elif choice == "3":
        # display members in pages of 10
        offset = 0
        while True:
            # get 10 members from the Members table
            c.execute("SELECT name, email FROM Members LIMIT 10 OFFSET ?", (offset,))
            rows = c.fetchall()

            # print the rows
            if len(rows) == 0:
                print("\nNo more members.")
                break
            else:
                print("\nMEMBERS:")
                for row in rows:
                    print(row[0] + " (" + row[1] + ")")

            # check if there are more rows
            c.execute("SELECT COUNT(*) FROM Members")
            count = c.fetchone()[0]
            if offset + 10 < count:
                print("\nPress enter to see the next page.")
                input()
                offset += 10
            else:
                print("\nNo more members.")
                break

    elif choice == "4":
        # display books in pages of 10
        offset = 0
        while True:
            # get 10 books from the Books table
            c.execute("SELECT title, author FROM Books LIMIT 10 OFFSET ?", (offset,))
            rows = c.fetchall()

            # print the rows
            if len(rows) == 0:
                print("\nNo more books.")
                break
            else:
                print("\nBOOKS:")
                for row in rows:
                    print(row[0] + " - " + row[1])

            # check if there are more rows
            c.execute("SELECT COUNT(*) FROM Books")
            count = c.fetchone()[0]
            if offset + 10 < count:
                print("\nPress enter to see the next page.")
                input()
                offset += 10
            else:
                print("\nNo more books.")
                break

    elif choice == "0":
        # quit the program
        break

    else:
        print("Invalid choice. Please try again.")

# close the database connection
conn.close()