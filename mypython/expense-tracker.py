import sqlite3 as sql
import datetime as dt
from tabulate import tabulate

con = sql.connect("exp.db");    #connected to a database

cursor = con.cursor();

tab=  '''CREATE TABLE IF NOT EXISTS tracker(
            


            Spent_on TEXT       NOT null,
            Amount   INTEGER    NOT null,
            Comments TEXT       NOT null
            );'''

cursor.execute(tab)

cur_e = cursor.execute('SELECT * FROM tracker')
columns= cur_e.description

columns = cur_e.description
col = []
i=0
for row in columns:
    col.append(row[0])
    i=i+1


noc = len(col);         #number of columns in the table



col_set= set(col)

if not ("Date") in col_set:

    
    addColumn = "ALTER TABLE tracker ADD COLUMN Date INTEGER "
    cursor.execute(addColumn)


                   #commit changes to the database


ins = ''' INSERT INTO tracker(Spent_on, Amount, Comments, Date)
                      VALUES(?, ?, ?, ?);'''





category = input("Where you spent the amount? ") 
amt = input ("How much did you spent? ")
cmt = input ("Give some short description ")
when= dt.date.today()

data= [category, amt, cmt, when]

cursor.execute(ins, data)

con.commit();



#FETCHING contents from the table and printing it

sel=cursor.execute("SELECT * FROM tracker")

rows = sel.fetchall()
print (tabulate(rows, headers= col))


con.close;                      #closing the database

