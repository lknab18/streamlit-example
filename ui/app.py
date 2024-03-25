import streamlit as st
from menu import menu

# Initialize st.session_state.demo to None
if "demo" not in st.session_state:
    st.session_state.demo = None

# Retrieve the demo from Session State to initialize the widget
st.session_state._demo = st.session_state.demo

def set_demo(**kwargs):
    # Callback function to save the demo selection to Session State
    #previous_demo = st.session_state.demo
    st.session_state.demo = kwargs['demo']
    
    #load models based on demo choice and models loaded from past demo

def demo_change_popup():
    form = st.form("my_form")
    form.text("Changing the demo will unload previously loaded models.\nPress button below to proceed.")
    form.form_submit_button("Submit", on_click=set_demo, kwargs = {"demo": st.session_state._demo})

# Selectbox to choose demo
st.selectbox(
    "Select a demo:",
    [None, "demo1", "demo2"],
    key="_demo",
    on_change=demo_change_popup,
)

st.header("Demo 1 Name")
st.text("Demo 1 description")
st.header("Demo 2 Name")
st.text("Demo 1 description")

menu() # Render the dynamic menu!
