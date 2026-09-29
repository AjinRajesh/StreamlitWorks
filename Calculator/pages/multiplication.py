import streamlit as st

st.title("Multiplication")


n1=st.number_input("Enter number 1")
n2=st.number_input("Enter number 2")

btn=st.button("Multiply")
if btn:
    st.write("Product is:",n1*n2)