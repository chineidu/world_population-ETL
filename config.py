import os
import mysql.connector as sql

# configuration
config = {
    'host': 'localhost',
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PSWD')
}
# create connection using configuration
conn = sql.connect(**config)
# create cursor object
cursor = conn.cursor()


def create_db(DB_NAME, sql_query):
    """Create a MySQL DB"""
    cursor.execute(sql_query)
    print(f"{DB_NAME} was created")    

def create_table(table_name, sql_query):
    """Add a table to the DB"""
    # select DB
    cursor.execute(""" USE World_population """)
    # execute the query
    cursor.execute(sql_query)
    print(f"{table_name} was created")    

def show_tables():
    # check for the tables
    cursor.execute('SHOW TABLES')
    # display tables
    for table in cursor:
        print(table)
             
def insert_into_table(table_name, sql_query, values):
    """Insert values into a table"""
    # add all the rows to the db
    cursor.executemany(sql_query, values)
    # commit the changes
    conn.commit()
    print(f"Values inserted into {table_name}")
     
def select_records(sql_query):
    """Select records from a table"""
    cursor.execute(sql_query)
    # display records
    for x in cursor:
        print(f"{x} \n")
