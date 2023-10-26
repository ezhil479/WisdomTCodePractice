track = []
books = []

def getAllBooks(a=1):
    book_reg_file_obj = open("bookregister.txt", "r")
    file_books = book_reg_file_obj.readlines()
    for book in file_books:
        if(int(book.split("|")[1]) !=0):
            bookname = book.split("|")[0]
            books.append(bookname)
            print('\n')    

def displayAllBooks():
    books.clear()
    getAllBooks(2)
    print(f"The books available are: {len(books)}")
    i = 1
    strToPrint = ""
    for book in books:
        strToPrint += """ {}. {}  \n""".format(i, book)
        i += 1
    print(strToPrint) 
    print("\n")   

def borrowbooks(studentName, bookIndex):
    bookname = getBookNameBasedOnIndex(bookIndex)
    print(books)
    if bookname not in books:
        print(f"{bookname} Book is not available at the moment The book is taken by someone else. \n")
    else:
        track.append({studentName: bookname})    
        print(track)
        trackdetails = studentName + ":" +bookname + "\n"
        addTrack(trackdetails)
        print("Book Issued: THANK YOU \n")
        books.remove(bookname)
        removeBooks(bookname)

def isBookNameExistsInLibrary(bookname):
    flag = False
    book_reg_file_obj = open("bookregister.txt","r")
    data = book_reg_file_obj.readlines()
    if(len(data) > 0):
        for user in data:
            bookdetails = user.split("|")
            if(bookdetails[0] == bookname):
                flag = True
                break
    return flag  

def getBookNameBasedOnIndex(index):
    if(index <= len(books)):
        return books[index - 1]
    else:
        print("Index is not present")

def removeBooks(bookname):
    with open("bookregister.txt", "r") as f:
        lines = f.readlines()
    with open("bookregister.txt", "w") as f:
        for line in lines:
            if line.split("|")[0] == bookname:
                bookdetail = line.split("|")[0] + '|' + '0\n'
                f.write(bookdetail)
            else:
                f.write(line) 
def returnBookUpdateReg(bookname):
    with open("bookregister.txt", "r") as f:
        lines = f.readlines()
    with open("bookregister.txt", "w") as f:
        for line in lines:
            if line.split("|")[0] == bookname:
                bookdetail = line.split("|")[0] + '|' + '1 \n'    
                f.write(bookdetail)
            else:
                f.write(line)    

def addBooks(bookname):
    file_object = open("bookregister.txt", 'a')
    bookname = bookname + '|' + '1 \n'
    file_object.write(bookname)
    file_object.close()
def addTrack(trackdetails):
    file_object = open("track.txt", 'a')
    trackdetails = trackdetails + '\n'
    file_object.write(trackdetails)
    file_object.close()

def returnBook(bookname):
    print("BOOK RETURNED : THANK YOU! \n")
    books.append(bookname)
    returnBookUpdateReg(bookname)

def donateBook(bookname):
    print("BOOK DONATED : THANK YOU VERY MUCH, HAVE A GREAT DAY AHEAD. \n")
    books.append(bookname)
    addBooks(bookname)




