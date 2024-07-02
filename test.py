#get sqlite extension
import sqlite3
con = sqlite3.connect("Library.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Library(Name,ReturnDays,Count )")

cur.execute("""
    INSERT INTO Library VALUES
        ('Book1', '20',1 ),
        ('Book2', '14' ,4),
        ('Book3', '11',3 ),
        ('Book4', '4',2 )    
""")
#global VAR
finalreuslt = 0
stockofbooks = 0
UserBooks = []
test = []
#global VAR



getbook = input("Enter the name of the book you wish to take out? ")
UserBooks.append(getbook)
""" Make a user interface so you can interact with the system more cleanly. will require lots of conditionals and reroutes """

def fetchvalue(nameofbook,):
    res = cur.execute("""SELECT Count FROM Library WHERE Name=? """,(nameofbook,)) #allows me to fetch value based on a search term 
    this = res.fetchall()
    global stockofbooks
    stockofbooks = str(this)

def display_table():
    cur.execute("SELECT name FROM Library")
    poi = cur.fetchall()
    cur.execute("SELECT count FROM Library")
    iop = cur.fetchall()
    cur.execute("SELECT ReturnDays FROM Library")
    opi = cur.fetchall()
    count=0
    for x in poi:
        print('Name:',poi[count],'Stock:',iop[count],'BorrowTime:',opi[count],'days')
        count +=1

def makenumber(x):
    for nonnumber in x:
        if nonnumber == '[' or nonnumber == ']' or nonnumber == '(' or nonnumber == ')' or nonnumber == ',':
            P = x.replace(nonnumber,"")
            x = P
    global finalreuslt
    y = int(x)
    finalreuslt = y
    #finalreuslt is the where the actual number goes not into the value we plugged in 
    
def updatestock(currentcount,nameofbook):
    cur.execute("""update Library set Count=? where Name=?""", (currentcount, nameofbook)) # can now update the table base by changing values





fetchvalue(getbook)
makenumber(stockofbooks)
print(finalreuslt)
updatestock(10,getbook)
display_table()







""" con.commit()
 dont really need to use other wise it breaks but you cant see the DB table now on the DB file """




#next step is to make a sort of user invotry  and allow the user to do multiple transactiuons if they want too
#handle book loans, returns, and inventory.
# return- when you return the value goes back to orginal state
# invotry- name of book, , (is book taken out), 
# make a user invotry system



Loan = None # how many books loaned to you
Books = None # Name of books loaned to you/ How many you have



