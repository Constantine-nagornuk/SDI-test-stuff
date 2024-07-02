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
        ('Book4', '19',0 ),
        ('Book5', '4',2 )    
""")
#global VAR
finalreuslt = 0
stockofbooks = 0
UserBooks = ['Book4']
test = []
#global VAR


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

def linebreak():
    print('----------------------------------------')


def DCR(userchoice,):
    if userchoice == 'database':
    
        display_table()
        linebreak()
    elif userchoice == 'checkout': 
        linebreak()
        getbook = input("Enter the name of the book you wish to take out")
        UserBooks.append(getbook) 
        fetchvalue(getbook)
        makenumber(stockofbooks)
        if finalreuslt  <= 0:
            print('Out of stock')
        else:
            updatestockcurrent = finalreuslt - 1 
            updatestock(updatestockcurrent,getbook)


    elif userchoice == 'return': #  add in so that when you return the book it clear from userbooks list
        linebreak()
        print('Book account:')
        print(UserBooks)
        ReturnBook = input('Name of book returning:')
        fetchvalue(ReturnBook)
        makenumber(stockofbooks)
        newvalue = finalreuslt + 1 
        updatestock(newvalue,ReturnBook)
        print('Book has been returned to the Constantine Library')
        count = 0
        for x in UserBooks:
            if x == ReturnBook:
                UserBooks.pop(UserBooks[count]) # something in here brooke or mayde DCR function idk, constantine will fiz this tomorrow - constantine
            else:
                None
        linebreak()
   


print('Welcome to the Constantine Library.')
print('What would you like to do? View the database, checkout a book out or return a book? ')
user_choiceone = input('Choose a option: database,checkout or return ')
user_choicetwo = user_choiceone.lower()

DCR(user_choicetwo)
print('Would you like to return to the main menu')
userresponce = input('Answer here: ')
linebreak()
userresponceone = userresponce.lower()

if userresponceone == 'yes':
    while userresponceone == 'yes':
        user_choiceone = input('Choose a option: database,checkout or return ')
        user_choicetwo = user_choiceone.lower()
        linebreak()
        DCR(user_choicetwo)
        print('Would you like to return to the main menu')
        userresponce = input('Answer here: ')
        linebreak()
        userresponceone = userresponce.lower()
else:
    print('Exiting Constantine Library main system ')

        
    



    
    



""" 
fetchvalue(getbook)
makenumber(stockofbooks)
print(finalreuslt)
updatestock(10,getbook)
display_table()
 """






""" con.commit()
 dont really need to use other wise it breaks but you cant see the DB table now on the DB file """




#next step is to make a sort of user invotry  and allow the user to do multiple transactiuons if they want too
#handle book loans, returns, and inventory.
# return- when you return the value goes back to orginal state
# invotry- name of book, , (is book taken out), 
# make a user invotry system



Loan = None # how many books loaned to you
Books = None # Name of books loaned to you/ How many you have



