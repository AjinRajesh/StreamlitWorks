import streamlit as st
from blood_db import DonorAddRetrieveUpdateDelete

st.title("Delete Donor Details")
id=st.number_input("Enter id of Donor to Delete:",min_value=0)
btn=st.button("Delete Donor")
if btn:
    d=DonorAddRetrieveUpdateDelete()
    val=d.delete(id)
    if val:
        st.success("Donor deleted successfully")
    else:
        st.error("Donor not Found")
