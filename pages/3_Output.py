import streamlit as st
import os, zipfile
import pandas as pd

df_data = {
    "Standard": [],
    "Matching Number": [],
    "Filename": [],
}

def zip_outputs():
    if os.path.exists('./outputs.zip'):
        os.remove('./outputs.zip')
    with zipfile.ZipFile('./outputs.zip', 'w') as zipf:
        for filename in os.listdir('./outputs/'):
            if filename.split('.')[-1] != 'txt':
                file_path = './outputs/' + filename
                zipf.write(file_path, compress_type=zipfile.ZIP_DEFLATED)

def get_outputs(get_match: bool):
    df_data['Standard'] = []
    df_data['Matching Number'] = []
    df_data['Filename'] = []
    files = os.listdir('./outputs/')
    for file in files:
        if file.split('.')[-1] != 'txt':
            list_name, matching_number, filename = file.split('&')
            if matching_number != '0' or not get_match:
                df_data['Standard'].append(list_name)
                df_data['Matching Number'].append(matching_number)
                df_data['Filename'].append(filename)
    df = pd.DataFrame(df_data)
    df['Matching Number'] = df['Matching Number'].astype(int)
    return df

def clear_folder():
    files = os.listdir('./outputs/')
    for file in files:
        if file.split('.')[-1] != 'txt':
            os.remove(os.path.join('./outputs/', file))

def main():
    st.title(' 📁 Outputs')
    st.header("All the files in output folder:", divider='rainbow')
    st.dataframe(
        get_outputs(False),
        hide_index=True,
    )
    st.header("List of files with matching CAS number:", divider='rainbow')
    st.dataframe(
        get_outputs(True),
        hide_index=True,
    )
    st.divider()
    end_col1, end_col2 = st.columns(2)
    with end_col1:
        st.subheader("Download all output files:")
        zip_outputs()
        with open('outputs.zip', 'rb') as datazip:
            st.download_button(
                label='Download ZIP',
                data=datazip,
                file_name="outputs.zip",
                mime="application/octet-stream"
                )
    with end_col2:
        st.subheader("Clear all output files:")
        st.button(label='Clear Outputs', on_click=clear_folder)

if __name__ == '__main__':
    st.set_page_config(page_title='Output', page_icon='./sources/johnson.jpg')
    st.logo(image='./sources/johnson.jpg')
    main()