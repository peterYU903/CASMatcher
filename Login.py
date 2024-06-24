import streamlit as st
import hmac, os
from dotenv import load_dotenv
from st_pages import Page, show_pages

def check_password():
    def password_entered():
        if hmac.compare_digest(st.session_state["password"], os.getenv("password")):
            st.session_state["password_correct"] = True
            del st.session_state["password"]
        else:
            st.session_state["password_correct"] = False
    if st.session_state.get("password_correct", False):
        return True
    st.header("Please enter the password to access CASMatcher:")
    st.text_input("Password", type="password", on_change=password_entered, key="password")
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False

def main():
    load_dotenv()
    if not check_password():
        st.stop()
    else:
        st.header("Welcome to CASMatcher. :smile:", )
        show_pages(
            [
                Page("Login.py", "Login", "🔑"),
                Page("pages/1_Guideline.py", "Guideline", "📚"),
                Page("pages/2_CasMatcher.py", "CasMatcher", "📋"),
                Page("pages/3_Output.py", "Outputs", "📁")
            ]
        )
        st.logo(image='./sources/johnson.jpg')

if __name__ == '__main__':
    st.set_page_config("Login", page_icon='sources/johnson.jpg')
    st.title("🔑 Login to CasMatcher")
    show_pages([Page("Login.py", "Login", "🔑")])
    main()