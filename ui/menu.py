import streamlit as st

def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("app.py", label="Switch demos")
    demo = st.session_state.demo
    match demo:
        case "demo1":
            st.sidebar.page_link("pages/image-segmentation.py", label="Demo 1: Image Segmentation")
        case "demo2":
            st.sidebar.page_link("pages/uber-data.py", label="Demo 2: Uber Data")


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("app.py", label="Choose demo")


def menu():
    # Determine if a user is logged in or not, then show the correct
    # navigation menu
    if "demo" not in st.session_state or st.session_state.demo is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # Redirect users to the main page if not logged in, otherwise continue to
    # render the navigation menu
    if "demo" not in st.session_state or st.session_state.demo is None:
        st.switch_page("app.py")
    menu()