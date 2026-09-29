import streamlit as st

st.title("Addition")


n1=st.number_input("Enter number 1",min_value=0)
n2=st.number_input("Enter number 2",min_value=0)

btn=st.button("ADD")
if btn:
    st.write("Sum is:",n1+n2)