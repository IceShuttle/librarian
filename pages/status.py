import streamlit as st

branch = st.session_state["branch"]
br = branch.name
p_name = st.session_state["patron"].name
patron = st.session_state["patron"]

st.title(f"Welcome {p_name}")
st.write("Checked Out Books")
chbooks = []
for i,b in enumerate(patron.chbooks):
    date_str = b.date.strftime("%d/%m/%Y")
    # st.write(f"{i+1}.) {b.book.title} \t\t\t {date_str}")
    chbooks.append([b.book.title,date_str])
st.table(chbooks)

st.write("Dues")
dues = patron.get_dues()
st.write(str(len(dues)))
dues_table = []
total = 0
if dues:
    for k,v in dues.items():
        dues_table.append([k.book.title,v])
        total+=v
st.table(dues_table)
st.write(f"Total: {total}")

st.write("Reserved Books")
rev_books = patron.reserved
rev_table = []
for b in rev_books:
    rev_table.append((b.title))
st.table(rev_table)


