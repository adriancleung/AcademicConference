import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def task_6_bar(conn, c):
    # Purpose: For each reviewer, give a bar chart of their average review 
    # scores for each category. You must return a single grouped bar chart.
    #
    # Parameters: Takes the connection to the database and the cursor
    #
    # Return: None
    
    # Query returns the reviewer's email address and their average scores
    # for each category by grouping each reviewer from the table reviews
    df = pd.read_sql_query('SELECT reviewer, AVG(originality) as Originality,\
    AVG(importance) as Importance, AVG(soundness) as Soundness, AVG(overall)\
    as Overall FROM reviews GROUP BY reviewer;', conn)
    
    # rot = 0: rotates the axes to horizontal
    # figsize = (14, 7): expands the window size of the chart
    df.plot.bar(x = 'reviewer', rot = 0, figsize = (14,7))
    plt.plot()
    plt.show()
    
    return