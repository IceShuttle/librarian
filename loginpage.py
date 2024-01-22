import streamlit as st
import pickle as pk
from library import get_branches

st.title("Login")
branch_name = st.selectbox("Select Branch",get_branches())
with open(f"./data/{branch_name}",'rb') as f:
    st.session_state["branch"]=pk.load(f)

ID = st.text_input("ID")
password = st.text_input("Password", type="password")

if st.button("Login"):
    id = int(ID)
    if len(st.session_state["branch"].patrons)>id:
        if st.session_state["branch"].patrons[id].passwd == password:
            st.session_state["patron"] = st.session_state["branch"].patrons[id]
            st.success("Welcome "+st.session_state["patron"].name)
        else:
            st.error("Login failed")

if __name__ == "__main__":
    pass

