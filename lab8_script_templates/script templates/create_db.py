"""
Description:
 Creates the people table in the Social Network database
 and populates it with 200 fake people.

Usage:
 python create_db.py
"""
import sqlite3
import os
import inspect
from faker import Faker
from random import randint, choice
from datetime import datetime

def main():
    global db_path
    
    db_path = os.path.join(get_script_dir(), 'social_network.db')
    
    create_people_table()
    populate_people_table()

def create_people_table():
    con=sqlite3.connect('social_network.db')
    
    cur=con.cursor()
    create_ppl_tbl_query = """
    CREATE TABLE IF NOT EXISTS people
    (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    province TEXT NOT NULL,
    bio TEXT,
    age INTEGER,
    created_at DATETIME NOT NULL,
    updated_at DATETIME NOT NULL
    );
    """
    cur.execute(create_ppl_tbl_query) 
    con.commit()
    con.close()
def create_fake_data():
    fake=Faker()
   # print()
    new_person=(fake.name(),fake.email(),fake.address(),fake.city(),fake.country(),fake.profile()['job'],randint(1, 100),datetime.now(),datetime.now())
    print(new_person)
    return new_person

def populate_people_table():
    """Populates the people table with 200 fake people"""
    con=sqlite3.connect('social_network.db')
    
    cur=con.cursor()
    

    add_person_query = """
    INSERT INTO people
    (
    name,
    email,
    address,
    city,
    province,
    bio,
    age,
    created_at,
    updated_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
    """
    for i in range(200):
        new_row=create_fake_data()
        cur.execute(add_person_query,new_row)
        #cu.commit()
    con.commit()
    con.close()

    #COMP

    # TODO: Create function body
    return

def get_script_dir():
    """Determines the path of the directory in which this script resides
    Returns:
        str: Full path of the directory in which this script resides
    """
    con = sqlite3.connect('social_network.db')
    
    script_path = os.path.abspath(inspect.getframeinfo(inspect.currentframe()).filename)
    return os.path.dirname(script_path)

if __name__ == '__main__':
   main()