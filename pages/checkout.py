import streamlit as st
from datetime import date
import library
import pickle as pk

branch = st.session_state["branch"]
br = branch.name
p_name = st.session_state["patron"].name
patron = branch.get_patron(p_name)

st.write(f"Welcome {p_name}")

bk = st.selectbox("Book Title",branch.get_avb_names())

if st.button("Checkout"):
    book = branch.get_book(bk)
    chbook = library.Chbook(book,date.today())
    patron.checkout(chbook)

    st.session_state["branch"] = branch
    with open(f"./data/{br}",'wb') as f:
        pk.dump(branch,f)
    st.success("Checked Out")



