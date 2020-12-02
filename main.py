import streamlit as st
import pandas as pd
import numpy as np

st.title('Weekly Deaths from Pneumonia, Influenza, or COVID-19')

DATA_SOURCE = 'NCHSData47.CSV'
YEAR = 'year'
WEEK = 'week'
ALL_DEATHS = 'all deaths'
PNEUMONIA_DEATHS = 'pneumonia deaths'
INFLUENZA_DEATHS = 'influenza deaths'
COVID19_DEATHS = 'covid-19 deaths'


@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_SOURCE, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Done! (using st.cache)')
st.subheader('Deaths per week')


st.bar_chart(data=data[[ALL_DEATHS, PNEUMONIA_DEATHS, INFLUENZA_DEATHS, COVID19_DEATHS]])