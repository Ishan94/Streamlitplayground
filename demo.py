import pandas as pd

import streamlit as st

st.markdown(
    """
    <style>
    h1 {
        color: red;
    }

    .st-key-first-expander [data-testid="stExpander"] details summary,
    .st-key-first-expander [data-testid="stExpander"] details[open] summary {
        background-color: #1f77ff;
        color: white;
    }

    .st-key-second-expander [data-testid="stExpander"] details summary {
        background-color: #2ca02c;
        color: white;
    }

    .st-key-second-expander [data-testid="stExpander"] details[open] summary {
        background-color: #ffd700;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Expander Test")

with st.container(key="first-expander"):
    with st.expander("Click ME!"):
        st.write("This is content")
        st.button("A button")

with st.container(key="second-expander"):
    with st.expander("Another one"):
        st.write("More content here")