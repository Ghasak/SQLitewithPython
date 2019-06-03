# SQLite3 with Python 3.7
# - Quick References and Formula to increase productivity

Everything you need to know about SQLite is located here.
We will start with the following syllabus. SQLite is a lighter version of SQL, we can create a database without a server.

# P1- Creating a Database, table and inserting:

We always define the connection and cursor,

```
import sqlite3
import os


ResourceDir = os.getcwd()
# print (ResourceDir)

# Connect a database if its existed:
conn = sqlite3.connect(ResourceDir+'/resources/'+'tutorial.db')
c = conn.cursor()


# Define a new table in the database

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS stuffToPlot (unix, REAL, Datestamp TEXT, keyword TEXT, value REAL)')


# Define inputing data to your Table in your current open database

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES(145123232, 4.454,'2016-01-02', 'python', 5 )")
    conn.commit()
    c.close()
    conn.close()



create_table()
data_entry()
```
* Every time you modify your table you need to commit (**Save**) your table once you modify it.

![](./Output_images/P1-1.png)


# P2- Inserting variables to database table (IMPORT)
There are few things that you will need to input your variables in **Hard way** as you saw previously. and here how to make things are more easy for importing data.

```


# Adding here the code of P2-

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?,?,?,?)",
              (unix, date, keyword,value))
    conn.commit()

create_table()
#data_entry()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1) # just to make our datestamp goes for a second to get a new entry, this just for the tutorial


c.close()
conn.close()
```
![](./Output_images/P2-1.png)

## NOTE-1
you can change the order of the table in your SQL, you can level a value empty for a certain cell in your table, but you cant offer input values less than the column-numbers.
## NOTE-2
You have to be careful to add **conn.colse()** and **c.colse()** only when you are not running input values several times in a loop or something that ended up in open and close the connection everytime you are working on your data. Therefore, we will try to make this only once to pen and close the connection once, **ONE** when you open the database and inserting your patch, **SECOND** then close your connection after you finish working with the current database. Also keep in mind, **conn.commit** is to commit (execute) your statement that you wrote in SQL.


# P3-
