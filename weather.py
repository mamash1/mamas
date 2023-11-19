import streamlit as st
import requests
import time

#1

def get_temperature(api_key, city):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        temperature = data["main"]["temp"]
        return temperature
    except Exception as e:
        print(f"Error: {e}")
        return None

# Streamlit app
st.title("Real-Time Temperature in Limassol")

# API key input (replace with your actual OpenWeatherMap API key)
api_key = "a8dcb5acefdcb38357cf12102169abdc"

# Default city
default_city = "Limassol,CY"

# Real-time temperature for the default city
default_temperature = get_temperature(api_key, default_city)

if default_temperature is not None:
    st.success(f"The current temperature in {default_city} is {default_temperature}°C.")
else:
    st.error("Failed to retrieve temperature. Please check your API key and network connection.")


#2
def get_temperature(city):
    api_key = "a8dcb5acefdcb38357cf12102169abdc"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": api_key, "units": "metric"}  

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        temperature = data["main"]["temp"]
        return temperature
    except Exception as e:
        print(f"Error: {e}")
        return None

# Streamlit app
st.title("Real-Time Temperature of your choosen city")

# City selection

selected_city = st.text_input("Select a city:")

# Check temperature button
if st.button("Check Temperature"):
    if selected_city:
        temperature = get_temperature(selected_city)
        if temperature is not None:
            st.success(f"The current temperature in {selected_city} is {temperature}°C.")
        else:
            st.error("Failed to retrieve temperature. Please check your input.")
    else:
        st.warning("Please enter a city before checking temperature.")

#3


def get_currency_rate(api_key, base_currency, target_currency):
    base_url = "https://open.er-api.com/v6/latest"
    params = {"base": base_currency, "apikey": api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        rate = data["rates"].get(target_currency)
        return rate
    except Exception as e:
        print(f"Error: {e}")
        return None

# Streamlit app
st.title("Real-Time Currency Exchange Rates")

# API key input (replace with your actual ExchangeRate-API key)
api_key = "43d8dec514da24164ab13722"

# Base currency
base_currency = "EUR"

# Target currencies
target_currencies = ["GBP", "JPY", "USD"]

# Display real-time currency exchange rates
for target_currency in target_currencies:
    rate = get_currency_rate(api_key, base_currency, target_currency)
    if rate is not None:
        st.success(f"The exchange rate from {base_currency} to {target_currency} is {rate:.4f}.")
    else:
        st.error("Failed to retrieve exchange rate. Please check your API key and network connection.")


#4


def get_currency_rate(api_key, base_currency, target_currency):
    base_url = "https://open.er-api.com/v6/latest"
    params = {"base": base_currency, "apikey": api_key}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        rate = data["rates"].get(target_currency)
        return rate
    except Exception as e:
        print(f"Error: {e}")
        return None

# Streamlit app
st.title("Real-Time Currency Converter")

# API key input (replace with your actual ExchangeRate-API key)
api_key = "43d8dec514da24164ab13722"

# Base currency selection
base_currency = st.selectbox("Select the base currency:", ["EUR", "GBP", "JPY", "USD"])

# Input amount in the base currency
base_amount = st.number_input("Enter the amount in the base currency:", min_value=0.01, value=1.0, step=0.01)

# Target currencies
target_currencies = ["EUR", "GBP", "JPY", "USD"]

# Display converted values
st.header("Converted Values:")
for target_currency in target_currencies:
    rate = get_currency_rate(api_key, base_currency, target_currency)
    if rate is not None:
        converted_value = base_amount * rate
        st.success(f"{base_amount:.2f} {base_currency} is equal to {converted_value:.2f} {target_currency}.")
    else:
        st.error("Failed to retrieve exchange rate. Please check your API key and network connection.")


