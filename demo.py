import pandas as pd

import streamlit as st

st.markdown(
    """
    <style>
    h1 {
        color: red;
    }

    [data-testid="stExpander"]:nth-of-type(1) details summary,
    [data-testid="stExpander"]:nth-of-type(1) details[open] summary {
        background-color: #1f77ff;
        color: white;
    }

    [data-testid="stExpander"]:nth-of-type(2) details summary {
        background-color: #2ca02c;
        color: white;
    }

    [data-testid="stExpander"]:nth-of-type(2) details[open] summary {
        background-color: #ffd700;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Expander Test")

with st.expander("Click ME!"):
    st.write("This is content")
    st.button("A button", key="first_expander_button")

with st.expander("Another one"):
    st.write("More content here")