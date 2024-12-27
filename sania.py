import streamlit as st
import requests

# Set up the Streamlit app
st.title("Node.js Backend + Streamlit Frontend")

# API Base URL
BASE_URL = "http://localhost:3000/api"

# Get Request Example
if st.button("Fetch Data"):
    response = requests.get(f"{BASE_URL}/data")
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("Failed to fetch data.")

# Post Request Example
user_input = st.text_input("Enter some data to send to backend:")
if st.button("Submit Data"):
    response = requests.post(f"{BASE_URL}/submit", json={"data": user_input})
    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("Failed to submit data.")
