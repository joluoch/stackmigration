'''
This script migrates data from the sql to postgres database
'''

import os
import sys
import mysql.connector
import psycopg2
# import MySQLdb
from mysql.connector import Error
from tqdm import tqdm as tq
from psycopg2 import OperationalError, errorcodes, errors
import os
import sys

def mysql_connect(dbname):
    try:
        conn_mysql = mysql.connector.connect(host='localhost',
                                            user='root',
                                            database=dbname)
        print("connected to the mysql database")
        mysql_cursor = conn_mysql.cursor(dictionary=True)

    except Error as e:

        print(e)

    return conn_mysql,mysql_cursor

#postgres connection
def post_connect(dbname):
    try:
        for i in tq(range(100), desc="Connecting to postgres"):
            pass
        post_connection = psycopg2.connect(database=dbname,
                                        user="postgres",
                                        password="qwerty")
        post_connection.autocommit = True
        print("Successfully connected to postgres database")
        post_cursor = post_connection.cursor()
    except OperationalError as e:
        print("Failed to connect to postgres db \n")
        print("Check credentials and retry")
        print("Safely exiting system")
        sys.exit(1)
    return post_connection,post_cursor

def migrate(dbname,select_statement,insert_statement):
    #connect to mysql and postgress
    conn_mysql,mysql_cursor = mysql_connect(dbname)
    post_connection,post_cursor = post_connect(dbname)

    #sql query
    print("querying summary table in sql")
    mysql_cursor.execute(select_statement)


    print("Migrating summary table to postgres database...")
    for i in tq(range(10), desc="Migrating to postgres"):
        for row in mysql_cursor:
            # print(row)
            try:

                post_cursor.execute(insert_statement, row)
                
            except Exception as e:
                print(e)

    print("Done..")
if __name__ == "__main__":
    mysql_connect('stations')
    post_connect('stations')
    migrate('stations',select_statement="SELECT * FROM flow",insert_statement= '''

                    INSERT INTO flow (date,flow1,flow2,flow3,flowtotal)
                    VALUES(%(date)s,%(flow1)s,%(flow2)s,%(flow3)s,%(flowtotal)s);
                    
                    
                ''')

 