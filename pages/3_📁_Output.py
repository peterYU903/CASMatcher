import streamlit as st
import os, zipfile
import pandas as pd

df_data = {
    "Standard": [],
    "Matching Number": [],
    "Filename": [],
}

def zip_outputs():
    os.remove('./outputs.zip')
    with zipfile.ZipFile('./outputs.zip', 'w') as zipf:
        for filename in os.listdir('./outputs/'):
            if filename.split('.')[-1] != 'txt':
                file_path = './outputs/' + filename
                zipf.write(file_path, compress_type=zipfile.ZIP_DEFLATED)

def get_outputs():
    df_data['Standard'] = []
    df_data['Matching Number'] = []
    df_data['Filename'] = []
    files = os.listdir('./outputs/')
    for file in files:
        if file.split('.')[-1] != 'txt':
            list_name, matching_number, filename = file.split('&')
            df_data['Standard'].append(list_name)
            df_data['Matching Number'].append(matching_number)
            df_data['Filename'].append(filename)
    df = pd.DataFrame(df_data)
    df['Matching Number'] = df['Matching Number'].astype(int)
    return df

st.set_page_config(page_title='Output', page_icon='./sources/johnson.jpg')
st.logo(image='./sources/johnson.jpg')

st.header("All the files in output folder:")
st.dataframe(
            get_outputs(),
            hide_index=True,
        )
st.header("Download the output files:")
with open('outputs.zip', 'rb') as datazip:
    st.download_button(
        label='Download ZIP',
        data=datazip,
        file_name="outputs.zip",
        mime="application/octet-stream"
        )