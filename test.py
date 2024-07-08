#get sqlite extension
import sqlite3
con = sqlite3.connect("Library.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Library(Name,ReturnDays,Count,Genre)")

cur.execute("""
    INSERT INTO Library VALUES
        ('Year of the Maid', '20',1,'horror' ),
        ('Death of the Stuffed Corgi', '14' ,4,'romance'),
        ('Ice and the Tomb', '11',3,'horror' ),
        ('Queen of Nirvana', '19',0,'action' ),
        ('The Haunted Mask', '4',2,'action' ),
        ('Avian Shadow', '19',0,'action' ),
        ('The Attack of Jupiter', '4',2,'action' ),
        ('Thorns and the Princess', '4',2,'action' ),
        ('Tears of Fire', '4',2,'action' ),
        ('Strike the Shadow', '4',2,'action' ),
        ('Wicked Dance', '4',2,'action' )    
""") 
#global VAR
finalreuslt = 0
stockofbooks = 0
UserBooks = []
searching = []
MenuHistory = []
temphold = None
#global VAR

def strip(x):
    for nonnumber in x:
        if nonnumber == '(' or nonnumber == ')' or nonnumber == ',':
            P = x.replace(nonnumber,"")
            x = P
    global temphold
    temphold = x
    #temphold is the where the word goes after stripped 

def search(UserSearchTerm):
    cur.execute("SELECT name FROM Library")
    namesofbook = cur.fetchall()
    cur.execute("SELECT genre FROM Library")
    genreofbook = cur.fetchall()
    termof = input('Search: ')
    datainsert = "('"+termof+"',)"
    count = 0
    count2 = 0
    results = []
    
    if UserSearchTerm == 'name': # add in a key word search | we have acces to each name now
        for name in namesofbook:
            new = str(name)
            strip(new)
            search1 = temphold.lower()
            search2 = termof.lower()
            if search2 in search: # might have to use the .find() method to search, 
                results.append(temphold)
        print("results matching your search: " , results )

    elif UserSearchTerm == 'genre': 
        for x in genreofbook:
            poop = genreofbook[count2]
            pooptwo = str(poop) #repersents what genre we are on 
            if datainsert == pooptwo:
                results.append(namesofbook[count2])
                count2 += 1
            else:
                count2 += 1
    elif UserSearchTerm != 'genre' or UserSearchTerm != 'name':
        print('Not Valid')
    """ print('Results: ' , results) """ # i dont know where this goes for now
    

    
    
        



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
    cur.execute("SELECT Genre FROM Library")
    top = cur.fetchall()
    count=0
    for x in poi:
        print('Name:',poi[count],'|','Stock:',iop[count],'|','Genre:',top[count],'|','BorrowTime:',opi[count],'days','|')
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
        MenuHistory.append("database")
        display_table()
        linebreak()

    elif userchoice == 'checkout': 
        histrycount = 0 
        for x in MenuHistory:
            if x == "database":
                histrycount += 1
                if histrycount == 1:
                    getbook = input("Enter the name of the book you wish to take out ")
                    fetchvalue(getbook)
                    makenumber(stockofbooks)
                    if finalreuslt  <= 0:
                        print('Out of stock')
                    elif finalreuslt > 0:
                        updatestockcurrent = finalreuslt - 1 
                        updatestock(updatestockcurrent,getbook)
                        UserBooks.append(getbook) 
                        linebreak()
                        print('Book has succefully been checked out to your account')
                        linebreak()
                    break
        if histrycount == 0:
            print("Please view the database before you checkout a book")
            linebreak()
    elif userchoice == 'return':  
        MenuHistory.append("return")
        userbookscount = 0 
        for L in UserBooks:
            userbookscount += 1
        if userbookscount > 0:
            linebreak()
            print('Book account:')
            print(UserBooks)
            linebreak()
            ReturnBook = input('Name of book returning: ')
            fetchvalue(ReturnBook)
            makenumber(stockofbooks)
            newvalue = finalreuslt + 1 
            updatestock(newvalue,ReturnBook)
            print('Book has been returned to the Constantine Library')
            count = 0
            for x in UserBooks:
                if x == ReturnBook:
                    del UserBooks[count]
                    count += 1
                else:
                    count += 1
            linebreak()
        else:
            print('No books to return')
            linebreak()
    elif userchoice == 'viewbooks':
        MenuHistory.append("viewbooks")
        if not UserBooks:
            print("Account empty")
        else:
            print('Book account:')
            print(UserBooks)
    elif userchoice == 'search':
        MenuHistory.append("search")
        print('The search system is case sensitive')
        ask = input('Search by Name or Genre? ')
        ask2 = ask.lower()
        linebreak()
        if ask2 =='name' or ask2 == 'genre':
            search(ask2)
        else:
            print('Error')
        


            

       
   


print('Welcome to the Constantine Library.')
print('What would you like to do? View the database, checkout a book out or return a book? ')
user_choiceone = input('| database | checkout | return | ViewBooks | Search | Choose a option: ')
user_choicetwo = user_choiceone.lower()

DCR(user_choicetwo)
print('Would you like to return to the main menu')
userresponce = input('Answer here: ')
userresponceone = userresponce.lower()
if userresponceone == 'yes':
    while userresponceone == 'yes':
        user_choiceone = input('| database | checkout | return | ViewBooks | Search | Choose a option: ')
        user_choicetwo = user_choiceone.lower()
        linebreak()
        DCR(user_choicetwo)
        print('Would you like to return to the main menu')
        userresponce = input('Answer here: ')
        linebreak()
        userresponceone = userresponce.lower()
else:
    print('Exiting Constantine Library main system ')








