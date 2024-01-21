import streamlit as st
import pickle as pk
import library

st.title("Register Patron")

branches = library.get_branches()
br = st.selectbox("Select Branch",branches)
name = st.text_input("Name")
passwd = st.text_input("Password",type="password")
root_pass = st.text_input("Admin Password",type="password")
branch = library.get_branch(br)
id = len(branch.patrons)
st.write(f"ID: [{id}]")


if st.button("Add Patron"):
    if root_pass == library.ROOT_PASS:
        patron = library.libpatron(id,name,passwd)
        branch.patrons.append(patron)

        st.session_state["branch"] = branch
        with open(f"./data/{br}",'wb') as f:
            pk.dump(branch,f)
        st.success("Patron added")
    else:
        st.error("Cannot add book")




