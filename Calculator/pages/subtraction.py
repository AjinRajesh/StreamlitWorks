import streamlit as st

st.title("Subtraction")


n1=st.number_input("Enter number 1")
n2=st.number_input("Enter number 2")

btn=st.button("Subtract")
if btn:
    st.write("Difference is:",n1-n2)