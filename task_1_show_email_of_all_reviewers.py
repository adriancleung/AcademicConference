import math
import sqlite3
import pandas as pd

def email_of_reviewers(connection, cursor):
    # Purpose: Shows all papers and allow one to be selected. Once a paper is
    #          selected, show the email of all reviewers that have reviewed the paper
    # Parameters: Passes connected db and cursor
    # Return: None   
    
    df = pd.read_sql_query("select * from papers;", connection)
    cursor.execute("select * from papers;")	
    rows = cursor.fetchall() 
    
    print("\n=== (Task 1) Showing the email of all reviewers that have reviewed the paper ===")
   
    i = 0; j = 0; k = 5; page = 1; # temporary variables for indexing titles/page 
    while True:
        i = j        
        print("=== List of paper titles ("+ str(page) +"/" + \
              str(math.ceil(len(rows)/5))+ " Pages) ===")
        
        for i in range(j, k):
            if i > len(rows) - 1: # When there is no more titles to display
                print() 
            else:
                print("(", df["Id"][i], ") ",  df["title"][i], sep = '')  
        
        print("\n(p) Previous page or (n) Next page\n(q) Quit this task\n")
        user_input = str(input('Select a paper number or enter a command: '))
        
        if user_input.lower() == 'q': # For quitting
            return
        
        elif user_input.lower() == 'n' and k <= len(rows): # For next page
            j += 5; k += 5; page += 1;
        
        elif user_input.lower() == 'p' and j > 0: # For previous page 
            j -= 5; k -= 5; page -= 1;
        
        elif user_input.isnumeric() and int(user_input) > 0 and \
             int(user_input) <= len(rows): # When a valid paper is selected
            
            cursor.execute('''SELECT reviewer FROM reviews WHERE paper = :num;''', \
                           {"num" : (int(user_input))})     
            
            reviewers = cursor.fetchall()
            print('\n=== Email of reviewers for this paper, ('\
                  + user_input +') "'+ df["title"][int(user_input)-1]+'" ===')
            
            if not reviewers: # When no reviewers
                print("\nThere are no reviewers for this paper")
            else:
                for reviewer in reviewers:
                    print(reviewer)
            return
       
        else: # Catches any other errors
            print("Invalid command. Please try again")
        print("\n")

