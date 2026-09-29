import streamlit as st
from blood_db import DonorAddRetrieveUpdateDelete

st.title("Add Donor Details")
name=st.text_input("Enter Donor Name")
bld_grp=st.text_input("Enter Blood Group")
phone=st.text_input("Enter Phone Number")
place=st.text_input("Enter city of Donor")
don_date=st.date_input("Enter Date of Last Donation")

btn=st.button("Add Donor")
if btn:
    d=DonorAddRetrieveUpdateDelete()
    val=d.add(name,bld_grp,phone,place,don_date)
    if val:
        st.success("Donor added successfully")
    else:
        st.error("Donor not added")
