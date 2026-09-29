import streamlit as st
from blood_db import DonorAddRetrieveUpdateDelete

st.title("Update Donor Details")
id=st.number_input("Enter id of Donor to update:",min_value=0)
name=st.text_input("Enter updated Donor Name")
bld_grp=st.text_input("Enter updated Blood Group")
phone=st.text_input("Enter updated Phone Number")
place=st.text_input("Enter updated city of Donor")
don_date=st.date_input("Enter updated Date of Last Donation")

btn=st.button("Update Details")
if btn:
    d=DonorAddRetrieveUpdateDelete()
    val=d.update(name,bld_grp,phone,place,don_date,id)
    if val:
        st.success("Donor details Updated successfully")
    else:
        st.error("Donor not Found")
