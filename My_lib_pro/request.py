from library import track, books

"""REQUEST SECTION"""
def requestBook():
    print("You are requested to borrow a book! ")
    msg = f"Enter book index between 1 and {len(books)}: "
    bookindex = int(input(msg))
    return bookindex

def returnBookUser():
    print("You are requested to return a book! ")
    name = input("Please Enter your name: ")
    book = input("ENTER A BOOK NAME FOR RETURN: ")
    if {name: book} in track:
        track.remove({name: book})
    return book    

def donateBookUser():
    print("Okay ! Youu want to donate book! ")
    book = input("Enter book name for donate: ")
    return book

