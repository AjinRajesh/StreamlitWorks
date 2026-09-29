import streamlit as st
from blood_db import DonorAddRetrieveUpdateDelete

st.title("Retrieve details of a single Donor")
id=st.number_input("Enter id of Donor",min_value=0)
btn=st.button("Click")
if btn:
    d=DonorAddRetrieveUpdateDelete()
    rec=d.retrieve(id)
    if rec:
        st.write("Donor Name:",rec[1])
        st.write("Blood Group:",rec[2])
        st.write("Phone Number:",rec[3])
        st.write("City:",rec[4])
        st.write("Date of last Donation:",rec[5])
    else:
        st.error("No records Found")