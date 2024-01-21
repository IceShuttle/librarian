import streamlit as st
import pickle as pk
import library

st.title("Add Books")

branches = library.get_branches()
br = st.selectbox("Select Branch",branches)
title = st.text_input("Title")
auth = st.text_input("Author")
pub = st.text_input("Publisher")
total = st.number_input("Total")
passwd = st.text_input("Admin Password",type="password")

if st.button("Add Book"):
    if passwd == library.ROOT_PASS:
        book = library.Book(title,auth,pub,total,total)
        branch = library.get_branch(br)
        branch.books.append(book)
        st.session_state["branch"] = branch
        with open(f"./data/{br}",'wb') as f:
            pk.dump(branch,f)
        st.success("Book added")
    else:
        st.error("Cannot add book")





