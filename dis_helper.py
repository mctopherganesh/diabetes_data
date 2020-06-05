import sqlite3
import datetime
import pandas as pd

def db_and_table_name_setter(name_of_db, name_of_table):
    return name_of_db, name_of_table


def sqlite_create_table(name_of_db, name_of_table):
    conn = sqlite3.connect(name_of_db) # previously 'bs.db'
    c = conn.cursor()
    c.execute('create table if not exists {}(date_measure_taken text, bs_measure real)'.format(name_of_table))
    c.close()
    conn.close()
    
def sqlite_data_entry(new_data_row, name_of_db, name_of_table):
    conn = sqlite3.connect(name_of_db)
    c = conn.cursor()
    c.execute('insert into {} values{}'.format(name_of_table, new_data_row))
    conn.commit() # have to run this after changing the table
    c.close()  # closes the connection to the cursor
    conn.close()

def return_date():
    x = datetime.datetime.now()
    return x.strftime("%Y-%m-%d %H:%M:%S")


def reads_in_bs(bs):
    dtstmp = return_date()
    return "('{}',{})".format(dtstmp, bs)

