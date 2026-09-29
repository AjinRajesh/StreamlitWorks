import streamlit as st

#text_input()

#number_input()
num1=st.number_input("Enter Number 1")
num2=st.number_input("Enter Number 2")
name=st.text_input("Enter your name")

#date
date=st.date_input("Enter date")


#Button
btn=st.button("Click")
if btn:
    st.write("BRAVO")
    st.write(num1)
    st.write(num2)
    st.write(name)
    st.write(num1 + num2)
    st.write(date)