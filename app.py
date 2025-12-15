import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("CR.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Clash Royale Card Type Predictor 🏰")

st.write("Enter card details to predict whether it is a **troop**, **spell**, or **building**.")

# User inputs
hitpoints = st.number_input("Hitpoints", min_value=0, value=1500)
elixir_cost = st.number_input("Elixir Cost", min_value=0, value=4)
usage = st.number_input("Usage (%)", min_value=0.0, value=20.5)

if st.button("Predict Card Type"):
    input_data = np.array([[hitpoints, elixir_cost, usage]])
    prediction = model.predict(input_data)
    st.success(f"Predicted Card Type: **{prediction[0]}**")

