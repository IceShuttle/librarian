import streamlit as st
import pickle as pk

branch = st.session_state["branch"]
br = branch.name
p_name = st.session_state["patron"].name
patron = branch.get_patron(p_name)

st.write(f"Welcome {p_name}")

bk = st.selectbox("Book Title",branch.get_b_names())

if st.button("Reserve"):
    book = branch.get_book(bk)
    patron.revbook(book)

    st.session_state["branch"] = branch
    with open(f"./data/{br}",'wb') as f:
        pk.dump(branch,f)
    st.success("Reserved")



