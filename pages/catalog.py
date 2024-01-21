import streamlit as st
import pandas as pd
branch = st.session_state["branch"]

titles = []
authors = []
pubs = []
avail = []
total = []

for b in branch.books:
    titles.append(b.title)
    authors.append(b.author)
    pubs.append(b.pub)
    avail.append(b.avail)
    total.append(b.total)

st.title("Catalog")
df = pd.DataFrame({
    "Title":titles,
    "Authors":authors,
    "Publisher":pubs,
    "Available":avail,
    "Total":total
})
df.index+=1
st.dataframe(df)



