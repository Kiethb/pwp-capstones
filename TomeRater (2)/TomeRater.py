class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("Email address updated")

    def __repr__(self):
        return "User: {}  Email: {}  #Books read: {}".format(self.name,self.email,len(self.books))

    def __eq__(self, other_user):
        if (self.name == other_user.name and self.email == other_user.email):
            return ("They are equal!")
        else:
            return ("They are different!")

    def read_book(self, book, rating=None): #tested
        self.books[book]=rating

    def get_average_rating(self):  #tested
        sum = 0
        qty = 0
        for book in self.books.values():
            if(book != None):
                qty+=1
                sum += book
        try:
            average = sum/qty
        except ZeroDivisionError:
          return 0.0
        else:
            return average

class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def __hash__(self):
        return hash((self.title,self.isbn))

    def __repr__(self):
        return "Title: {}  ISBN: {}  Ratings: {}".format(self.title,self.isbn,self.ratings)

    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self,new_isbn):
        self.isbn = new_isbn
        print("ISBN has been updated")

    def add_rating(self,rating):
        if (rating >=0 and rating < 5):
            self.ratings.append(rating)
        else:
            print("Invalid value")
            
    def get_average_rating(self):  #tested
        sum = 0
        count = 0
        for rating in self.ratings:
            sum += rating
            count += 1
        try:
            average = sum/count
        except ZeroDivisionError:
          return 0.0
        else:
            return sum/count
            
    def __eq__(self,other_book):
        if(self.title == other_book.title and self.isbn == other_book.isbn):
            return ("They are equal!")
        else:
            return ("They are different!")

class Fiction(Book):

    def __init__(self,title,author,isbn):
        super().__init__(title,isbn)
        self.author = author

    def __repr__(self):
        return ("{} by {}".format(self.title,self.author))

    def get_author(self):
        return self.author

class Non_Fiction(Book):

    def __init__(self, title, subject, level,isbn):
        super().__init__(title,isbn)
        self.subject = subject
        self.level = level
                
    def __repr__(self):
        return ("{}, a {} manual on {}".format(self.title,self.level, self.subject))

    def get_author(self):
        return self.author

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level
    
class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def __repr__(self): # this needs to print user, books, user, books, user books....
        print(self.users)
        print(self.books)

    def __eq__(self, other_TR):
        if (self.users == other_TR.users and self.books == other_TR.books):
            return ("They are equal!")
        else:
            return ("They are different!")

    def create_book(self, title, isbn):
        new_book = Book(title,isbn)
        return new_book

    def create_novel(self,title,author,isbn):
        fb = Fiction(title,author,isbn)
        return fb

    def create_non_fiction(self,title,subject,level,isbn):
        nfb = Non_Fiction(title,subject,level,isbn)
        return nfb

    def add_book_to_user(self,book,email, rating= None):      
        try:
            user = self.users[email]
        except KeyError:
            print("No user with email {}".format(email))
        else:
            user.read_book(book,rating)
            if(rating!=None):
                book.add_rating(rating)
            if(book not in self.books):
                self.books[book] = 1
            else:
                self.books[book]+=1
                
    def add_user(self,name,email,user_books=None):
        new_user= User(name, email)
        #print(new_user)
        self.users[email] = new_user #name
        #print(self.users)
        if user_books is not None:
            for book in user_books:
                self.add_book_to_user(book,email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
            largest_key = ""
            largest_value = float("-inf")
            for key,value in self.books.items():
                if value > largest_value:
                    largest_value = value
                    largest_key = key
            return("{} is the most read book at {} times".format(largest_key,largest_value))
                
    def highest_rated_book(self):
            highest_rated_book = ""
            largest_value = float("-inf")
            for key in self.books.keys():
                book_rating = key.get_average_rating()
                if book_rating > largest_value:
                    largest_value = book_rating
                    highest_rated_book = key
            return("The highest rated book is {} at {}".format(highest_rated_book,largest_value))

    def most_positive_user(self):
        most_positive_user = ""
        largest_value = float("-inf")
        for user in self.users.values():
            print(user)
            user_rating = user.get_average_rating()
            if user_rating > largest_value:
                largest_value = user_rating
                most_positive_user = user
        return("The most positive user is {}".format(most_positive_user))

