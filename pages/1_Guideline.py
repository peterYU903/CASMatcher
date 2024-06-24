import streamlit as st

def main():
    st.title(':books: Guideline')
    st.markdown('**1. Go to the "CasMatcher" page.**')
    st.markdown('**2. Upload standard lists that you want to use for comparison.**')
    st.markdown('**3. Select the standard list for comparison.**')
    st.markdown('**4. Upload the MAS Reports before process.**')
    st.caption('*Please wait until all reports are uploaded for next step.')
    st.markdown('**5. Press the "Process" button.**')
    st.caption('*Wait until operation success.')
    st.markdown('**6. Go to the "Outputs" page.**')
    st.markdown('**7. Download the output files via "Download ZIP" button.**')

if __name__ == '__main__':
    st.set_page_config(page_title='Guideline', page_icon='./sources/johnson.jpg')
    st.logo(image='./sources/johnson.jpg')
    main()