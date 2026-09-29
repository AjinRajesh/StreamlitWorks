import streamlit as st

st.title("Division")


n1=st.number_input("Enter number 1")
n2=st.number_input("Enter number 2")

btn=st.button("Divide")
if btn:
    st.write("Result is:",n1/n2)