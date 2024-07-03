#get sqlite extension
import sqlite3
con = sqlite3.connect("Library.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Library(Name,ReturnDays,Count,Genre)")

cur.execute("""
    INSERT INTO Library VALUES
        ('Book1', '20',1,'horror' ),
        ('Book2', '14' ,4,'romance'),
        ('Book3', '11',3,'horror' ),
        ('Book4', '19',0,'action' ),
        ('Book5', '4',2,'action' )    
""")
#global VAR
finalreuslt = 0
stockofbooks = 0
UserBooks = []
searching = []
test = []
#global VAR


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
    
    if UserSearchTerm == 'name': # add in a check so that searchs are all automitcally lower case so no need for case senstivity
        for x in namesofbook:
            ready = namesofbook[count]
            readytwo = str(ready)
            if datainsert == readytwo:
                results.append(readytwo)
                count += 1
            else:
                count += 1
    elif UserSearchTerm == 'genre': # add in a check so that searchs are all automitcally lower case so no need for case senstivity
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
    print('Results: ' , results)
    

    
    
        



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
        print('Name:',poi[count],'Stock:',iop[count],'Genre:',top[count],'BorrowTime:',opi[count],'days')
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


    elif userchoice == 'return':  
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
        print('Book account:')
        print(UserBooks)
    elif userchoice == 'search':
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
user_choiceone = input('Choose a option: | database | checkout | return | ViewBooks | Search | ') # add a exit feature
user_choicetwo = user_choiceone.lower()

DCR(user_choicetwo)
print('Would you like to return to the main menu')
userresponce = input('Answer here: ')
userresponceone = userresponce.lower()
if userresponceone == 'yes':
    while userresponceone == 'yes':
        user_choiceone = input('Choose a option: | database | checkout | return | ViewBooks | Search | ')
        user_choicetwo = user_choiceone.lower()
        linebreak()
        DCR(user_choicetwo)
        print('Would you like to return to the main menu')
        userresponce = input('Answer here: ')
        linebreak()
        userresponceone = userresponce.lower()
else:
    print('Exiting Constantine Library main system ')

        
    




# make a search funtion where user can looks for books by name or genere



""" con.commit()
 dont really need to use other wise it breaks but you cant see the DB table now on the DB file """







