import numpy  as np 
import pandas as pd
import pickle as pkl
import streamlit as st

model = pkl.load(open("MIPML.pkl", "rb"))

st.header("Medical insurance Prediction App")

gender = st.selectbox("Choose Gender", ["Female", "Male"])
smoker = st.selectbox("Are you a smoker?", ["yes", "No"])
region = st.selectbox("Choose Region", ["SouthEast", "SouthWest", "NorthEast", "NorthWest"])
age = st.slider("Enter Age", 5, 100)
bmi = st.slider("Enter BMI", 5, 100)
children = st.slider("Choose number of children", 0, 5)


if gender == "Female":
    gender = 0
else :
    gender = 1

if smoker == "No":
    smoker = 0
else :
    smoker = 1

if region == "SouthEast":
    region  = 0
if region == "SouthWest":
    region  = 1
if region == "NorthEast":
    region  = 2
else :
    region  = 3

input_data = (age, gender, bmi, children, smoker, region)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)


if st.button("Predict"):
    predicted_prem = model.predict(input_data)

    display_string = f"Insurance Premium will be {round(predicted_prem[0], 2)} USD Dollars"

    st.markdown(display_string)
