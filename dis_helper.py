import sqlite3
import datetime
import pandas as pd

def sqlite_create_table():
    conn = sqlite3.connect('test.db') # previously 'bs.db'
    c = conn.cursor()
    c.execute('create table if not exists blood_sugar(date_measure_taken text, bs_measure real)')
    c.close()
    conn.close()
    
def sqlite_data_entry(new_data_row):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute('insert into blood_sugar values{}'.format(new_data_row))
    conn.commit() # have to run this after changing the table
    c.close()  # closes the connection to the cursor
    conn.close()

def return_date():
    x = datetime.datetime.now()
    return x.strftime("%Y-%m-%d %H:%M:%S")


def reads_in_bs(bs):
    dtstmp = return_date()
    return "('{}',{})".format(dtstmp, bs)

