import streamlit as st
import library
import pickle as pk

st.title("Register Branch")
name = st.text_input("Branch Name")
passwd = st.text_input("Admin password",type="password")

if st.button("Create"):
    if passwd==library.ROOT_PASS:
        branch = library.libbranch(name)
        st.session_state["branch"] = branch
        with open(f"./data/{name}",'wb') as f:
            pk.dump(branch,f)
        st.success("Branch Created")
    else:
        st.error("Cannot create branch")


