import streamlit as st

st.title("BMI Calculator")
wt=st.number_input("Enter weight in kg")
ht=st.number_input("Enter height in cm")
btn=st.button("BMI")
if btn:
    bmi=wt/(ht/100)**2
    st.write(bmi)
    if bmi<18.5:
        st.info("UNDERWEIGHT")
    elif 18.5<=bmi<25:
        st.success("Normal")
    elif 25<=bmi<=30:
        st.error("Overweight")
    elif bmi>30:
        st.warning("OBESITY")