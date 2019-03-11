import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def task_5_pie(conn, c):
    # Purpose: Create a pie chart of the top 5 most popular areas, 
    # popularity comes from the number of papers under the area. 
    # If there are less than 5 areas, show pie chart of however many 
    # areas that exist.
    #
    # Parameters: Takes the connection to the database and the cursor
    #
    # Return: None
    
    c.execute('SELECT COUNT(*) FROM areas;')
    num_of_areas = c.fetchone()
    
    # Joins papers and areas where name from areas is equal to area from papers
    # and group by area name. Orders by number of papers per area in descending
    # order.
    df = pd.read_sql_query('SELECT name,COUNT(*) as count FROM areas, \
    papers WHERE name = area GROUP BY name ORDER BY count DESC;', conn)
    
    if num_of_areas[0] > 5:
        df = df.iloc[0:5,:] # takes first 5 rows if there are more than 5 areas

    plot = df.plot.pie(labels = df.name,y = 'count')
    plt.plot()
    plt.show()
    
    return