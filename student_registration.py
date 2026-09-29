import streamlit as st
from datetime import date

st.title("Student Registration Form")

name=st.text_input("Name")
age=st.number_input("Age",min_value=0)

#date boundaries
min_date=date(1990,1,1)
max_date=date.today()
dob=st.date_input("DOB",value=min_date,min_value=min_date,max_value=max_date)

email=st.text_input("Email")

g=st.radio("Gender",['Male','Female'])

s=st.selectbox('Courses',['Python','dotnet','Testing'])

btn=st.button("Submit")
if btn:
    st.write("NAME:",name)
    st.write("AGE:",age)
    st.write("DOB:",dob)
    st.write("Email:",email)
    st.write("Gender:",g)
    st.write("Course:",s)