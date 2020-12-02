import streamlit as st
import pandas as pd
import numpy as np

st.title('Weekly Deaths from Pneumonia, Influenza, or COVID-19')

DATA_SOURCE = './NCHSData47.csv'
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


# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
st.subheader('Deaths per week *')
year_filter = st.slider(YEAR, 2014, 2020)
filtered_data = data[data[YEAR] == year_filter]

st.bar_chart(data=filtered_data.set_index(WEEK)[[ALL_DEATHS, COVID19_DEATHS, INFLUENZA_DEATHS, PNEUMONIA_DEATHS]], use_container_width=True)

st.text('* Data for 2020 is incomplete')
st.text('Check out my Github for other projects')
st.markdown('[https://github.com/greenfructose]')