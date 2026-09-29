import streamlit as  st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Update Record")

id=st.number_input("Enter id of book to update details",min_value=0)
title=st.text_input("New book Title")
auth=st.text_input("New Author Name")
price=st.number_input("New Price",min_value=0)
lang=st.text_input("Updated Language")
pg=st.number_input("Number of pages in the updated book",min_value=0)

btn=st.button("Update")
if btn:
    b=BookListCreateRetrieveUpdateDelete()
    row_count=b.update(title,auth,price,lang,pg,id)
    if row_count>0:
        st.success("Data Updated successfully")
    else:
        st.error("No record found")

