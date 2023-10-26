import library as lib
import request


def libraryHome():
    print("**** WELCOME TO LIBRARY *****")
    # lib.getAllBooks()
    print("""CHOOSE WHAT YOU WANT TO DO:-\n1. Listing all books\n2. Borrow books\n3. Return books\n4. Donate books\n5. Track books\n6. exit the library\n""")
     
    while(True):
        try:
            user_response = int(input("Enter your choice: "))
            if user_response == 1: # listingbooks
                lib.displayAllBooks()
            elif user_response == 2: # borrow books
                lib.borrowbooks(input("Please Enter Your Name: "), request.requestBook())    
            elif user_response == 3: # return book
                lib.returnBook(request.returnBookUser())
            elif user_response == 4: # donate
                lib.donateBook(request.donateBookUser())    
            elif user_response == 5: # track
                for i in lib.track:
                    for key, value in i.items():
                        holder = key
                        book = value
                        print(f"{book} BOOK Is taken/Issued by {holder}.")
                print("\n")        
                if len(lib.track) == 0:
                    print("No Books Are Issued!. \n")
        
            elif user_response == 6:  # exit
                print("Thank you! \n")
                exit() 
            else:
                print("Invalid input! \n")

        except Exception as e: # catch errors
            print(f"{e} --> INVALID INPUT!, PLEASE ENTER VALID INPUT \n")       

libraryHome()
