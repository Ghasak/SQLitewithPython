import sqlite3
import os
import time
import datetime
import random
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib import style
style.use('fivethirtyeight')

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



# Adding here the code of P2-

def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))

    keyword = 'Python'
    value = random.randrange(0,10)
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?,?,?,?)",
              (unix, date, keyword,value))
    conn.commit()


#create_table()


def Input_values():
    for i in range(10):
        dynamic_data_entry()
        time.sleep(1) # just to make our datestamp goes for a second to get a new entry, this just for the tutorial



#data_entry()
# c.close()
# conn.close(0)

# Adding here the code of P3-

def read_from_db():
    c.execute("SELECT keyword, unix, value, datestamp FROM stuffToPlot WHERE unix > 1559550811") #AND keyword= 'Python'
    #data = c.fetchall()
    #print(data)
    for row_no, row in enumerate(c.fetchall()):
        #print(row_no,row)
        print(row_no, row[0])


def graph_data():
    data = c.execute("SELECT unix, value FROM stuffToPlot")
    dates = []
    values = []
    for row in c.fetchall(): #Or you can use data
        #print(row[0]) # that should give us the UNIX column data
        #dates.append()
        #print(datetime.datetime.fromtimestamp(row[0])) #Same as before but better style format.
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates,values, '-')
    plt.show()




#create_table()
#read_from_db()
#Input_values()
graph_data()
c.close()
conn.close()
