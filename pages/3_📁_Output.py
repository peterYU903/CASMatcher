import streamlit as st
import os
import pandas as pd

df_data = {
    "Standard": [],
    "Matching Number": [],
    "Filename": [],
}

def get_outputs():
    df_data['Standard'] = []
    df_data['Matching Number'] = []
    df_data['Filename'] = []
    files = os.listdir('outputs/')
    for file in files:
        list_name, matching_number, filename = file.split('&')
        df_data['Standard'].append(list_name)
        df_data['Matching Number'].append(matching_number)
        df_data['Filename'].append(filename)
    df = pd.DataFrame(df_data)
    df['Matching Number'] = df['Matching Number'].astype(int)
    return df

st.set_page_config(page_title='Output', page_icon='sources/johnson.jpg')
st.logo(image='sources/johnson.jpg')

st.header("All the files in output folder:")
st.dataframe(
            get_outputs(),
            hide_index=True,
        )