import streamlit as st
import pickle as pk
import os

def list_files_in_folder(folder_path):
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        return "Folder path does not exist."

    # Get a list of file names in the folder
    file_names = os.listdir(folder_path)

    # Print or return the list of file names
    return file_names

branch_name = st.selectbox("Select Branch",list_files_in_folder("./data"))
with open(f"./data/{branch_name}",'rb') as f:
    st.session_state["branch"]=pk.load(f)

# Create input fields for username and password
id = st.text_input("ID")
id = int(id)
password = st.text_input("Password", type="password")

# Check if the login button is clicked
if st.button("Login"):
    if len(st.session_state["branch"].patrons)>id:
        if st.session_state["branch"].patrons[id].passwd == password:
            st.success("Login Success")
            st.session_state["patron"] = st.session_state["branch"].patrons[id]
        else:
            st.error("Login failed")

if __name__ == "__main__":
    pass

