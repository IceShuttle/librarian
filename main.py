from datetime import date
import pickle as pk

RETURN_PERIOD = 7
FINE_RATE = 10

class Book():
    def __init__(self,title,author,pub,avail,total) -> None:
        self.title = title
        self.author = author
        self.pub = pub
        self.avail = avail
        self.total = total
    def checkout(self):
        self.avail-=1
    def checkin(self):
        self.avail+=1

class Chbook():
    def __init__(self,book,date):
        self.book = book
        self.date = date

class libpatron():
    def __init__(self,id,name,passwd,chbooks=[],reserved=[]):
        self.id = id
        self.name =name
        self.passwd = passwd
        self.chbooks =chbooks
        self.reserved = reserved
    def checkout(self,book):
        self.chbooks.append(book)
        book.checkout()
    def retbook(self,book):
        self.chbooks.remove(book)
        book.checkin()
    def get_dues(self):
        dues = {}
        for b in self.chbooks:
            bt = date.today()-b.date
            if bt>RETURN_PERIOD:
                dues[b]=(bt - RETURN_PERIOD) * FINE_RATE

class libtrans():
    def __init__(self,id,book,date):
        self.id = id
        self.book =book
        self.date =date

class libbranch():
    def __init__(self,name,books,patrons,chbooks,reserved=[]):
        self.name = name
        self.books = books
        self.patrons = patrons
        self.chbooks = chbooks
        self.reserved = reserved
        return False

def main():
    pass
if __name__ == "__main__":
    main()
