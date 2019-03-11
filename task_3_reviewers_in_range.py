import sqlite3

def reviewers_in_range(connection, cursor):
    # Purpose: Takes as user input two integers representing upper and lower bounds,
    # returns all reviewers whose total number of reviews falls in that range
    # 
    # Parameters: Takes the connection to the database and the cursor
    #
    # Return: None
        
    x = int(input("Enter the lower bound: "))
    y = int(input("Enter the upper bound: "))
        
    statement = ("SELECT DISTINCT reviewer, COUNT(*) FROM reviews GROUP BY reviewer HAVING COUNT(*) >= " + str(x) + " and COUNT(*) <= "+ str(y)+ ";")
    
    row = cursor.execute(statement)
    
    connection.commit()
    
    print("\nThe reviewers with papers in this range are: ")
    for item in row:
        print(item)
    print("\n")
    
    return