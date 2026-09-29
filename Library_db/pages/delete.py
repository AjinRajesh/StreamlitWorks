import streamlit as  st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Delete Record")

id=st.number_input("Enter the id of row to delete row",min_value=0)
btn=st.button("Delete")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    row_count=b.delete(id)
    if row_count>0:
        st.success("Data deleted successfully")
    else:
        st.error("Record not found")