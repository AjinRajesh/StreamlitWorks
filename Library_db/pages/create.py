import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Create Record")

title=st.text_input("Book Title")
auth=st.text_input("Author Name")
price=st.number_input("Price",min_value=0)
lang=st.text_input("Language")
pg=st.number_input("Number of pages",min_value=0)

btn=st.button("Add Record")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    b.create(title, auth, price, lang, pg)
    st.success("Book inserted successfully")