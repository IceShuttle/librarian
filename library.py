from datetime import date
import pickle as pk
import streamlit as st
import os

RETURN_PERIOD = -1
FINE_RATE = 10
ROOT_PASS = 'root'

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
        book.book.checkout()
    def retbook(self,book):
        self.chbooks.remove(book)
        book.book.checkin()
    def revbook(self,book):
        self.reserved.append(book)
    def get_dues(self):
        dues = {}
        for cb in self.chbooks:
            bt = date.today()-cb.date
            bt = bt.days
            if bt>RETURN_PERIOD:
                dues[cb]=(bt - RETURN_PERIOD) * FINE_RATE
        return dues

class libtrans():
    def __init__(self,id,book,date):
        self.id = id
        self.book =book
        self.date =date

class libbranch():
    def __init__(self,name,books=[],patrons=[],chbooks=[],reserved=[]):
        self.name = name
        self.books = books
        self.patrons = patrons
        self.chbooks = chbooks
        self.reserved = reserved

    def get_patron(self,name):
        for p in self.patrons:
            if p.name == name:
                return p

    def get_book(self,title):
        for b in self.books:
            if b.title ==title:
                return b

    def get_b_names(self):
        names = []
        for b in self.books:
            names.append(b.title)
        return names

    def get_avb_names(self):
        names = []
        for b in self.books:
            if b.avail:
                names.append(b.title)
        return names


def get_branches():
    folder_path = "./data/"
    if not os.path.exists(folder_path):
        return "Folder path does not exist."

    file_names = os.listdir(folder_path)

    return file_names

def get_branch(name):
    with open(f"./data/{name}",'rb') as f:
        return pk.load(f)


def main():
    pass
if __name__ == "__main__":
    main()
