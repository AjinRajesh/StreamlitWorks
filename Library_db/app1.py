import streamlit as st
from library_db import BookListCreateRetrieveUpdateDelete

st.title("Welcome to Library App")

b=BookListCreateRetrieveUpdateDelete()

tab1,tab2,tab3,tab4,tab5=st.tabs(['ADD','READ','RETRIEVE','UPDATE','DELETE'])

with tab1:
    st.header("ADD")

    title = st.text_input("Book Title")
    auth = st.text_input("Author Name")
    price = st.number_input("Price", min_value=0)
    lang = st.text_input("Language")
    pg = st.number_input("Number of pages", min_value=0)

    btn = st.button("Add Record")
    if btn:
        b.create(title, auth, price, lang, pg)
        st.success("Book inserted successfully")

with tab2:
    st.header("LIST")
    btn = st.button("Click to view all books in library")
    if btn:
        rec = b.list()
        if rec:
            # for row in rec:
            st.table(rec)
        else:
            st.info("No records found")

with tab3:
    st.header("Retrieve Single Record")

    id = st.number_input("Enter the id", min_value=0)
    btn = st.button("Retrieve Details")
    if btn:
        rec = b.retrieve(id)
        if rec:
            st.write("Title:", rec[1])
            st.write("Author:", rec[2])
            st.write("Price:", rec[3])
            st.write("Language:", rec[4])
            st.write("Pages:", rec[5])
        else:
            st.error("No records found")

with tab4:
    st.header("Update Record")

    id = st.number_input("Enter id of book to update details", min_value=0)
    title = st.text_input("New book Title")
    auth = st.text_input("New Author Name")
    price = st.number_input("New Price", min_value=0)
    lang = st.text_input("Updated Language")
    pg = st.number_input("Number of pages in the updated book", min_value=0)

    btn = st.button("Update")
    if btn:
        row_count = b.update(title, auth, price, lang, pg, id)
        if row_count > 0:
            st.success("Data Updated successfully")
        else:
            st.error("No record found")

with tab5:
    st.header("Delete Record")

    id = st.number_input("Enter the id of row to delete row", min_value=0)
    btn = st.button("Delete")
    if btn:
        row_count = b.delete(id)
        if row_count > 0:
            st.success("Data deleted successfully")
        else:
            st.error("Record not found")


