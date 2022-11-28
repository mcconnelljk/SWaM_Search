#!pip3 install psycopg2-binary
#!pip3 install python-dotenv

import os
import psycopg2
from dotenv import load_dotenv
  
load_dotenv()

def get_connection():
    try:
        return psycopg2.connect(
            database=os.environ['database'],
            user=os.environ['user'],
            password=os.environ['password'],
            host=os.environ['host'],
            port=int(os.environ['port']),
        )
    except:
        return False

#conn = get_connection()

def test_connection(conn):
    if conn and conn.closed == 0:
        print(" Connection to SWaM_DB established successfully.\n\n")
    elif conn and conn.closed == 1:
        print(" Connection to SWaM_DB closed successfully.\n\n")
    else:
        print(" Connection to SWaM_DB encountered an error...\n Please check your local configuration file for your environmental variables\n\n")
    return

#test_connection(conn)

def close(conn):
    conn.close()
    test_connection(conn)
    return

#conn.close()