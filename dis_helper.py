import sqlite3
import datetime
import pandas as pd

def db_and_table_name_setter(name_of_db, name_of_table):
    return name_of_db, name_of_table


def create_table_for_bs(name_of_db, name_of_table):
    # function for testing and creating bs data table
    conn = sqlite3.connect(name_of_db) # previously 'bs.db'
    c = conn.cursor()
    c.execute('create table if not exists {}(date_measure_taken text, bs_measure real)'.format(name_of_table))
    c.close()
    conn.close()

def create_table_for_food(name_of_db, name_of_table):
    # function for testing and creating bs data table
    conn = sqlite3.connect(name_of_db) # previously 'bs.db'
    c = conn.cursor()
    c.execute('create table if not exists {}(date_measure_taken text, food_consumed text)'.format(name_of_table))
    c.close()
    conn.close()
    
def data_entry(new_data_row, name_of_db, name_of_table):
    conn = sqlite3.connect(name_of_db)
    c = conn.cursor()
    c.execute('insert into {} values{}'.format(name_of_table, new_data_row))
    conn.commit() # have to run this after changing the table
    c.close()  # closes the connection to the cursor
    conn.close()

def return_date():
    x = datetime.datetime.now()
    return x.strftime("%Y-%m-%d %H:%M:%S")


def reads_in_time_and_data(data):
    dtstmp = return_date()
    return "('{}',{})".format(dtstmp, data)

