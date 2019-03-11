import string
import sqlite3
import pandas as pd
import sys
import matplotlib.pyplot as plt
import task_1_show_email_of_all_reviewers as t1
import task_2_show_potential_reviewers as t2
import task_3_reviewers_in_range as t3
import task_4 as t4
import task_5_pie as t5
import task_6_bar as t6

def main():
    # Purpose: Connect to db and calls menu
    # Parameters: Takes no parameters
    # Return: None 
    
    path = './' + str(sys.argv[1])
    conn = sqlite3.connect(path)
    c = conn.cursor()
    c.execute('PRAGMA foreign_keys=ON;')
    
    menu(conn, c)
    
    conn.commit()
    conn.close()
    
    return 0

def menu(conn, c):
    # Purpose: Prints out the menu for the program
    # Parameters: Passes connected db and cursor
    # Return: None
    
    while True: 
        print('''
=== Assignment 3 Project ===
(1) Show the email of all reviewers that have reviewed the paper
(2) Show all potential reviewers for that paper
(3) Find all reviewers whose number of reviews is in that range
(4) Show in how many sessions do authors participate in
(5) Top 5 most popular areas
(6) A bar chart of their average review scores for each category
        
(q) Quit
''')
        
        user_input = str(input('Enter command: '))
        option_lst = ['1', '2', '3', '4', '5', '6', 'q']
        
        if user_input not in option_lst:
            print('\nInvalid command. Please enter again')
        else:
            if user_input == '1':
                t1.email_of_reviewers(conn, c)
            if user_input == '2':
                t2.potential_reviewers(conn, c)
            if user_input == '3':
                t3.reviewers_in_range(conn, c)
            if user_input == '4':
                t4.t4_main(conn, c)
            if user_input == '5':
                t5.task_5_pie(conn, c)
            if user_input == '6':
                t6.task_6_bar(conn, c)
            if user_input == 'q':
                break
            
main()