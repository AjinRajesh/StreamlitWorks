import streamlit as  st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Show Records")

btn = st.button("Click to view all books in library")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    rec=b.list()
    if rec:
        # for row in rec:
        st.table(rec)
    else:
        st.info("No records found")
