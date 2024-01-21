import streamlit as st

st.title("Check In")
cbs = st.session_state["patron"].chbooks
cb_names = []
for cb in cbs:
    cb_names.append(cb.book.title)

book_name = st.selectbox("Book Name",cb_names)

if st.button("CheckIn"):
    for cb in cbs:
        if cb.book.title == book_name:
            st.session_state["patron"].retbook(cb)
            st.success("Checked in successfully")
    pass

