import sqlite3


DB_PATH='./DeepCareX.db'
## Create user table
def user_table():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS USER(NAME VARCHAR,EMAIL VARCHAR,PASSWORD VARCHAR)")
    conn.commit()
    conn.close()

## Create contact table
def contact_table():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS CONTACT(NAME VARCHAR,EMAIL VARCHAR,CONTACT VARCHAR(13), MESSAGE VARCHAR)")
    conn.commit()
    conn.close()

## Create newsletter table
def newsletter():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS NEWSLETTER(EMAIL VARCHAR)")
    conn.commit()
    conn.close()

## Create patients table
def patients():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("CREATE TABLE  IF NOT EXISTS PATIENTS(NAME VARCHAR,EMAIL VARCHAR, ID VARCHAR, CONTACT NUMBER, COUNTRY VARCHAR, STATE VARCHAR, PINCODE NUMBER, GENDER VARCHAR, AGE NUMBER, DISEASE VARCHAR, RESULT VARCHAR)")
    conn.commit()
    conn.close()



user_table()
contact_table()
newsletter()
patients()
