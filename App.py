
import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

st.set_page_config(page_title="Clash Royale Card Type Predictor")

st.title("🎮 Clash Royale Card Type Prediction")
st.write("Predict whether a card is **Troop / Spell / Building** using Logistic Regression")

# Load dataset
data = pd.read_excel("clash_royale_cards.xlsx")

# Features & target
X = data[["hitpoints", "elixirCost", "usage"]]
y = data["type"]

# Preprocessing
imputer = SimpleImputer(strategy="mean")
X = imputer.fit_transform(X)

scaler = StandardScaler()
X = scaler.fit_transform(X)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

st.success("Model trained successfully!")

st.header("Enter Card Details")

# User Inputs
hitpoints = st.number_input("Hitpoints", min_value=0)
elixirCost = st.number_input("Elixir Cost", min_value=0)
usage = st.number_input("Usage (%)", min_value=0.0)

# Prediction
if st.button("Predict Card Type"):
    new_card = [[hitpoints, elixirCost, usage]]
    new_card = imputer.transform(new_card)
    new_card = scaler.transform(new_card)

    prediction = model.predict(new_card)

    st.subheader("Prediction Result")
    st.success(f"Predicted Card Type: **{prediction[0]}**")
  
