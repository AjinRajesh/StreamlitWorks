import streamlit as st
from blood_db import DonorAddRetrieveUpdateDelete

st.title("Show Details of Donor")
btn=st.button("Click")
if btn:
    d=DonorAddRetrieveUpdateDelete()
    rec=d.readall()
    if rec:
        st.table(rec)
    else:
        st.error("No Records Found")