import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

# Set page configuration for a wider layout and green theme
st.set_page_config(layout="wide", page_title="Peatland Monitoring", page_icon="🌿")

# Add custom CSS for styling
st.markdown("""
<style>
    body {
        background-color: #f0f9f4;
    }
    .title {
        font-size: 48px;
        color: #2E8B57; /* Dark green */
        text-align: center;
        margin-top: 20px;
    }
    .header {
        font-size: 36px;
        color: #3CB371; /* Medium sea green */
        margin-top: 20px;
    }
    .subheader {
        font-size: 24px;
        color: #556B2F; /* Dark olive green */
    }
    .callout {
        background-color: #e6f7e6;
        border-left: 4px solid #2E8B57;
        padding: 10px;
        margin: 20px 0;
    }
    .footer {
        text-align: center;
        padding: 20px;
        background-color: #3CB371;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Create the DataFrame
df = pd.DataFrame({
    'Date': [2018, 2021, 2022, 2023, 2024],
    'NDVI': [1, 1, 0.665254, 0.64197, 0.702914],
    'NDWI': [0.711013, 0.626983, 0.614526, 0.612952, 0.499578],
    'NDMI': [0.3099, 0.3027745, 0.295649, 0.285479, 0.269119]
})

# Set the Date as the index
df.set_index('Date', inplace=True)

# Function to fit ARIMA model and forecast
def fit_arima_and_forecast(data, order=(1, 1, 1), steps=2):
    model = ARIMA(data, order=order)
    model_fit = model.fit()
    forecast = model_fit.forecast(steps=steps)
    return forecast

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.radio("Select a section:", 
                             ["Home", "Peatland Knowledge Base", "Carbon Footprint Analysis", 
                              "Stakeholder Connections", "Time Series Analysis", 
                              "Correlation Analysis", "Spatial and Clustering Analysis"])

# Home Section with Hero Image
if options == "Home":
    st.markdown("<h1 class='title'>Welcome to Peatland Monitoring</h1>", unsafe_allow_html=True)
    st.image("/Users/swastika/IIRS/PYTHON/peatland-7.jpg", use_container_width=True)  # Replace with actual image URL
    st.write("Explore our resources and analyses related to peatland health and restoration efforts.")
    
# Peatland Knowledge Base Section
elif options == "Peatland Knowledge Base":
    st.markdown("<h2 class='header'>Peatland Knowledge Base</h2>", unsafe_allow_html=True)
    st.write("Welcome to the peatland knowledge base section where you can learn about peatland ecosystems...")
    
# Carbon Footprint Analysis Section
elif options == "Carbon Footprint Analysis":
    st.markdown("<h2 class='header'>Carbon Footprint Analysis</h2>", unsafe_allow_html=True)
    st.write("This section provides tools for calculating and analyzing carbon footprints related to peatland activities...")
    
# Stakeholder Connection Section
elif options == "Stakeholder Connections":
    st.markdown("<h2 class='header'>Stakeholder Connections</h2>", unsafe_allow_html=True)
    st.write("Connect with stakeholders involved in peatland monitoring and restoration efforts...")
    
# Time Series Analysis Section
elif options == "Time Series Analysis":
    st.markdown("<h2 class='header'>ARIMA Time Series Forecasting</h2>", unsafe_allow_html=True)
    
    # Fit ARIMA models for NDVI, NDWI and NDMI
    ndvi_forecast = fit_arima_and_forecast(df['NDVI'])
    ndwi_forecast = fit_arima_and_forecast(df['NDWI'])
    ndmi_forecast = fit_arima_and_forecast(df['NDMI'])

    # Display forecasts with callout box
    st.markdown("<div class='callout'><strong>Forecast Results:</strong></div>", unsafe_allow_html=True)
    st.write("NDVI Forecast Values:", ndvi_forecast)
    st.write("NDWI Forecast Values:", ndwi_forecast)
    st.write("NDMI Forecast Values:", ndmi_forecast)

# Correlation Analysis Section
elif options == "Correlation Analysis":
    st.markdown("<h2 class='header'>Correlation Analysis</h2>", unsafe_allow_html=True)
    
    correlation_matrix = df.corr()
    
    st.write("Correlation Matrix:")
    st.write(correlation_matrix)

# Spatial and Clustering Analysis Section
elif options == "Spatial and Clustering Analysis":
    st.markdown("<h2 class='header'>Spatial and Clustering Analysis</h2>", unsafe_allow_html=True)
    
    # Replace with actual image paths or URLs
    st.image("/Users/swastika/IIRS/ndmi_diff_map.png", caption="NDMI Difference Map")
    st.image("/Users/swastika/IIRS/ndwi_diff_map.png", caption="NDWI Difference Map")
    st.image("/Users/swastika/IIRS/ndvi_diff_map.png", caption="NDVI Difference Map")
    
# Footer with Resources
st.markdown("""
<div class='footer'>
<p>©2024 Peatland Monitoring Project | <a href="swastika21csu450@ncuindia.edu" style="color:white;">Contact Us</a> | <a href="https://www.linkedin.com/in/swastika30/" style="color:white;">LinkedIn</a></p>
</div>
""", unsafe_allow_html=True)
