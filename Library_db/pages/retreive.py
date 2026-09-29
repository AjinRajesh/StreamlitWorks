import streamlit as  st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Retrieve Single Record")

id=st.number_input("Enter the id",min_value=0)
btn=st.button("Retrieve Details")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    rec=b.retrieve(id)
    if rec:
        st.write("Title:",rec[1])
        st.write("Author:", rec[2])
        st.write("Price:", rec[3])
        st.write("Language:", rec[4])
        st.write("Pages:", rec[5])
    else:
        st.error("No records found")
