

# Importing module
import sqlite3


# Creating connection
conn = sqlite3.connect('test2.db')


# While connection is open, do the following:
with conn:
    cur = conn.cursor()
    # Here I create a table with two columns
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_example( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_data TEXT)")
    conn.commit() # Makes the changes
conn.close() # Closes the connection


# Creating list
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')


# Connecting
conn = sqlite3.connect('test2.db')


# Iterates through list and finds files that have the .txt file extension, and inserts their name into the database
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_example (col_data) VALUES (?)", (x,))
            print(x)
conn.close() # Closes the connection
