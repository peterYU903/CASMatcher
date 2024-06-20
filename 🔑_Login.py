# import streamlit as st
# import hmac
# import json
# from pathlib import Path
# from streamlit.source_util import _on_pages_changed, get_pages

# DEFAULT_PAGE = "🔑_Login.py"

# def get_all_pages():
#     default_pages = get_pages(DEFAULT_PAGE)
#     pages_path = Path("pages.json")
#     if pages_path.exists():
#         saved_default_pages = json.loads(pages_path.read_text())
#     else:
#         saved_default_pages = default_pages.copy()
#         pages_path.write_text(json.dumps(default_pages, indent=4))
#     return saved_default_pages

# def clear_all_but_first_page():
#     current_pages = get_pages(DEFAULT_PAGE)
#     if len(current_pages.keys()) == 1:
#         return
#     key, val = list(current_pages.items())[0]
#     current_pages.clear()
#     current_pages[key] = val
#     _on_pages_changed.send()

# def show_all_pages():
#     current_pages = get_pages(DEFAULT_PAGE)
#     saved_pages = get_all_pages()
#     for key in saved_pages:
#         if key not in current_pages:
#             current_pages[key] = saved_pages[key]
#     _on_pages_changed.send()

# def check_password():
#     def password_entered():
#         if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):
#             st.session_state["password_correct"] = True
#             del st.session_state["password"]
#         else:
#             st.session_state["password_correct"] = False
#     if st.session_state.get("password_correct", False):
#         return True
#     st.set_page_config(page_title='Login', page_icon='sources/johnson.jpg')
#     st.header("Please enter the password to access CASMatcher:")
#     st.text_input("Password", type="password", on_change=password_entered, key="password")
#     if "password_correct" in st.session_state:
#         st.error("😕 Password incorrect")
#     return False

# def main():
#     if not check_password():
#         clear_all_but_first_page()
#         st.stop()
#     else:
#         show_all_pages()
#         st.set_page_config(page_title='Login', page_icon='sources/johnson.jpg')
#         st.logo(image='sources/johnson.jpg')
#         st.header("Welcome to CASMatcher. :smile:", )
# main()