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

UserBooks = []
getbook = input("Enter the name of the book you wish to take out? ")
UserBooks.append(getbook)
print(UserBooks)

res = cur.execute("""SELECT Count FROM Library WHERE Name=? """,(getbook,)) #allows me to fetch value based on a search term 

print(res.fetchall())

cur.execute("""update Library set Count=? where Name=?""", (3, getbook)) # can now update the table base by changing values
con.commit()




#make it so that you can now enter a book and it systems takes a book out of invtory
#next step is to make a sort of user invotry  and allow the user to do multiple transactiuons if they want too


#handle book loans, returns, and inventory.
# return- when you return the value goes back to orginal state
# invotry- name of book, , (is book taken out), 
# make a user invotry system



Loan = None # how many books loaned to you
Books = None # Name of books loaned to you/ How many you have



