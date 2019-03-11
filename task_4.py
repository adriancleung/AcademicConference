import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def t4_main(conn, c):
    # Purpose: implements two options for displaying the number of sessions
    # authors participate in:
    # 1) displays a bar plot of all authors and how many sessions they participate in
    # 2) displaying a single specified author and their number of sessions
    #       included in option 2 is a sub-option to display all authors
    #
    # Parameters: takes the connection to the database and the cursor
    #
    # Return: None
    
    query = '''select author, count(distinct(csession)) as count
    from  papers 
    group by author;'''
    
    df = pd.read_sql_query(query, conn) #This df contains two columns: "author" and "count"
    
    
    print('''
=== (Task 1) Show how many sessions authors participate in ===
There are two options for display:
(1) a bar plot of authors and number of sessions
(2) select an author and view their number of sessions
''')
    
    while True:
        option = input("Which option would you like to display? Enter 1 or 2. ")
    
        if option == '1':
            # This part displays a bar plot of all authors
            # and # of sessions in dataframe
            plot = df.plot.bar(x = "author", rot = 0)
            
            plt.plot()
            plt.show()
            
        elif option == '2':
            # This part either displays all authors or displays the number of 
            # sessions for a single specified author (specified by email)
            
            authors = df["author"]
            name = input('''
Which author would you like information about?
Enter the Email of an author or enter "authors" to see a list of authors.
''')
            
            if name == "authors":
                for item in authors:
                    print(item)
            elif name in authors.values:
                print(df[df.author == name])
            else:
                print("Invalid author name.")
                break
            
        else:
            print("Invalid input.")
    
        x = input("Would you like to display another option? y/n. ")
        if x == "n":
            break
        if x != "y":
            print("Invalid option.")
            break
        
    return

    