import streamlit as st

st.title("Addition")

st.write("Number 1")
n1=st.number_input("Enter number 1")
st.write("Number 2")
n2=st.number_input("Enter number 2")
btn=st.button("Click")
if btn:
    st.write("Sum is:",n1+n2)