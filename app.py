import streamlit as st
import pandas as pd
from statsmodels.tsa.arima.model import ARIMAResults

# Load the saved model
model = ARIMAResults.load('sarimax_model.pkl')

# Streamlit App
st.title('Exchange Rate Prediction App')

# User Input
st.sidebar.header('User Input')

# Date Picker
user_input_date = st.sidebar.date_input('Select a Date', pd.to_datetime('2023-01-01'))

# Currency Selection Dropdowns
currencies = ['SA RAND', 'US DOLLAR', 'KES / BIF', 'CAN $', 'KES / TSHS']
user_input_base_currency = st.sidebar.selectbox('Select Base Currency', currencies)
user_input_target_currency = st.sidebar.selectbox('Select Target Currency', currencies)

# Make Predictions
if st.button('Predict'):
    # Make predictions using the saved model
    # You may need to adjust this part based on the features expected by your model
    # For example, if your model expects additional features or lag values, provide them here
    forecast_result = model.get_forecast(steps=1)  # Adjust the steps parameter based on your requirements

    # Access the predicted mean values
    prediction = forecast_result.predicted_mean

    # Display the prediction
    st.subheader(f'Predicted Exchange Rate for {user_input_base_currency} to {user_input_target_currency} '
                 f'on {user_input_date}: {prediction.iloc[0]}')

