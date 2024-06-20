import streamlit as st
import os
import pandas as pd

df_data = {
    "Standard": [],
    "Matching Number": [],
    "Filename": [],
}

def get_match_data():
    df_data['Standard'] = []
    df_data['Matching Number'] = []
    df_data['Filename'] = []
    files = os.listdir('outputs/')
    for file in files:
        list_name, matching_number, filename = file.split('&')
        if matching_number != '0':
            df_data['Standard'].append(list_name)
            df_data['Matching Number'].append(matching_number)
            df_data['Filename'].append(filename)
    return pd.DataFrame(df_data)

st.dataframe(
            get_match_data(),
            hide_index=True,
        )